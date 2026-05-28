import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    package_name='xetuhanh1' 

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )
    
    world_arg = DeclareLaunchArgument(
        'world',
        default_value="empty.world",
        description='World to load'
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    )

    # Nâng z lên 0.2m để xe rơi xuống từ từ, tránh nổ vật lý
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'xetuhanh1',
                                   '-z', '0.2'],
                        output='screen')

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["diff_cont"],
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_broad"],
    )

    twist_mux_config = os.path.join(get_package_share_directory(package_name),
                                         'config', 'twist_mux.yaml')
    twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        output='screen',
        # Đã thêm _unstamped vào đuôi
        remappings=[('/cmd_vel_out', '/diff_cont/cmd_vel_unstamped')], 
        parameters=[
            {'use_sim_time': True},
            twist_mux_config])

            
    return LaunchDescription([
        rsp,
        world_arg,
        gazebo,
        spawn_entity,
        twist_mux,
        # Trì hoãn 5 giây để Gazebo và spawn_entity chạy xong trước
        TimerAction(
            period=5.0,
            actions=[diff_drive_spawner, joint_broad_spawner]
        )
    ])
