# Hướng dẫn sử dụng gói xetuhanh1

1. Mở terminal và chạy môi trường ROS2.
2. Vào workspace chứa gói `xetuhanh1`:
   ```bash
   cd /home/mayao3/da_ws/src/xetuhanh1
   ```
3. Nguồn setup cho ROS2 (ví dụ ROS2 Humble, Foxy hoặc phiên bản bạn đang dùng):
   ```bash
   source /opt/ros/<distro>/setup.bash
   source /home/mayao3/da_ws/install/setup.bash
   ```
4. Khởi động mô phỏng Gazebo:
   ```bash
   ros2 launch xetuhanh1 khoi_dong_gazebo.launch.py
   ```
5. Khởi động joystick để điều khiển robot:
   ```bash
   ros2 launch xetuhanh1 dieu_khien_joystick.launch.py
   ```

## Chú ý cài đặt true/false
- Trong `launch/cong_bo_trang_thai_robot.launch.py`: `use_sim_time` mặc định là `true` để chạy đúng thời gian Gazebo.
- Trong `config/bo_dieu_khien.yaml`: `use_stamped_vel` hiện đang `false`; nếu bật `true` thì bộ điều khiển phải nhận velocity stamped.
- Trong `description/robot.urdf.xacro`: `use_ros2_control=true` sử dụng ROS2 Control. Thay thành `false` để dùng plugin Gazebo khác.

