from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os, pathlib

def generate_launch_description():
    pkg_share = get_package_share_directory('my_bot_description')
    urdf = os.path.join(pkg_share, 'urdf', 'my_bot.urdf')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='rsp',
            parameters=[{'robot_description': pathlib.Path(urdf).read_text()}],
            output='screen'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='jsp_gui',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            arguments=['-d', os.path.join(pkg_share, 'rviz', 'display.rviz')],
            output='screen'
        )
    ])
