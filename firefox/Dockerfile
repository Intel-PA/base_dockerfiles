FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y libcanberra-gtk-module libcanberra-gtk3-module

RUN apt-get install -y firefox
# RUN apt-get install -y x11-apps

CMD ["bash", "-c", "firefox"]