ARG UBUNTU_NAME=noble
FROM ubuntu:${UBUNTU_NAME}
ARG UBUNTU_NAME
ARG UBUNTU_RELEASE=24.04
ARG UBUNTU_RELEASE_SIMPLE=2404
ARG CUDA_VERSION=12-6
ARG OPENJDK_VERSION=21
LABEL org.opencontainers.authors="KOLEJKA <kolejka@matinf.uj.edu.pl>"
ENTRYPOINT ["/bin/bash"]
WORKDIR /root

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV DEBIAN_PRIORITY=critical
ENV DEBIAN_FRONTEND=noninteractive

RUN rm -f /etc/apt/sources.list.d/*
RUN echo "deb     http://archive.ubuntu.com/ubuntu/ ${UBUNTU_NAME}           main restricted universe multiverse" >  /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu/ ${UBUNTU_NAME}-updates   main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu/ ${UBUNTU_NAME}-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb     http://security.ubuntu.com/ubuntu ${UBUNTU_NAME}-security  main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get -f -y install \
        apt-transport-https \
        apt-utils \
        curl \
        locales \
        software-properties-common \
    && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    true

RUN apt-get -y dist-upgrade

RUN apt-get -f -y install \
        ubuntu-minimal \
        ubuntu-server \
    && \
    true

RUN apt-get --no-install-recommends -f -y install \
        cmake \
        coinor-libclp-dev \
        fp-compiler \
        g++ \
        gcc \
        make \
        openjdk-${OPENJDK_VERSION}-jdk \
        p7zip-full \
        p7zip-rar \
        pkg-config \
        python3 \
        python3-dev \
        python3-numpy \
        python3-venv \
        rsync \
        zip \
    && \
    true

RUN update-java-alternatives -s java-1.${OPENJDK_VERSION}.0-openjdk-amd64

RUN curl --silent --show-error --fail --location --output /tmp/cuda.deb "https://developer.download.nvidia.com/compute/cuda/repos/ubuntu${UBUNTU_RELEASE_SIMPLE}/x86_64/cuda-keyring_1.1-1_all.deb" && \
    dpkg -i /tmp/cuda.deb && \
    rm -f /tmp/cuda.deb && \
    apt-get update && \
    apt-get -f -y install \
        cuda-command-line-tools-${CUDA_VERSION} \
        cuda-libraries-dev-${CUDA_VERSION} \
        cuda-nsight-${CUDA_VERSION} \
        cuda-nsight-compute-${CUDA_VERSION} \
        cuda-nvcc-${CUDA_VERSION} \
    && \
    true

RUN apt-get -y autoremove
