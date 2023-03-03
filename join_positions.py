#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def joint_position ():
    pub =rospy.Publisher('/base_c/command', Float64, queue_size=10)
    rospy.init_node('w_1', anonymous=False)
    rate = rospy.Rate(10)
    position=float(input())
    print (position)
    while not rospy.is_shutdown():
        hello_str = position
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
   try:
       joint_position()
   except rospy.ROSInterruptException:
        pass
        