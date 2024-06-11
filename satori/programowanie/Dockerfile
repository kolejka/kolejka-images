ARG UBUNTU_NAME=focal
FROM ubuntu:${UBUNTU_NAME}
ARG UBUNTU_NAME
ARG UBUNTU_RELEASE=20.04
ARG UBUNTU_RELEASE_SIMPLE=2004
ARG GRADLE_VERSION=8.4
ARG MAVEN_VERSION=3.9.5
ARG OPENJDK_VERSION=17
MAINTAINER KOLEJKA <kolejka@matinf.uj.edu.pl>
ENTRYPOINT ["/bin/bash"]
WORKDIR /root

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_PRIORITY critical
ENV DEBIAN_FRONTEND noninteractive

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
        fp-compiler \
        g++ \
        gcc \
        coinor-libclp-dev \
        make \
        openjdk-${OPENJDK_VERSION}-jdk \
        p7zip-full \
        p7zip-rar \
        python3 \
        python3-dev \
        python3-numpy \
        python3-venv \
        rsync \
        zip \
    && \
    true

RUN update-java-alternatives -s java-1.${OPENJDK_VERSION}.0-openjdk-amd64

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

COPY pom.xml /tmp/
RUN sed -e "s|\(</settings>\)|<localRepository>/opt/maven/repository</localRepository>\1|" -i /opt/maven/conf/settings.xml && \
    mvn -f /tmp/pom.xml dependency:go-offline && \
    rm /tmp/pom.xml
