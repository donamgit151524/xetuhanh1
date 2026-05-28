import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Tên gói ROS chứa file cấu hình và launch
    ten_goi_ros = 'xetuhanh1'

    # Tham số dùng để bật chế độ mô phỏng hoặc thời gian thực
    su_dung_thoi_gian_mo_phong = LaunchConfiguration('use_sim_time')

    # File cấu hình joystick (danh sách phím, nhạy, nút)
    tep_tham_so_joy = os.path.join(
        get_package_share_directory(ten_goi_ros),
        'config',
        'dieu_khien_joystick.yaml'
    )

    node_joy = Node(
        package='joy',
        executable='joy_node',
        parameters=[{'use_sim_time': su_dung_thoi_gian_mo_phong}, tep_tham_so_joy],
    )

    node_dieu_khien_teleop = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_node',
        parameters=[{'use_sim_time': su_dung_thoi_gian_mo_phong}, tep_tham_so_joy],
        remappings=[('/cmd_vel', '/cmd_vel_joy')],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Sử dụng thời gian mô phỏng nếu true, nếu false dùng thời gian thực.'
        ),
        node_joy,
        node_dieu_khien_teleop,
    ])