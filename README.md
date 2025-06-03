# Robotnik
* doing stanford's https://cs224r.stanford.edu/ in here to start
* using podman to make containers for it (run this in the hw1 directory)
    * I had to install the nvidia container toolkit into the pod machine itself: https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
    * podman build -t cs224r-hw1 .
    * podman run --rm -it -v .:/workspace:Z cs224r-hw1
    * With GPU Support:
```
podman run --rm -it --device nvidia.com/gpu=all -e MUJOCO_GL=egl -e PYOPENGL_PLATFORM=egl -v ${PWD}:/workspace --workdir /workspace cs224r-hw1
```
    
```
cd /workplace
python -m cs224r.scripts.run_hw1 \
       --expert_policy_file cs224r/policies/experts/Ant.pkl \
       --env_name Ant-v4 --exp_name bc_ant --n_iter 1 \
       --expert_data cs224r/expert_data/expert_data_Ant-v4.pkl \
       --video_log_freq -1
```

