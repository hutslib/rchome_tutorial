#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    # define a  publisher with topic name my_pub with massage type String 
    pub=rospy.Publisher('my_pub',String, queue_size=10)
    #initial a ros node with name takler anonymous=True means each node has its own name
    rospy.init_node('talker',anonymous=True)
    # set rate 10HZ
    rate=rospy.Rate(10) 
    # check wheather ros is shuttdown
    while not rospy.is_shutdown():
        # message 
        my_str="send msg at time %s" % rospy.get_time()
        # show log in screen
        rospy.loginfo(my_str)
        # publish your msg
        pub.publish(my_str)
        #sleep for a duration
        rate.sleep()

if __name__ == '__main__':
    try :
        talker()
    except rospy.ROSInterruptException:
        pass