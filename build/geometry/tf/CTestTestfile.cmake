# CMake generated Testfile for 
# Source directory: /home/ucar/ucar_5/src/geometry/tf
# Build directory: /home/ucar/ucar_5/build/geometry/tf
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_tf_gtest_tf_unittest "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/gtest-tf_unittest.xml" "--return-code" "/home/ucar/ucar_5/devel/lib/tf/tf_unittest --gtest_output=xml:/home/ucar/ucar_5/build/test_results/tf/gtest-tf_unittest.xml")
add_test(_ctest_tf_gtest_tf_quaternion_unittest "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/gtest-tf_quaternion_unittest.xml" "--return-code" "/home/ucar/ucar_5/devel/lib/tf/tf_quaternion_unittest --gtest_output=xml:/home/ucar/ucar_5/build/test_results/tf/gtest-tf_quaternion_unittest.xml")
add_test(_ctest_tf_gtest_test_transform_datatypes "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/gtest-test_transform_datatypes.xml" "--return-code" "/home/ucar/ucar_5/devel/lib/tf/test_transform_datatypes --gtest_output=xml:/home/ucar/ucar_5/build/test_results/tf/gtest-test_transform_datatypes.xml")
add_test(_ctest_tf_rostest_test_transform_listener_unittest.launch "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/rostest-test_transform_listener_unittest.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ucar/ucar_5/src/geometry/tf --package=tf --results-filename test_transform_listener_unittest.xml --results-base-dir \"/home/ucar/ucar_5/build/test_results\" /home/ucar/ucar_5/src/geometry/tf/test/transform_listener_unittest.launch ")
add_test(_ctest_tf_gtest_test_velocity "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/gtest-test_velocity.xml" "--return-code" "/home/ucar/ucar_5/devel/lib/tf/test_velocity --gtest_output=xml:/home/ucar/ucar_5/build/test_results/tf/gtest-test_velocity.xml")
add_test(_ctest_tf_gtest_cache_unittest "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/gtest-cache_unittest.xml" "--return-code" "/home/ucar/ucar_5/devel/lib/tf/cache_unittest --gtest_output=xml:/home/ucar/ucar_5/build/test_results/tf/gtest-cache_unittest.xml")
add_test(_ctest_tf_rostest_test_test_message_filter.xml "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/rostest-test_test_message_filter.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ucar/ucar_5/src/geometry/tf --package=tf --results-filename test_test_message_filter.xml --results-base-dir \"/home/ucar/ucar_5/build/test_results\" /home/ucar/ucar_5/src/geometry/tf/test/test_message_filter.xml ")
add_test(_ctest_tf_rostest_test_test_broadcaster.launch "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/rostest-test_test_broadcaster.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ucar/ucar_5/src/geometry/tf --package=tf --results-filename test_test_broadcaster.xml --results-base-dir \"/home/ucar/ucar_5/build/test_results\" /home/ucar/ucar_5/src/geometry/tf/test/test_broadcaster.launch ")
add_test(_ctest_tf_nosetests_test.testPython.py "/home/ucar/ucar_5/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_5/build/test_results/tf/nosetests-test.testPython.py.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/ucar/ucar_5/build/test_results/tf" "/usr/bin/nosetests-2.7 -P --process-timeout=60 /home/ucar/ucar_5/src/geometry/tf/test/testPython.py --with-xunit --xunit-file=/home/ucar/ucar_5/build/test_results/tf/nosetests-test.testPython.py.xml")
