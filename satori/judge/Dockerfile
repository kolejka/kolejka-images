FROM ubuntu:bionic
MAINTAINER KOLEJKA <kolejka@matinf.uj.edu.pl>
ENTRYPOINT ["/bin/bash"]
WORKDIR /root

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_PRIORITY critical
ENV DEBIAN_FRONTEND noninteractive

RUN rm -f /etc/apt/sources.list.d/*
RUN echo "deb     http://archive.ubuntu.com/ubuntu bionic main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu bionic-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb     http://archive.ubuntu.com/ubuntu bionic-security main restricted universe multiverse" >> /etc/apt/sources.list && \
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

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    true

RUN apt-get -f -y install \
        apt-utils \
        python \
        ubuntu-minimal \
        ubuntu-server \
        software-properties-common \
    && \
    true

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get --no-install-recommends -f -y install \
        a2ps \
        fp-compiler \
        g++ \
        gcc \
        gcc-multilib \
        g++-multilib \
        iptables \
        libnss-myhostname \
        lzip \
        lzma \
        make \
        net-tools \
        openjdk-8-jdk \
        p7zip-full \
        p7zip-rar \
        python3-setproctitle \
        python3-yaml \
        python-setproctitle \
        python-yaml \
        rar \
        time \
        unrar \
        unzip \
        zip \
    && \
    true

RUN sed -i /usr/lib/jvm/.java-1.8.0-openjdk-amd64.jinfo -e "s/^jdkhl/jdk/"
RUN update-java-alternatives -s java-1.8.0-openjdk-amd64
