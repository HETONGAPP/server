#!/bin/bash

#sudo systemctl start get_ip.service  
#ttyd -p 8086 --interface <ip_address> bash

#ros2 run webrtc_ros webrtc_ros_server_node
tmux new-session -s Server -d 'ros2 run webrtc_ros webrtc_ros_server_node' &
#ttyd -p 8085 -i 192.168.2.156 -R tmux attach-session -t Server &
ttyd -p 8085 -i 0.0.0.0 -R tmux attach-session -t Server &

tmux new-session -s rosbridge_Server -d 'ros2 launch rosbridge_server rosbridge_websocket_launch.xml & ros2 run pointcloud_server web_start' &

ttyd -p 8086 -i 0.0.0.0 -R tmux attach-session -t rosbridge_Server &

ros2 run iveroslam_ros2 ivero_slam &

#ttyd -p 8086 -i 192.168.2.156 -R tmux attach-session -t rosbridge_Server &
#TODO: change, ttyd -p 8086 -i 10.42.0.99 -R tmux attach-session -t rosbridge_Server &
