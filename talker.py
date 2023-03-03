#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def sum(x,y):
    i=x+y
    return(i)
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    a=input("enter a:")
    b=input("enter b:")
    s=sum(a,b)
    while not rospy.is_shutdown():
        hello_str = s
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass