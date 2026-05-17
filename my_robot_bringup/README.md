# ROS2 Manipulation and Imitation Learning Prototype

This project is a simple ROS2 + Gazebo manipulation prototype.

I designed:
- mobile robot
- 2 DOF robotic arm
- two finger gripper
- pick and place simulation

The main goal of this project is to demonstrate a basic imitation learning pipeline:

manual control
→ data recording
→ autonomous replay

---

# Features

- ROS2 Jazzy
- Gazebo simulation
- Robotic arm with gripper
- Pick and place task
- Fake grasp system
- Dataset recording using CSV
- Autonomous trajectory replay

---

# Package Structure

## my_robot_description

Contains:
- URDF/Xacro files
- arm and gripper model
- RViz configuration

## my_robot_bringup

Contains:
- launch files
- Gazebo world
- bridge configuration
- recorder and playback nodes
- dataset folder

---

# Nodes

## record_node.py

Records:
- joint positions
- gripper states
- timestamps

and saves them into:

dataset/demo.csv

---

## playback_node.py

Reads the recorded CSV file and publishes the same joint commands again to replay the motion automatically.

---

# Running the Project

## Launch simulation

```bash
ros2 launch my_robot_bringup my_robot_gazebo.launch.xml
```
## Detach box initially

```bash
ros2 topic pub /gripper/detach std_msgs/msg/Empty "{}" 
```

## Start recording

```bash
ros2 run my_robot_bringup record_node.py
```

## Manual control example

### Open gripper

```bash
ros2 topic pub /left_finger_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.3}" 
```

```bash
ros2 topic pub /right_finger_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.3}" 
```

### Move arm

```bash
ros2 topic pub /base_to_forearm_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.65}" 
```


```bash
ros2 topic pub /forearm_to_hand_joint/cmd_pos std_msgs/msg/Float64 "{data: 1.1}" 
```
### close gripper

```bash
ros2 topic pub /left_finger_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.0}" 
```

```bash
ros2 topic pub /right_finger_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.0}" 
```

### Attach object

```bash
ros2 topic pub /gripper/attach std_msgs/msg/Empty "{}" 
```

### Move arm

```bash
ros2 topic pub /base_to_forearm_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.4}" 
```

```bash
ros2 topic pub /forearm_to_hand_joint/cmd_pos std_msgs/msg/Float64 "{data: 0.7}" 
```

## Playback recorded motion

```bash
ros2 run my_robot_bringup playback_node.py
```

---

# Future Improvements

- vision based object detection
- reinforcement learning
- webserver integration
- real robot implementation

---

# Author

Jaimish