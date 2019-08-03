#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class take_photo:

    def __init__(self):
        rospy.init_node('take_photo',anonymous = False)
        self.bridge = CvBridge()
        image_sub = rospy.Subscriber ("/astra/rgb/image_raw", Image, self.callback)
        rospy.sleep(1)

    def callback(self, msg):
    
        image = self.bridge.imgmsg_to_cv2(data,"bgr8")
        cv2.imwrite(result_path, image)




if __name__ == "__main__":

    my_pic = take_photo("/home/hts/rchome_tutorial/robocup_vision_tutorial/test_imgs/my_img1.jpg")