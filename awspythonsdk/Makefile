# set user
user 					= 1000:0

# docker image and container details
Docker_name				= $(shell whoami)/awspythonsdk
container_name 			= awspythonsdk

# forwards ports
# ports 					= -p 8888:8888 -p 6006:6006

# set volume directory
volume_dir 				= $(shell pwd):/home
dataset_dir 			= /media/$(shell whoami)/DATA/:/Datasets
aws_credentials			= /home/$(shell whoami)/.aws/:/root/.aws/

build:
	@docker build . -t $(Docker_name)

run:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) -v $(aws_credentials) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash