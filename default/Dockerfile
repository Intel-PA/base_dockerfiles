FROM ubuntu:20.04

RUN apt update

## START - Creating user
RUN apt-get -y install sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
## END - Creating user


## Insert Here
## 
##
##
## Insert Here



USER docker
WORKDIR /home/docker/project

CMD [ "bash" ]