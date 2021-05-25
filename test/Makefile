# set user
user 					= 1000:0

# docker image and container details
Docker_name				= knoriy/test
container_name 			= test

# forwards ports
ports 					= -p 8888:8888 -p 6006:6006

# set volume directory
volume_dir 				= $(shell pwd):/home
dataset_dir 			= /media/knoriy/DATA/Datasets/:/Datasets



build:
	@docker build . -t $(Docker_name)

run:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) || docker exec -it $(container_name) bash