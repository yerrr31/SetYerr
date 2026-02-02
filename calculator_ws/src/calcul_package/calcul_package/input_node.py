import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class InputNode(Node):
    def __init__(self):
        super().__init__('input_node')
        self.pub = self.create_publisher(String, '/calc/input', 10)
        self.timer = self.create_timer(2.0, self.timer_cb)

        self.get_logger().info('InputNode started. Will ask input every 2 seconds.')

    def timer_cb(self):
        try:
            expr = input("Enter expression (e.g., 3 + 5): ").strip()
        except EOFError:
            return

        if not expr:
            return

        msg = String()
        msg.data = expr
        self.pub.publish(msg)
        self.get_logger().info(f'Published: "{expr}"')


def main():
    rclpy.init()
    node = InputNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
