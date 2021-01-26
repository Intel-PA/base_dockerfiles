FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel

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

RUN apt-get install -y python-opengl

# START - OpenAI Gym setup from source
RUN apt-get install -y libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev xvfb ffmpeg curl patchelf libglfw3 libglfw3-dev cmake zlib1g zlib1g-dev swig
RUN xvfb-run -s "-screen 0 1400x900x24" bash
RUN pip install git+https://github.com/openai/gym
# End - OpenAI Gym setup from source


## START - Python packages
ADD requirements.txt .
RUN pip3 install -r requirements.txt
## END - Python packages

WORKDIR /home

ENV type lab

CMD ["bash","-c", "jupyter ${type} --ip 0.0.0.0 --no-browser --allow-root"]