#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import csv
import time


class PlaybackNode(Node):

    def __init__(self):
        super().__init__("playback_node")

        self.base_pub = self.create_publisher(
            Float64,
            "/base_to_forearm_joint/cmd_pos",
            10
        )

        self.hand_pub = self.create_publisher(
            Float64,
            "/forearm_to_hand_joint/cmd_pos",
            10
        )

        self.left_pub = self.create_publisher(
            Float64,
            "/left_finger_joint/cmd_pos",
            10
        )

        self.right_pub = self.create_publisher(
            Float64,
            "/right_finger_joint/cmd_pos",
            10
        )

        time.sleep(1.0)

        self.play_demo()

    def publish_value(self, publisher, value):
        msg = Float64()
        msg.data = float(value)
        publisher.publish(msg)

    def play_demo(self):
        self.get_logger().info("Playback started...")

        file = open("/home/jaimiish/ros2_ws/src/my_robot_bringup/dataset/demo.csv", "r")
        reader = csv.reader(file)

        next(reader)  # skip header

        previous_time = 0.0

        for row in reader:
            current_time = float(row[0])
            wait_time = current_time - previous_time

            if wait_time > 0:
                time.sleep(wait_time * 0.1)

            self.publish_value(self.base_pub, row[1])
            self.publish_value(self.hand_pub, row[2])
            self.publish_value(self.left_pub, row[3])
            self.publish_value(self.right_pub, row[4])

            previous_time = current_time

        file.close()

        self.get_logger().info("Playback finished.")


def main(args=None):
    rclpy.init(args=args)

    node = PlaybackNode()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()