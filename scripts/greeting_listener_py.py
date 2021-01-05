#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("listener_py received [%s]",data.data)

def listener():
    rospy.init_node('greeting_listener_py', anonymous=True)
    rospy.Subscriber("chatter_cpp", String, callback)
    rospy.spin()

if __name__== '__main__':
    listener()
