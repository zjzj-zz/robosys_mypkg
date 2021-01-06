#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(msg):
    print(msg)

def output_data_mode():
    rospy.init_node('output_data')
    sub = rospy.Subscriber('Answer', Float32, callback)
    rospy.spin()

if __name__ == "__main__":
    output_data_mode()
