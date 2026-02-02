from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='calcul_package',
            executable='calc_node',
            name='calc_node',
            output='screen',
        ),
        Node(
            package='calcul_package',
            executable='output_node',
            name='output_node',
            output='screen',
        ),
    ])
