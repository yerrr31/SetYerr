import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CalcNode(Node):
    def __init__(self):
        super().__init__('calc_node')
        self.sub = self.create_subscription(
            String,
            '/calc/input',
            self.input_cb,
            10
        )
        self.pub = self.create_publisher(String, '/calc/result', 10)
        self.get_logger().info('CalcNode started.')


    def input_cb(self, msg: String):
        expr = msg.data.strip()

        out = String()
        try:
            # 허용 문자만 검사 (보안 + 파싱 안정화)
            allowed = "0123456789+-*/(). "
            for ch in expr:
                if ch not in allowed:
                    raise ValueError("Only numbers and + - * / ( ) allowed")

            # 수식 전체 계산 (여러 변수/연산 지원)
            result = eval(expr)

            out.data = f"result={result}"
        except Exception as e:
            out.data = f"error: {e}"

        self.pub.publish(out)
        self.get_logger().info(f'Computed from "{expr}" -> "{out.data}"')


def main():
    rclpy.init()
    node = CalcNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
