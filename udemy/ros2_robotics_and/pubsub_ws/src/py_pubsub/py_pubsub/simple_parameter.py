import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult

class SimpleParameterNode(Node):
    def __init__(self):
        super().__init__('simple_parameter_node')
        self.declare_parameter('my_param', 'default_value')
        self.declare_parameter('my_int_param', 42)
        self.declare_parameter('my_bool_param', True)
        self.get_logger().info(f'Parameter my_param: {self.get_parameter("my_param").get_parameter_value().string_value}')
        self.add_on_set_parameters_callback(self.parameter_callback)
    def parameter_callback(self, params):
        result = SetParametersResult()
        for param in params:
            self.get_logger().info(f'Received parameter change: {param.name} = {param.value}')
            if param.name == 'my_param':
                self.get_logger().info(f'Set my_param to: {param.value}')
                result.successful = True
            elif param.name == 'my_int_param' and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info(f'Set my_int_param to: {param.value}')
                result.successful = True
            elif param.name == 'my_bool_param' and param.type_ == Parameter.Type.BOOL:
                self.get_logger().info(f'Set my_bool_param to: {param.value}')
                result.successful = True
            else:
                self.get_logger().warn(f'Unknown parameter name/type pair for {param.name}: {self.get_parameter_type(param.name)}')
                result.successful = False
        return result


def main():
    rclpy.init()
    node = SimpleParameterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()