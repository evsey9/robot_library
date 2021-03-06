#!/usr/bin/env python3

import rospy
from robot_library.srv import *
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from tf.transformations import euler_from_quaternion


z = Float64()

def callback(msg):
    global z
    quaternion = msg.pose.pose.orientation
    quaternion_list = [quaternion.x, quaternion.y, quaternion.z, quaternion.w]
    # rospy.loginfo("Quaternion list: %s"%(quaternion_list))
    (roll, pitch, yaw) = euler_from_quaternion(quaternion_list)
    z = yaw
    # rospy.loginfo("Direction: %s" % (z))


def handle_get_direction(req):
    rospy.loginfo("New request for direction of robot")
    return GetDirectionResponse(z)


def get_girection_server():
    rospy.init_node('get_direction_server',  anonymous=True)
    rospy.Subscriber("/r1/odom", Odometry, callback)
    s = rospy.Service('get_direction', GetDirection, handle_get_direction)
    print("Ready to sending current direction.")
    rospy.spin()

if __name__ == "__main__":
    get_girection_server()
