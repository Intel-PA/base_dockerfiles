FROM ubuntu:18.04

RUN apt update && apt upgrade -y

RUN apt install -y  python3 \
                    python3-pip

## START - Jupyter notebook setup
RUN pip3 install jupyterlab
## END - Jupyter notebook setup

## START - Python packages
ADD requirements.txt .
RUN pip3 install -r requirements.txt
## END - Python packages

WORKDIR /home

CMD [ "bash", "-c", "jupyter lab --ip 0.0.0.0 --no-browser --allow-root" ]