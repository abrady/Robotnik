* <https://www.udemy.com/course/ros2-for-beginners>
* set up nvidia support on the machine
  * podman machine ssh

  * ```

sudo curl -s -L <https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo> \
     -o /etc/yum.repos.d/nvidia-container-toolkit.repo
sudo dnf install -y nvidia-container-toolkit            # pulls nvidia-ctk and hook

```
* podman build -t myros:jazzy-gpu .
* make sure to run this from the directory you want to mount:
    * podman run --rm -it --device nvidia.com/gpu=all --security-opt label=disable --network host --ipc host -e DISPLAY=:0 -v /mnt/wslg/.X11-unix:/tmp/.X11-unix -v /mnt/wslg:/mnt/wslg -v ./ws:/ws osrf/ros:jazzy-desktop bash


* inside container
    * source /opt/ros/jazzy/setup.bash
    * rviz2 &
    * 
