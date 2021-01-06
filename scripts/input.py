#!/usr/bin/env python3

import rospy
from robosys_mypkg.msg import data

def input_data_mode():
    rospy.init_node('input', anonymous=True)
    pub = rospy.Publisher('input_data', data, queue_size=1)
    rate = rospy.Rate(10)
    msg = data()

    while not rospy.is_shutdown():
        input_data = input().split()
        msg.a = int(input_data[0])
        msg.ope = input_data[1]
        msg.b = int(input_data[2])
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    input_data_mode()
