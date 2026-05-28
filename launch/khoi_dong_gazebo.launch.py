import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    ten_goi_ros = 'xetuhanh1'

    # Include launch để khởi tạo robot_state_publisher với mô phỏng thời gian
    bao_gom_rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory(ten_goi_ros),
                'launch',
                'cong_bo_trang_thai_robot.launch.py'
            )
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    tham_so_the_gioi = DeclareLaunchArgument(
        'world',
        default_value='empty.world',
        description='Tên world Gazebo cần tải.'
    )

    khoi_dong_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ]),
    )

    node_spawning_thuc_the = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'xetuhanh1',
            '-z', '0.2'
        ],
        output='screen'
    )

    node_spawner_diff_cont = Node(
        package='controller_manager',
        executable='spawner.py',
        arguments=['diff_cont'],
    )

    node_spawner_joint_broad = Node(
        package='controller_manager',
        executable='spawner.py',
        arguments=['joint_broad'],
    )

    tep_cau_hinh_twist_mux = os.path.join(
        get_package_share_directory(ten_goi_ros),
        'config',
        'bo_tron_twist.yaml'
    )

    node_twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        output='screen',
        remappings=[('/cmd_vel_out', '/diff_cont/cmd_vel_unstamped')],
        parameters=[
            {'use_sim_time': True},
            tep_cau_hinh_twist_mux
        ]
    )

    return LaunchDescription([
        bao_gom_rsp,
        tham_so_the_gioi,
        khoi_dong_gazebo,
        node_spawning_thuc_the,
        node_twist_mux,
        TimerAction(
            period=10.0,
            actions=[node_spawner_diff_cont, node_spawner_joint_broad]
        )
    ])
