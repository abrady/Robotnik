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

## making a package

`ros2 pkg create my_py_pkg --build-type ament_python --dependencies `rclypy`
* can also specify dependencies: --dependencies

`colcon build`
* builds it. you can run this in /ws and it'll recursively find package.xmls to build

`colcon build --packages-select my_py_pkg`
* this will build just my_py_pkg if you run it in /ws

`ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp`

## Documentation
* workspace - `/ws` : the workspace where your packages live
* package - `/ws/py_pubsub` : a 'package' that contains node definitions
* node - `talker` or `listener`, a running instance

## Cheat Sheet
* `source install/setup.bash` : set up ros2 with your packages in the workspace
* `colcon build --symlink-install` : builds the projects
* ros2 pkg
  * `ros2 pkg list` : shows packages
  * `ros2 pkg executables <package>` : show what you can run
* `ros2 run <package> <node>`
* params:
  * ros2 param list
  * ros2 param set /node name val
* urdf files
  * link: root of a transform effectively.
  * joint : joins two links

## Making a Damned Robot
* new ws: robot_ws
* make a urdf file
* make a launch/display.launch.py file
