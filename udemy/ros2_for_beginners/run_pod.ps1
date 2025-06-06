# podman run --rm -it --read-only -v ./ros_logs:/root/.ros --device nvidia.com/gpu=all --security-opt label=disable --network host --ipc host -e DISPLAY=:0 -v /mnt/wslg/.X11-unix:/tmp/.X11-unix -v /mnt/wslg:/mnt/wslg -v ./ws:/ws osrf/ros:jazzy-desktop bash
#     --userns keep-id `
# --read-only `

podman run --rm -it `
    --device nvidia.com/gpu=all `
    --network host `
    --ipc host `
    --tmpfs /root `
    -e DISPLAY=:0 `
    -v /mnt/wslg/.X11-unix:/tmp/.X11-unix `
    -v /mnt/wslg:/mnt/wslg:ro `
    -v ./ws:/ws `
    -v ./ros_logs:/root/.ros `
    osrf/ros:jazzy-desktop bash
