FROM ubuntu:focal
MAINTAINER KOLEJKA <kolejka@matinf.uj.edu.pl>
ENTRYPOINT ["/bin/bash"]
WORKDIR /root

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_PRIORITY critical
ENV DEBIAN_FRONTEND noninteractive

RUN rm -f /etc/apt/sources.list.d/*
RUN echo "deb     http://archive.ubuntu.com/ubuntu/ focal           main restricted universe multiverse" >  /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu/ focal-updates   main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb     http://security.ubuntu.com/ubuntu focal-security  main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get -f -y install \
        apt-transport-https \
        apt-utils \
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
        fp-compiler \
        g++ \
        gcc \
        make \
        openjdk-14-jdk \
        p7zip-full \
        p7zip-rar \
        python3 \
	    python3-dev \
        rsync \
        zip \
    && \
    true

RUN update-java-alternatives -s java-1.14.0-openjdk-amd64

RUN apt-add-repository ppa:kolejka/kolejka && \
    apt-get -f -y install \
        python3-kolejkaobserver \
    && \
    true

RUN echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64 /" >> /etc/apt/sources.list && \
    echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64 /" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key F60F4B3D7FA2AF80 C45B1676A04EA552 && \
    apt-get update && \
    apt-get -f -y install \
        cuda-command-line-tools-11.4 \
        cuda-libraries-dev-11-4 \
        cuda-nsight-11-4 \
        cuda-nsight-compute-11-4 \
        cuda-nvcc-11.4 \
    && \
    true

RUN apt-get -y autoremove