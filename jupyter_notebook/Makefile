# set user
user 					= 1000:0

# docker image and container details
Docker_name				= $(shell whoami)/jupyter
container_name 			= jupyter

# forwards ports
# ports 					= -p 8888:8888

# set volume directory
volume_dir 				?= $(shell pwd):/workspace
dataset_dir 			= /media/$(shell whoami)/DATA/Datasets/:/Datasets
jupyter_lab_setting 	= /home/$(shell whoami)/Documents/dockerfiles/jupyter/.jupyter:/root/.jupyter


build:
	@docker build . -t $(Docker_name)

run:
	@docker run --rm --gpus=all $(ports) -e type=lab -v $(jupyter_lab_setting) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) || jupyter lab --ip 0.0.0.0 --no-browser --allow-root

bash:
	@docker run -it --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) -v $(modules_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash