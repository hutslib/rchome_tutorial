import dlib
import cv2
import rospy

class face_detect_dlib:

    def __init__(self):

        self.detector = dlib.get_frontal_face_detector()

    def face_detection(self, img_path, result_path):
        frame = cv2.imread(img_path)
        rects = self.detector(frame, 1)
        if len(rects) != 0:
            for rect in rects:
                cv2.rectangle(frame, (rect.left(), rect.top()), (rect.right(), rect.bottom()), (0, 0, 255), 2, 8)
                cv2.imshow("dlib_face_result", frame)
                cv2.imwrite(result_path, frame)
            # press keyborad to destory windows or change it like cv2.waitKey(1000), the time to wait is 1000ms
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == '__main__':

    my_dlib = face_detect_dlib()
    ##### change the image path and result path#####
    my_dlib.face_detection("/home/hts/ROS_test/src/vision_test/test_imgs/test_img2","/home/hts/ROS_test/src/vision_test/test_imgs/result4.jpg")