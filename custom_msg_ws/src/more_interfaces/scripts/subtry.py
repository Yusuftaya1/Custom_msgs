#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from more_interfaces.msg import AddressBook

class MotorSubscriber(Node):
    def __init__(self):
        super().__init__('_subscriber')

        self.sag_teker_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor_speeds',
            self.motor_callback,
            10)

    def motor_callback(self, msg):
        self.get_logger().info(f'Received sag_teker_hiz: {msg.sag_teker_hiz}')
        self.get_logger().info(f'Received sol_teker_hiz: {msg.sol_teker_hiz}')
        self.get_logger().info(f'Received linear_actuator: {msg.linear_actuator}')

def main(args=None):
    rclpy.init(args=args)
    Motor_subscriber = MotorSubscriber()
    rclpy.spin(Motor_subscriber)
    Motor_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()