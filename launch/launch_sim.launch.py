import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():

    # 1. Khai báo các biến tên gói và tên robot để dễ dàng thay đổi sau này
    package_name = 'xetuhanh1'
    robot_name = 'Sieu_xe_AGV'

    # Khởi tạo Launch Configuration cho môi trường (world)
    world = LaunchConfiguration('world')

    # 2. Định nghĩa tham số world (giống tư duy của tác giả)
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='', # Để trống mặc định sẽ tải world trống của Gazebo
        description='Đường dẫn đến file .world của Gazebo'
    )

    # Chạy file rsp.launch.py từ package của bạn
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Khởi chạy Gazebo Classic (tối ưu: truyền thêm tham số world)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
        )]),
        launch_arguments={'world': world}.items()
    )

    # 3. Khởi tạo robot (tối ưu: thêm toạ độ -z 0.1)
    spawn_entity = Node(
        package='gazebo_ros', 
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', robot_name,
            '-z', '0.1'  # Thả robot cách mặt đất 0.1m để tránh kẹt bánh xe
        ],
        output='screen'
    )

    # Chạy tất cả các tiến trình
    return LaunchDescription([
        world_arg,
        rsp,
        gazebo,
        spawn_entity,
    ])