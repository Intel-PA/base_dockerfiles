FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel

LABEL MAINTAINER=" Kari Noriy knoriy@bournemouth.ac.uk"

RUN apt-get update

RUN apt-get install -y  git \
                        openssh-server \
                        vim \
                        tree

## START - Jupyter notebook setup
RUN pip install jupyterlab
## END - Jupyter notebook setup

## START - Python packages
ADD requirements.txt .
RUN pip install -r requirements.txt
## END - Python packages

WORKDIR /home

ENV type notebook

CMD ["bash","-c", "jupyter ${type} --ip 0.0.0.0 --no-browser --allow-root"]