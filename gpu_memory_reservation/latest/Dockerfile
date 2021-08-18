FROM nvidia/cuda:11.0-base
MAINTAINER KOLEJKA <kolejka@matinf.uj.edu.pl>
ENTRYPOINT ["/usr/bin/python3", "reserve_gpu_memory.py"]
WORKDIR /app

COPY ./reserve_gpu_memory.py /app/

RUN apt-get update && apt install -y python3 python3-pip
RUN pip3 install -q numba==0.53.1
