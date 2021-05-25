FROM ubuntu:20.04

RUN apt update

RUN apt install -y  python3 \
                    python3-pip

## START - Python packages
ADD requirements.txt .
RUN pip3 install -r requirements.txt
## END - Python packages

WORKDIR /home

CMD [ "bash" ]