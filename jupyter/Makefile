# set user
user 					= 1000:0

# docker image and container details
Docker_name				= knoriy/jupyter
container_name 			= jupyter

# forwards ports
ports 					= -p 8888:8888

# set volume directory
volume_dir 				= $(shell pwd):/home
dataset_dir 			= /media/knoriy/DATA/Datasets/:/Datasets
jupyter_lab_setting = /home/knoriy/Documents/dockerfiles/jupyter/.jupyter:/root/.jupyter


build:
	@docker build . -t $(Docker_name)

lab:
	@docker run --rm --gpus=all $(ports) -v $(jupyter_lab_setting) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) 