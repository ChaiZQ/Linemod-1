#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from object_recognition_msgs.msg import *

i = 0
averagePoints = []
printed = 0
def callback(data):
    global averagePoints
    global i
    global printed
    rospy.loginfo(averagePoints)
    rospy.loginfo("i = %d", i)
    if len(data.objects) == 0:
         rospy.loginfo("nothing detected")
         return
    if i > 100:
	if printed == 0:
            rospy.loginfo("average = %f", sum([i for i in averagePoints])/len(averagePoints))
            #rospy.loginfo("average x = %f", sum([i.x for i in averagePoints])/len(averagePoints))
            #rospy.loginfo("average y = %f", sum([i.y for i in averagePoints])/len(averagePoints))
            #rospy.loginfo("average z = %f", sum([i.z for i in averagePoints])/len(averagePoints))
            printed = 1
	    return
	return
    
    
    #rospy.loginfo(rospy.get_caller_id() + "I heard \n%s", data.objects[0].pose.pose.pose.position)
    rospy.loginfo(rospy.get_caller_id() + "I heard \n%s", data.objects[0].type.key)
    i = i + 1
    #averagePoints.append(data.objects[0].pose.pose.pose.position)
    if data.objects[0].type.key == "8779c7f97b6f1fdeeb7b091601000a95":
         averagePoints.append(1.0)
         rospy.loginfo("true")
    else:
         averagePoints.append(0)
    return

def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("recognized_object_array", RecognizedObjectArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
