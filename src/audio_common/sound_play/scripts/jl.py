import rospy
import math
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseArray, PoseStamped, Quaternion
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from tf import TransformListener
import numpy as np

class LaserScanProcessor:
    def __init__(self):
        self.systemInited = False
        self.systemInitCount = 0
        self.systemDelay = 5  # assuming some delay value
        self.MINIMUM_RANGE = 0.1
        self.MAX_X_FRONT = 10.0
        self.MAX_X_BACK = 10.0
        self.MAX_Y_LEFT = 5.0
        self.MAX_Y_RIGHT = 5.0
        self.goal_received = False
        self.goal_reached = False
        self.goal_ind = 0
        self.goal_yaw = 0
        self.goal_pos = None
        self.map_goal_ptr = []
        self.PUB = False
        self.tf_listener = TransformListener()
        self.goal_pub = rospy.Publisher('/goal_pose', PoseStamped, queue_size=10)

    def removeClosedPointCloud(self, scan_in, thres):
        scan_out = LaserScan()
        scan_out.header = scan_in.header
        scan_out.ranges = []
        scan_out.intensities = []
        
        for i in range(len(scan_in.ranges)):
            if scan_in.ranges[i] >= thres:
                scan_out.ranges.append(scan_in.ranges[i])
                scan_out.intensities.append(scan_in.intensities[i])
        
        return scan_out

    def TransformCoord(self, laserCloudIn):
        obstacleCoord = []
        startOri = laserCloudIn.angle_min
        angleIncrement = laserCloudIn.angle_increment

        for i in range(len(laserCloudIn.ranges)):
            obstacleMayangle = i * angleIncrement + startOri
            if obstacleMayangle > math.pi:
                obstacleMayangle -= 2 * math.pi

            x = math.cos(obstacleMayangle) * laserCloudIn.ranges[i]
            y = math.sin(obstacleMayangle) * laserCloudIn.ranges[i]
            obstacleCoord.append([x, y])
        
        return obstacleCoord

    def resetRange(self, obstacleMaycoord_in, max_x_f, max_x_b, max_y_l, max_y_r):
        obstacleMaycoord_out = []

        for i in range(len(obstacleMaycoord_in)):
            x, y = obstacleMaycoord_in[i]
            if -max_x_b <= x <= max_x_f and -max_y_l <= y <= max_y_r:
                obstacleMaycoord_out.append([x, y, i])
        
        return obstacleMaycoord_out

    def laserCloudHandler(self, laserScan):
        if not self.systemInited:
            self.systemInitCount += 1
            if self.systemInitCount >= self.systemDelay:
                self.systemInited = True
            else:
                return

        laserCloudIn = laserScan
        laserCloudIn = self.removeClosedPointCloud(laserCloudIn, self.MINIMUM_RANGE)
        obstacleCoord = self.TransformCoord(laserCloudIn)
        obstacleCoord = self.resetRange(obstacleCoord, self.MAX_X_FRONT, self.MAX_X_BACK, self.MAX_Y_LEFT, self.MAX_Y_RIGHT)

        obstacleCornerPoint = []
        for i in range(len(obstacleCoord)):
            if i == len(obstacleCoord) - 1:
                break
            if i == 0:
                obstacleCornerPoint.append(obstacleCoord[i])
            elif obstacleCoord[i + 1][2] - obstacleCoord[i][2] > 4.0:
                obstacleCornerPoint.append(obstacleCoord[i])
                obstacleCornerPoint.append(obstacleCoord[i + 1])
            if i == len(obstacleCoord) - 2:
                if obstacleCornerPoint[-1][2] != obstacleCoord[i + 1][2]:
                    obstacleCornerPoint.append(obstacleCoord[i])

        obstacleCenterPoint = []
        for i in range(0, len(obstacleCornerPoint), 2):
            if i == len(obstacleCornerPoint) - 1:
                break

            x1, y1 = obstacleCornerPoint[i][:2]
            x2, y2 = obstacleCornerPoint[i + 1][:2]
            center_x = (x1 + x2) * 0.5
            center_y = (y1 + y2) * 0.5

            if x1 == x2:
                yaw = 0.5 * math.pi
            else:
                yaw = math.atan2((y1 - y2), (x1 - x2))

            CenterPoint = [center_x, center_y, yaw]
            obstacleCenterPoint.append(CenterPoint)

        for center in obstacleCenterPoint:
            yaw = center[2]
            quaternion = quaternion_from_euler(0.0, 0.0, yaw)
            scan_goal = PoseStamped()
            scan_goal.header.frame_id = "laser_frame"
            scan_goal.header.stamp = rospy.Time.now()
            scan_goal.pose.position.x = center[0] * 0.4
            scan_goal.pose.position.y = center[1] * 0.4
            scan_goal.pose.position.z = 0.0
            scan_goal.pose.orientation = Quaternion(*quaternion)

            try:
                self.tf_listener.waitForTransform("map", "laser_frame", rospy.Time.now(), rospy.Duration(2.0))
                map_goal = self.tf_listener.transformPose("map", scan_goal)
                self.map_goal_ptr.append(map_goal)
                self.PUB = True
            except Exception as ex:
                rospy.logerr("Failed to transform point: {}".format(str(ex)))


        if self.PUB:
            num = len(obstacleCenterPoint)
            if self.goal_reached and self.goal_ind < num:
                self.goal_ind += 1
                map_goal = self.map_goal_ptr[self.goal_ind - 1]
                quaternion = map_goal.pose.orientation
                roll, pitch, current_yaw = euler_from_quaternion([quaternion.x, quaternion.y, quaternion.z, quaternion.w])
                self.goal_yaw = current_yaw
                self.goal_pos = map_goal.pose.position
                # Assuming goal_pub is initialized elsewhere in the code
                self.goal_pub.publish(map_goal)
                self.goal_received = True
                self.goal_reached = False

if __name__ == "__main__":
    rospy.init_node('laser_scan_processor')
    processor = LaserScanProcessor()
    rospy.Subscriber("/scan", LaserScan, processor.laserCloudHandler)
    rospy.spin()