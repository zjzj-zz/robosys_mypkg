cmake_minimum_required(VERSION 3.0.2)
project(robosys_mypkg)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  data.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
)

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

add_Executable(greeting_talker   src/greeting_talker.cpp)
add_Executable(greeting_listener src/greeting_listener.cpp)

target_link_libraries(greeting_talker
  ${catkin_LIBRARIES}
)
target_link_libraries(greeting_listener
  ${catkin_LIBRARIES}
)
