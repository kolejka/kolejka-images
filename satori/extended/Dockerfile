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
        fp-compiler \
        g++ \
        gcc \
        make \
        openjdk-17-jdk \
        p7zip-full \
        p7zip-rar \
        python3 \
        python3-dev \
        python3-numpy \
        rsync \
        zip \
    && \
    true

RUN update-java-alternatives -s java-1.17.0-openjdk-amd64

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
        cargo \
        clang \
        clang-format \
        clang-tidy \
        clang-tools \
        coq \
        erlang \
        g++-10 \
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

RUN curl --silent --show-error --fail --location --output /tmp/dotnet.deb "https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb" && \
    dpkg -i /tmp/dotnet.deb && \
    rm -f /tmp/dotnet.deb && \
    apt-get update && \
    apt-get -f -y install \
        dotnet-sdk-7.0 \
    && \
    true

RUN curl --silent --show-error --fail --location --output /tmp/gradle.zip "https://services.gradle.org/distributions/gradle-8.4-bin.zip" && \
    echo "3e1af3ae886920c3ac87f7a91f816c0c7c436f276a6eefdb3da152100fef72ae /tmp/gradle.zip" | sha256sum --quiet --strict --check - && \
    7z x -y -aoa -bb0 -bd -o/opt /tmp/gradle.zip && \
    rm -f /tmp/gradle.zip && \
    mv /opt/gradle-8.4 /opt/gradle && \
    ln -s /opt/gradle/bin/gradle /usr/local/bin/gradle && \
    true

RUN curl --silent --show-error --fail --location --output /tmp/maven.zip "https://dlcdn.apache.org/maven/maven-3/3.9.5/binaries/apache-maven-3.9.5-bin.zip" && \
    echo "ca59380b839c6bea8f464a08bb7873a1cab91007b95876ba9ed8a9a2b03ceac893e661d218ba3d4af3ccf46d26600fc4c59fccabba9d7b2cc4adcd8aecc1df2a /tmp/maven.zip" |sha512sum --quiet --strict --check - && \
    7z x -y -aoa -bb0 -bd -o/opt /tmp/maven.zip && \
    rm -f /tmp/maven.zip && \
    mv /opt/apache-maven-3.9.5 /opt/maven && \
    ln -s /opt/maven/bin/mvn /usr/local/bin/mvn && \
    true

RUN apt-get -y autoremove
