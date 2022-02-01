FROM ubuntu:20.04

RUN apt update

## START - Creating user
RUN apt-get -y install sudo
RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
## END - Creating user

RUN apt install -y  python3 \
                    python3-pip \ 
                    vim \
                    tree

## START - Jupyter notebook setup
RUN pip3 install jupyterlab
## END - Jupyter notebook setup

## START - Python packages
ADD requirements.txt .
RUN pip3 install -r requirements.txt
## END - Python packages

WORKDIR /home
USER docker

ENV type lab

CMD ["bash","-c", "jupyter ${type} --ip 0.0.0.0 --no-browser --allow-root"]