FROM tensorflow/tensorflow:latest-gpu

LABEL MAINTAINER="Kari Noriy, knoriy@bournemouth.ac.uk"

RUN apt-get update

RUN apt-get install -y  git \
                        openssh-server \
                        vim \
                        tree

RUN apt-get install -y  python3 \
                        python3-pip

RUN pip install --upgrade pip

## START - Jupyter notebook setup
RUN pip3 install jupyter \ 
                 jupyterlab \
                 jupyterthemes \
                 jupyter_contrib_nbextensions 

RUN jupyter contrib nbextension install
RUN jt -t chesterish

RUN jupyter nbextension enable  codefolding/main
RUN jupyter nbextension enable  code_prettify/code_prettify
RUN jupyter nbextension enable  notify/notify
RUN jupyter nbextension enable  python-markdown/main
## END - Jupyter notebook setup

## START - Tensorflow specific packages
RUN pip install tensorflow_hub
RUN pip install tf-nightly
## START - Tensorflow specific packages

## START - Python packages
ADD requirements.txt .
RUN pip3 install -r requirements.txt
## END - Python packages

WORKDIR /home

EXPOSE 8888
EXPOSE 5000

ENV type lab

CMD ["bash", "-c", "jupyter ${type} --ip 0.0.0.0 --no-browser --allow-root"]