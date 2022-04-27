FROM ubuntu:20.04

RUN apt update

## START - Creating user
RUN apt-get -y install sudo
RUN adduser --disabled-password --gecos '' user
RUN adduser user sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
## END - Creating user


## Insert Here
## 
##
##
## Insert Here



WORKDIR /workspace
RUN chown user:user ../workspace/
USER user

CMD [ "bash" ]