import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class OutputNode(Node):
    def __init__(self):
        super().__init__('output_node')
        self.sub = self.create_subscription(String, '/calc/result', self.result_cb, 10)
        self.get_logger().info('OutputNode started.')

    def result_cb(self, msg: String):
        self.get_logger().info(f'[OUTPUT] {msg.data}')


def main():
    rclpy.init()
    node = OutputNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
