import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Tham số xác định dùng thời gian mô phỏng theo ROS2 hay không
    su_dung_thoi_gian_mo_phong = LaunchConfiguration('use_sim_time')

    # Đường dẫn đến file Xacro mô tả robot
    thu_muc_goi = get_package_share_directory('xetuhanh1')
    tep_xacro = os.path.join(thu_muc_goi, 'description', 'robot.urdf.xacro')
    mo_ta_robot_xml = xacro.process_file(tep_xacro).toxml()

    # Node publish thông tin khung xương robot và robot_description cho hệ thống
    tham_so_node = {
        'robot_description': mo_ta_robot_xml,
        'use_sim_time': su_dung_thoi_gian_mo_phong
    }

    node_cong_bo_trang_thai_robot = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[tham_so_node]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Sử dụng thời gian mô phỏng nếu true, nếu false dùng thời gian thực.'
        ),
        node_cong_bo_trang_thai_robot
    ])
