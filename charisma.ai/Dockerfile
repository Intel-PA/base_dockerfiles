FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

LABEL MAINTAINER="Kari Noriy, knoriy@bournemouth.ac.uk"

WORKDIR /home/

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y git \
                                         openssh-server \
                                         vim \
                                         tree 

RUN pip3 install ipykernel --upgrade \
                       opencv-python \
                       Pillow \
                       jupyterthemes \
                       flask

COPY /home/knoriy/.bashrc /home/
RUN Source .bashrc
                       
VOLUME [ "/home/knoriy/" ]

CMD ["bash", "-c", "source /etc/bash.bashrc && jt -t chesterish && jupyter notebook --notebook-dir=../ --ip 0.0.0.0 --no-browser --allow-root"]