#!/usr/bin/env python3

import rospy
from robosys_mypkg.msg import data
from std_msgs.msg import Float32

def callback(msg):
    pub = rospy.Publisher('Answer', Float32, queue_size=1)
    if msg.ope == "+":
        ans = msg.a + msg.b
    elif msg.ope == "-":
        ans = msg.a - msg.b
    elif msg.ope == "*":
        ans = msg.a * msg.b
    elif msg.ope == "/":
        ans = msg.a / msg.b
    print(ans)
    pub.publish(ans)

def calculate_mode():
    rospy.init_node('calculate')
    rate = rospy.Rate(10)
    sub = rospy.Subscriber('input_data', data, callback)
    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    calculate_mode()
