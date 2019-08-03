#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class take_photo:

    def __init__(self):
        rospy.init_node('take_photo',anonymous = False)
        self.switch = False
        self.bridge = CvBridge()
        # change the image topic name 
        image_sub = rospy.Subscriber ("/astra/rgb/image_raw", Image, self.callback)
        rospy.sleep(1)

    def callback(self, msg):
    
        self.image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
        self.switch = True
        
    def take(self,result_path):
        if self.switch == True:
            cv2.imwrite(result_path, self.image)
         # press keyborad to destory windows or change it like cv2.waitKey(1000), the time to wait is 1000ms 
            cv2.imshow("my_img", self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()





if __name__ == "__main__":

    my_pic = take_photo()
    #use your path to save the result
    my_pic.take("/home/hts/rchome_tutorial/robocup_vision_tutorial/test_imgs/my_img1.jpg")