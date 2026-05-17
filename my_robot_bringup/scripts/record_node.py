#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import csv
import time


class RecorderNode(Node):

    def __init__(self):
        super().__init__("recorder_node")

        self.file = open("/home/jaimiish/ros2_ws/src/my_robot_bringup/dataset/demo.csv", "w")
        self.writer = csv.writer(self.file)

        self.writer.writerow([
            "time",
            "base_to_forearm_joint",
            "forearm_to_hand_joint",
            "left_finger_joint",
            "right_finger_joint"
        ])

        self.start_time = time.time()

        self.subscriber = self.create_subscription(
            JointState,
            "/joint_states",
            self.record_callback,
            10
        )

        self.get_logger().info("Recording started... Press Ctrl+C to stop.")

    def record_callback(self, msg):
        t = time.time() - self.start_time

        base = 0.0
        hand = 0.0
        left = 0.0
        right = 0.0

        for i in range(len(msg.name)):
            if msg.name[i] == "base_to_forearm_joint":
                base = msg.position[i]

            if msg.name[i] == "forearm_to_hand_joint":
                hand = msg.position[i]

            if msg.name[i] == "left_finger_joint":
                left = msg.position[i]

            if msg.name[i] == "right_finger_joint":
                right = msg.position[i]

        self.writer.writerow([t, base, hand, left, right])
        self.file.flush()


def main(args=None):
    rclpy.init(args=args)

    node = RecorderNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Recording stopped.")

    node.file.close()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()