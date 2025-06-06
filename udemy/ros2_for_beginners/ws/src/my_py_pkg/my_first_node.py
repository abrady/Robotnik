#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)

    node = Node('my_first_node')
    node.get_logger().info('Hello, ROS 2!')

    # Keep the node running until it is shut down
    rclpy.spin(node)

    #node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
# This is a simple ROS 2 Python node that logs a message when started.
