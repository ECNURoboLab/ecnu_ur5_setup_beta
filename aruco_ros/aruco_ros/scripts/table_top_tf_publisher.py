#!/usr/bin/env python
import tf
import tf.transformations as tft
import rospy
import numpy as np
rospy.init_node("tabel_top_tf_publisher")

br = tf.TransformBroadcaster()
listener = tf.TransformListener()


def get_TF(tf_listener):
    try:
        tf_listener.waitForTransform("/camera_link", "/camera_marker", rospy.Time(0), rospy.Duration(5))
        (trans, rot) = tf_listener.lookupTransform('camera_link', '/camera_marker', rospy.Time(0))
        return trans, rot
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print "fuck!!! can't get what I want fuck!!!"

rate = rospy.Rate(50)
while not rospy.is_shutdown():

    trans,rot = get_TF(listener)
    convert = tf.TransformerROS()
    camera_link_T_camera_marker = convert.fromTranslationRotation(trans,rot)
    R = tft.euler_matrix(-3.141592/2.0,0,0)
    final_transform = np.dot(camera_link_T_camera_marker, R)
    trans = tft.translation_from_matrix(final_transform)
    rot   = tft.quaternion_from_matrix(final_transform)
    br.sendTransform(trans,rot,rospy.Time.now(),"/table_top","/camera_link")
    rate.sleep()
