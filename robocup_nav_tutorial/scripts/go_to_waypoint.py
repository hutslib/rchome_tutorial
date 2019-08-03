#!/urs/bin/env python
# -*- encoding:UTF-8 -*-

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import Empty

class nav_to_point:
    def __init__(self):

        rospy.init_node('nav_to_point')
        self.nav_as = actionlib.SimpleActionClient('/move_base',MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")  
        self.nav_as.wait_for_server()
         # 清除costmap
        self.map_clear_srv = rospy.ServiceProxy('/move_base/clear_costmaps', Empty)
        self.map_clear_srv()
        #load dataset
        self.dataset_points = {}
        ### you need to change the path to your waypoints.txt ###
        self.load_waypoint('/home/hts/ROS_test/src/nav_test/src/waypoints.txt')
        con = True
        self.switch = True
        self.data = ''
        ########################################################################################################## 
        # This example let you to input your destination by keyboard input. you can input your waypoint name you 
        # you list in the waypoints.txt, input stop to stop this code                                          
        while con:
            print "input your navigation goal point: "
            if self.switch == True:
                str = raw_input()
                if str != 'stop':
                    self.switch = False
                    data = str
                    self.go_to_waypoint(self.dataset_points[data]) 
                else:
                    con = False
            rospy.sleep(1)
        ##########################################################################################################
        
        #################################################################################
        ###  write your own destination in your scripts, you can follow this example ####
        # self.go_to_waypoint(self.dataset_points['point1'])                         
        #################################################################################

    def load_waypoint(self, file_name):
        curr_pos = PoseStamped()
        f = open(file_name, 'r')
        sourceInLines = f.readlines()
        for line in sourceInLines:
            temp1 = line.strip('\n')
            temp2 = temp1.split(' ')
            point_temp = MoveBaseGoal()
            point_temp.target_pose.header.frame_id = '/map'
            point_temp.target_pose.header.stamp = curr_pos.header.stamp
            point_temp.target_pose.header.seq = curr_pos.header.seq
            point_temp.target_pose.pose.position.x = float(temp2[3])
            point_temp.target_pose.pose.position.y = float(temp2[5])
            point_temp.target_pose.pose.position.z = float(temp2[7])
            point_temp.target_pose.pose.orientation.x = float(temp2[10])
            point_temp.target_pose.pose.orientation.y = float(temp2[12])
            point_temp.target_pose.pose.orientation.z = float(temp2[14])
            point_temp.target_pose.pose.orientation.w = float(temp2[16])
            self.dataset_points[temp2[0]] = point_temp
        print ("↓↓↓↓↓↓↓↓↓↓↓↓point↓↓↓↓↓↓↓↓↓↓↓↓")
        print (self.dataset_points)
        print ("↑↑↑↑↑↑↑↑↑↑↑↑point↑↑↑↑↑↑↑↑↑↑↑↑")
        print ('\033[0;32m [Kamerider I] Points Loaded! \033[0m')
        return self.dataset_points



    def go_to_waypoint (self,Point):

        self.nav_as.send_goal(Point)
        self.map_clear_srv()
        count_time = 0
        # 等于3的时候就是到达目的地了
        while self.nav_as.get_state() != 3:
            count_time += 1
            rospy.sleep(1)
            # 每隔4s清除一次local map
            if count_time == 3:
                self.map_clear_srv()
                count_time = 0
        rospy.loginfo("reach goal point!")
        self.switch = True

if __name__ == "__main__":
    
    try:
        nav_to_point()
    except rospy.ROSInterruptException:
        print "------save_point_error!------"
    
