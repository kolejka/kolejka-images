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
RUN echo "deb     http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu focal-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu focal-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    true
RUN apt-get update
RUN apt-get -f -y install \
        apt-transport-https \
        locales \
    && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    true

RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections

#RUN echo "y" | unminimize

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    true

RUN apt-get -f -y install \
        apt-utils \
        python3 \
        ubuntu-minimal \
        ubuntu-server \
        software-properties-common \
    && \
    true

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get --no-install-recommends -f -y install \
        a2ps \
        cmake \
        fp-compiler \
        g++ \
        g++-multilib \
        gcc \
        gcc-multilib \
        git \
        iptables \
        libnss-myhostname \
        lzip \
        lzma \
        make \
        net-tools \
        openjdk-11-jdk \
        p7zip-full \
        p7zip-rar \
        python \
        python3 \
        rar \
        time \
        unrar \
        unzip \
        zip \
    && \
    true

RUN update-java-alternatives -s java-1.11.0-openjdk-amd64

RUN apt-add-repository ppa:kolejka/kolejka
RUN apt-get -f -y install \
        python3-kolejkaobserver \
    && \
    true
