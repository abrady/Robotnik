# Containerfile for CS-224R homework 1
FROM python:3.11-slim-bullseye

# ---- system deps ----

    # ---- get curl ----
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
        build-essential git ffmpeg libgl1 libegl1 ca-certificates \
        curl gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
        build-essential git ffmpeg libgl1 libegl1 ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
        libosmesa6-dev libgl1-mesa-dev mesa-utils && \
    rm -rf /var/lib/apt/lists/*

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

# ENV MUJOCO_GL=osmesa        
ENV MUJOCO_GL=egl
# headless rendering
# MUJOCO_GL=egl

# ---- Python deps ----
COPY requirements.txt /tmp/
# silence “running pip as root” warning - it's fine in a container in this scenario
ENV PIP_ROOT_USER_ACTION=ignore   
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# ---- non-root user matches your host UID (nice for volume-mounts) ----
ARG USER_ID=1000
RUN adduser --disabled-password --uid $USER_ID student
USER student
WORKDIR /workspace

CMD ["bash"]
