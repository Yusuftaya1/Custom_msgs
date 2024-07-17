#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, Bool
from more_interfaces.msg import AddressBook

class CmdVelSubscriber(Node):
    def __init__(self):
        super().__init__('cmd_vel_subscriber')

        self.sag_teker_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor/sag_teker_hiz',
            self.sag_teker_callback,
            10)
        
        self.sol_teker_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor/sol_teker_hiz',
            self.sol_teker_callback,
            10)
        
        self.linear_actuator_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor/linear_actuator',
            self.linear_actuator_callback,
            10)

    def sag_teker_callback(self, msg):
        self.get_logger().info(f'Received sag_teker_hiz: {msg.sag_teker_hiz}')

    def sol_teker_callback(self, msg):
        self.get_logger().info(f'Received sol_teker_hiz: {msg.data}')

    def linear_actuator_callback(self, msg):
        self.get_logger().info(f'Received linear_actuator: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    cmd_vel_subscriber = CmdVelSubscriber()
    rclpy.spin(cmd_vel_subscriber)
    cmd_vel_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
