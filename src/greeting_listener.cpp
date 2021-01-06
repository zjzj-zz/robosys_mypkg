/*
 * Copyright(c)2021 Hikaru Jitsukawa. All rights reserved.
 */
#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(const std_msgs::String& msg){
	ROS_INFO("listener_cpp received [%s]", msg.data.c_str());
}

int main(int argc, char **argv){
	ros::init(argc, argv, "greeting_listener");
	ros::NodeHandle nh;
	ros::Subscriber sub = nh.subscribe("chatter_cpp", 10, chatterCallback);
	ros::spin();
	return 0;
}
