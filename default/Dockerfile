FROM ubuntu:20.04

RUN apt update

## START - Creating user
RUN apt-get -y install sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
## END - Creating user

## START - Load .bashrc
ADD ./.bashrc .
RUN "/bin/bash" "-c" "source .bashrc"
## End - Load .bashrc


RUN apt install -y  python3
RUN apt install -y  python3-pip

## START - Python packages
ADD requirements.txt .
RUN pip3 install -r requirements.txt
## END - Python packages


USER docker
WORKDIR /home/docker

CMD [ "bash" ]