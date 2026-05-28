# xetuhanh1

Đây là gói ROS2 chứa mô tả robot, tệp launch và cấu hình điều khiển cho mô phỏng Gazebo.

## Các file launch chính
- `launch/cong_bo_trang_thai_robot.launch.py`: Publish `robot_description` và node `robot_state_publisher`.
- `launch/khoi_dong_gazebo.launch.py`: Khởi động Gazebo, spawn robot, twist_mux và các controller.
- `launch/dieu_khien_joystick.launch.py`: Khởi động joystick và teleop để điều khiển robot.

## Cấu hình quan trọng
- `config/bo_dieu_khien.yaml`: cấu hình controller ROS2 và bộ điều khiển diff drive.
- `config/bo_tron_twist.yaml`: cấu hình twist_mux để trộn các lệnh `/cmd_vel`.
- `description/robot.urdf.xacro`: định nghĩa robot và lựa chọn plugin điều khiển theo `use_ros2_control`.

## Cách chạy
1. Source workspace ROS2.
2. Khởi chạy mô phỏng:
   ```bash
   ros2 launch xetuhanh1 khoi_dong_gazebo.launch.py
   ```
3. Khởi chạy điều khiển joystick:
   ```bash
   ros2 launch xetuhanh1 dieu_khien_joystick.launch.py
   ```

## Ghi chú true/false
- `use_sim_time`: true nếu chạy Gazebo, false nếu chạy phần cứng thật.
- `use_ros2_control`: true để sử dụng ROS2 Control, false để dùng plugin Gazebo thông thường.
- `use_stamped_vel`: false theo cấu hình hiện tại; bật true nếu muốn dùng velocity stamped.

