# set user
user 			= 1000:0

# docker image and container details
Docker_name		= knoriy/pytorch
container_name	= pytorh

# forwards ports
ports 			= -p 8888:8888

# set volume directory
volume_dir 		= $(shell pwd):/home
dataset_dir		= /media/karinoriy/DATA/Datasets/:/Datasets

build:
	@docker-compose build

run:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name)

lab:
	@docker run -it --rm --gpus=all $(ports) -e type=lab -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name)

bash:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash


