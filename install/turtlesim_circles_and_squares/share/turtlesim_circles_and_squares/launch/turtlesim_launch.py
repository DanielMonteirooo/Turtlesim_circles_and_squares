from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle1',
            output='screen',
            namespace='turtle1'
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle2',
            output='screen',
            namespace='turtle2'
        ),
    ])
