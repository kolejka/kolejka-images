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
        openjdk-16-jdk \
        p7zip-full \
        p7zip-rar \
        python3 \
	    python3-dev \
        rsync \
        zip \
    && \
    true

RUN update-java-alternatives -s java-1.16.0-openjdk-amd64

RUN apt-add-repository ppa:kolejka/kolejka && \
    apt-get -f -y install \
        python3-kolejkaobserver \
    && \
    true

RUN apt-get --no-install-recommends -f -y install \
	    ant \
	    ant-contrib \
	    bison \
	    cabal-install \
	    clang \
	    clang-format \
	    clang-tidy \
	    clang-tools \
	    coq \
	    erlang \
        g++-multilib \
        gcc-multilib \
	    ghc \
        git \
	    golang-go \
	    gprolog \
	    libcgal-dev \
	    libgmp-dev \
	    libglpk-dev \
	    mlton \
	    mono-complete \
	    nasm \
	    postgresql \
	    sqlite3 \
	    valgrind \
    && \
    true

RUN apt-get -y autoremove
