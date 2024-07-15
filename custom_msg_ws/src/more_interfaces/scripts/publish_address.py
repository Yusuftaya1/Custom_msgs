#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from more_interfaces.msg import AddressBook

class CmdVelPublisher(Node):
    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.sag_teker_publisher = self.create_publisher(AddressBook, 'AGV/motor/sag_teker_hiz', 10)
        self.sol_teker_publisher = self.create_publisher(AddressBook, 'AGV/motor/sol_teker_hiz', 10)
        self.linear_actuator_publisher = self.create_publisher(AddressBook, 'AGV/motor/linear_actuator', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        twist_msg = Twist()
        twist_msg.linear.x = 550.0
        twist_msg.angular.z = 0.0 
        self.publisher_.publish(twist_msg)
        self.get_logger().info(f'Publishing Twist: linear.x={twist_msg.linear.x}, angular.z={twist_msg.angular.z}')

        address_book_msg = AddressBook()

        sag_msg = address_book_msg.sag_teker_hiz
        sag_msg = 222.0
        sol_msg = address_book_msg.sol_teker_hiz
        sol_msg = 123.0
        aktuator = address_book_msg.linear_actuator
        aktuator = True

        self.sag_teker_publisher.publish(address_book_msg)
        self.get_logger().info(f'Publishing sag_teker_hiz: speed={sag_msg}')
        self.sol_teker_publisher.publish(address_book_msg)
        self.get_logger().info(f'Publishing sol_teker_hiz: speed={sol_msg}')
        self.linear_actuator_publisher.publish(address_book_msg)
        self.get_logger().info(f'Publishing actuator: {aktuator}')


def main(args=None):
    rclpy.init(args=args)
    cmd_vel_publisher = CmdVelPublisher()
    rclpy.spin(cmd_vel_publisher)
    cmd_vel_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
