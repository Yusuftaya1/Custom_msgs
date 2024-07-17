#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from more_interfaces.msg import AddressBook
from rclpy.executors import MultiThreadedExecutor

class sag_teker_sub(Node):
    def __init__(self):
        super().__init__('sag_teker_subscriber')
        self.sag_teker_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor/sag_teker_hiz',
            self.sag_teker_callback,
            10)
        
    def sag_teker_callback(self, msg):
        self.get_logger().info(f'Received sag_teker_hiz: {msg.sag_teker_hiz}')



class  sol_teker_sub(Node):
    def __init__(self):
        super().__init__('sol_teker_subscriber')
        self.sol_teker_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor/sol_teker_hiz',
            self.sol_teker_callback,
            10)
        
    def sol_teker_callback(self, msg):
        self.get_logger().info(f'Received sol_teker_hiz: {msg.sol_teker_hiz}')



class linear_actuator(Node):
    def __init__(self):
        super().__init__('linear_actuator_subscriber')
        self.linear_actuator_subscription = self.create_subscription(
            AddressBook,
            'AGV/motor/linear_actuator',
            self.linear_actuator_callback,
            10)
        
    def linear_actuator_callback(self, msg):
        self.get_logger().info(f'Received linear_actuator: {msg.linear_actuator}')


def main(args=None):
    rclpy.init(args=args)
    sag=  sag_teker_sub()
    sol = sol_teker_sub()
    actuator = linear_actuator()

    executor = MultiThreadedExecutor()
    executor.add_node(sag)
    executor.add_node(sol)
    executor.add_node(actuator)

    try:
      executor.spin()
    finally:
      executor.shutdown()

    sag.destroy_node()
    sol.destroy_node()
    actuator.destroy_node()

if __name__ == '__main__':
    main()
