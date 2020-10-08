FROM ubuntu:latest

LABEL MAINTAINER="Kari Noriy, knoriy@bournemouth.ac.uk"


RUN apt-get update

RUN apt-get update && apt-get install -y \
	alsa-utils \
	libasound2 \
	libasound2-plugins \
	pulseaudio \
	pulseaudio-utils \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

USER daemon
CMD [ "bash" ]