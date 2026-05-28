# Danh sách các tên đã đổi

## Tên file
- `launch/joystick.launch.py` -> `launch/dieu_khien_joystick.launch.py`
- `launch/launch_sim.launch.py` -> `launch/khoi_dong_gazebo.launch.py`
- `launch/rsp.launch.py` -> `launch/cong_bo_trang_thai_robot.launch.py`
- `config/joystick.yaml` -> `config/dieu_khien_joystick.yaml`
- `config/twist_mux.yaml` -> `config/bo_tron_twist.yaml`
- `config/my_controllers.yaml` -> `config/bo_dieu_khien.yaml`
- `config/xem_khoi_robot.rviz` -> `config/xem_robot.rviz`
- `config/drive_bot.rviz` -> `config/xem_bot.rviz`
- `config/empty.yaml` -> `config/rong.yaml`
- `config/gazebo_params.yaml` -> `config/tham_so_gazebo.yaml`

## Tên biến/biến tham số trong launch

### launch/dieu_khien_joystick.launch.py
- `package_name` -> `ten_goi_ros`
- `use_sim_time` -> `su_dung_thoi_gian_mo_phong`
- `joy_params` -> `tep_tham_so_joy`
- `joy_node` -> `node_joy`
- `teleop_node` -> `node_dieu_khien_teleop`

### launch/khoi_dong_gazebo.launch.py
- `package_name` -> `ten_goi_ros`
- `rsp` -> `bao_gom_rsp`
- `world_arg` -> `tham_so_the_gioi`
- `gazebo` -> `khoi_dong_gazebo`
- `spawn_entity` -> `node_spawning_thuc_the`
- `diff_drive_spawner` -> `node_spawner_diff_cont`
- `joint_broad_spawner` -> `node_spawner_joint_broad`
- `twist_mux_config` -> `tep_cau_hinh_twist_mux`
- `twist_mux` -> `node_twist_mux`

### launch/cong_bo_trang_thai_robot.launch.py
- `pkg_path` -> `thu_muc_goi`
- `cau_hinh_mo_ta_robot` -> `mo_ta_robot_xml`
- `tham_so` -> `tham_so_node`

## Tham chiếu cấu hình
- `description/ros2_control.xacro`: `$(find xetuhanh1)/config/my_controllers.yaml` -> `$(find xetuhanh1)/config/bo_dieu_khien.yaml`
