#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char** argv){
	ros::init(argc, argv, "greeting_talker");
	ros::NodeHandle nh;
	ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("chatter_cpp", 10);
	ros::Rate loop_rate(10);

	while(ros::ok()){
		std_msgs::String msg;
		msg.data = "Hello world from the talker_cpp";
		ROS_INFO(msg.data.c_str());
		chatter_pub.publish(msg);
		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}
