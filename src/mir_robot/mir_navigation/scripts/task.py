#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped


def movebase_client(goal):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    moveBaseGoal = MoveBaseGoal()
    moveBaseGoal.target_pose = goal
    client.send_goal(moveBaseGoal)
    wait = client.wait_for_result()

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('task_py')

        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.header.stamp = rospy.Time.now()
        goal.pose.position.z = 0
        goal.pose.orientation.x = 0
        goal.pose.orientation.y = 0
        goal.pose.orientation.z = 0
        goal.pose.orientation.w = 1
        
        # first goal
        rospy.loginfo("Goal1 is executing")
        
        goal.pose.position.x = 3
        goal.pose.position.y = 8
        
        result = movebase_client(goal)
        if result:
            rospy.loginfo("Goal1 execution done!")
        
        # second goal
        rospy.loginfo("Goal1 is executing")
        
        goal.pose.position.x = 10
        goal.pose.position.y = 10
        
        result = movebase_client(goal)
        if result:
            rospy.loginfo("Goal2 execution done!")

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
