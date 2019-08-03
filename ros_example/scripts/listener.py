#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# define a callback function when listen a msg then run the function
def callback(data):
    rospy.loginfo(rospy.get_caller_id()+'  '+ data.data)

def listener():
    
    rospy.Subscriber('my_pub', String, callback)
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    #spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__=='__main__':
    
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
