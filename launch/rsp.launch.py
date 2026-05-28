import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Lấy tham số thời gian mô phỏng
    su_dung_thoi_gian_mo_phong = LaunchConfiguration('use_sim_time')
    
    # Xử lý file Xacro thành XML
    pkg_path = os.path.join(get_package_share_directory('xetuhanh1'))
    tep_xacro = os.path.join(pkg_path, 'description', 'robot.urdf.xacro')
    cau_hinh_mo_ta_robot = xacro.process_file(tep_xacro).toxml()
    
    # Cấu hình node Robot State Publisher
    tham_so = {
        'robot_description': cau_hinh_mo_ta_robot,  
        'use_sim_time': su_dung_thoi_gian_mo_phong
    }
    
    node_cong_bo_trang_thai_robot = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[tham_so]
    )

    # TRẢ VỀ CHÍNH XÁC NODE NÀY
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Sử dụng thời gian mô phỏng nếu là true'),
        node_cong_bo_trang_thai_robot
    ])
