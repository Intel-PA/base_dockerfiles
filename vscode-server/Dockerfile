FROM codercom/code-server

RUN ["/bin/bash", "-c", "apt update"]
RUN ["/bin/bash", "-c", "apt install -y python3 \
                    python3-pip"]

## START - Python packages
ADD requirements.txt .

RUN pip3 install -r requirements.txt
## END - Python packages
