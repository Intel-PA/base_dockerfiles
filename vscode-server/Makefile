# set user
user 					= 1000:0

# docker image and container details
Docker_name				= $(shell whoami)/vscode-server
container_name 			= vscode-server

# forwards ports
ports 					= -p 19875:8080

# set volume directory
volume_dir 				= $(shell pwd):/home/coder/project
dataset_dir 			= /media/$(shell pwd)/DATA/Datasets/:/Datasets



build:
	@docker build . -t $(Docker_name)

run:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) -u "$(id -u):$(id -g)" --name $(container_name) $(Docker_name) || docker exec -it $(container_name) bash


# 	docker run -it -p 127.0.0.1:8080:8080 \
#   -v "$PWD:/home/coder/project" \
#   -u "$(id -u):$(id -g)" \
#   codercom/code-server:latest