#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from more_interfaces.msg import AddressBook

class CmdVelPublisher(Node):
    def __init__(self):
        super().__init__('custom_publisher')
        self.motor_speed_publisher = self.create_publisher(AddressBook, 'AGV/motor_speeds', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        address_book_msg = AddressBook()
        address_book_msg.sag_teker_hiz = 222
        address_book_msg.sol_teker_hiz = 123
        address_book_msg.linear_actuator = True

        self.motor_speed_publisher.publish(address_book_msg)
        self.get_logger().info(f'Received sag_teker_hiz: {address_book_msg.sag_teker_hiz}')
        self.get_logger().info(f'Received sol_teker_hiz: {address_book_msg.sol_teker_hiz}')
        self.get_logger().info(f'Received linear_aktuator: {address_book_msg.linear_actuator}')


def main(args=None):
    rclpy.init(args=args)
    cmd_vel_publisher = CmdVelPublisher()
    rclpy.spin(cmd_vel_publisher)
    cmd_vel_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()