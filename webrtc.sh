#!/bin/bash

echo 'webrtc'

gnome-terminal --tab --title="webrtc" --command="bash -c 'source /opt/ros/humble/setup.bash;source /home/khadas/workspace/install/setup.bash;source /home/khadas/ros2_ws/install/setup.bash;source /home/khadas/server/run.sh; $SHELL'"


