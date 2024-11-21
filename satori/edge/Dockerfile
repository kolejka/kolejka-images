ARG UBUNTU_NAME=oracular
FROM ubuntu:${UBUNTU_NAME}
ARG UBUNTU_NAME
ARG UBUNTU_RELEASE=24.10
ARG UBUNTU_RELEASE_SIMPLE=2410
ARG DOTNET_VERSION=9
ARG GRADLE_VERSION=8.10.1
ARG MAVEN_VERSION=3.9.9
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

RUN apt-get --no-install-recommends -f -y install \
        ant \
        ant-contrib \
        bison \
        cabal-install \
        cargo \
        clang \
        clang-format \
        clang-tidy \
        clang-tools \
        coq \
        erlang \
        g++ \
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
        python3-numpy \
        sqlite3 \
        valgrind \
    && \
    true

RUN add-apt-repository ppa:dotnet/backports && \
    apt-get -f -y install \
        dotnet${DOTNET_VERSION} \
    && \
    true

RUN curl --silent --show-error --fail --location --output /tmp/gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" && \
    7z x -y -aoa -bb0 -bd -o/opt /tmp/gradle.zip && \
    rm -f /tmp/gradle.zip && \
    mv /opt/gradle-${GRADLE_VERSION} /opt/gradle && \
    ln -s /opt/gradle/bin/gradle /usr/local/bin/gradle && \
    true

RUN curl --silent --show-error --fail --location --output /tmp/maven.zip "https://dlcdn.apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.zip" && \
    7z x -y -aoa -bb0 -bd -o/opt /tmp/maven.zip && \
    rm -f /tmp/maven.zip && \
    mv /opt/apache-maven-${MAVEN_VERSION} /opt/maven && \
    ln -s /opt/maven/bin/mvn /usr/local/bin/mvn && \
    true

RUN apt-get -y autoremove
