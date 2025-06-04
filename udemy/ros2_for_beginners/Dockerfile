# Containerfile
FROM osrf/ros:jazzy-desktop-full

ENV ROS_WS=/home/rosuser/ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS

RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc
