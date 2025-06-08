###############################################################################
# 0. Base image (very stable)
###############################################################################
FROM osrf/ros:jazzy-desktop-full AS ros-base

###############################################################################
# 1. OS setup  ─ rarely changes
#    * switch root → bash
#    * generic build utilities
###############################################################################
FROM ros-base AS os-prereqs

RUN usermod --shell /bin/bash root

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    curl ca-certificates build-essential neovim && \
    rm -rf /var/lib/apt/lists/*

###############################################################################
# 2. Rust toolchain  ─ bumps only when you change RUSTUP_INIT_ARGS
###############################################################################
FROM os-prereqs AS rust

ENV CARGO_HOME=/root/.cargo \
    RUSTUP_INIT_ARGS="-y --default-toolchain stable --profile minimal"

RUN curl -sSf https://sh.rustup.rs | \
    sh -s -- ${RUSTUP_INIT_ARGS} && \
    echo 'export PATH=$CARGO_HOME/bin:$PATH' > /etc/profile.d/cargo.sh

ENV PATH="/root/.cargo/bin:${PATH}"

###############################################################################
# 3. Extra CLI tools built with Cargo  ─ changes when you `cargo install …`
###############################################################################
FROM rust AS tools

RUN cargo install --locked zellij

###############################################################################
# 4. Final image  ─ leave build tools behind (optional but small & clean)
###############################################################################
FROM ros-base

# copy root’s updated shell entry
COPY --from=os-prereqs /etc/passwd /etc/passwd

# copy cargo + zellij binaries only
COPY --from=rust  /root/.cargo  /root/.cargo
COPY --from=tools /root/.cargo/bin/zellij /root/.cargo/bin/

ENV PATH="/root/.cargo/bin:${PATH}"

###############################################################################
# 5. Shell conveniences & working dir (frequent tweaks live here)
###############################################################################
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc && \
    echo "cd /ws" >> /root/.bashrc


RUN zellij setup --generate-auto-start bash >> ~/.bashrc
RUN mkdir -p /root/.config/zellij && \
    zellij setup --dump-config > /root/.config/zellij/config.kdl

RUN echo "copy_on_select true" >> /root/.config/zellij/config.kdl
#echo "copy_on_select_mode clipboard" >> /root/.config/zellij/config.kdl
RUN echo "default_shell \"/usr/bin/bash\"" >> /root/.config/zellij/config.kdl
RUN echo "" >> /root/.config/zellij/config.kdl

WORKDIR /ws


# default to bash to make life easy when you `podman run -it`
CMD ["/bin/bash"]
