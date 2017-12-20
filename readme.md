# UR5 Robotiq ROS moveit集成包
维护人：孙斌 邮箱：sunbuny@163.com

本项目基于indigo，为robotiq写了适配moveit的action。
集成了如下的几个功能：
- 机器人手眼标定
- aruco_marker的识别
- ikfast机器人逆运动学求解service

# 使用方法

 首先要配置好环境变量，在此不在赘述。
 
 运行ur5机器人实际机器：
 roslaunch ecnu_ur5_setup_bringup ecnu_ur5_setup.launch
 运行xtion摄像机：
 roslaunch ecnu_ur5_setup_bringup xtion.launch 
 然后打开rviz可以使用moveit的gui对机器人做一些简单的操作。

 标定机器人:
 执行机器人手眼标定，先将机器人实际环境运行起来。然后运行：
 roslaunch easy_handeye ur5_kinect_calibration_eye_on_hand.launch
 目前机器人的摄像机装在手上面。


 


