
# set user
user 					= 1000:0

# docker image and container details
Docker_name				= $(shell whoami)/openai_gym
container_name 			= openai_gym

# forwards ports
ports 					= -p 8888:8888 -p 6006:6006

# set volume directory

volume_dir 				= /home/$(shell whoami)/Documents/dockerfiles/openAI_Gym:/home
dataset_dir 			= /media/$(shell whoami)/DATA/Datasets/:/home/Datasets

#Other
files_to_remove 		= __pycache__ .ipynb_checkpoints saved_images/ logs/
other_files_to_remove 	= cache/ model/


build:
	@docker build . -t $(Docker_name)

notebook:
	@docker run -it --rm --gpus=all $(ports) -e type=notebook -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name)

lab:
	@docker run -it --rm --gpus=all $(ports) -e type=lab -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) || jupyter ${type} --ip 0.0.0.0 --no-browser --allow-root

bash:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash

bashDisplay:
	@docker run -it --rm --gpus=all $(ports) --net=host --env="DISPLAY" --rm -v /home/.Xauthority:/root/.Xauthority:rw -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash


clean:
	@rm -rf $(files_to_remove) || sudo rm -rf $(files_to_remove)
	@echo "Cleaned"

cleanall:
	@sudo rm -rf $(files_to_remove) $(other_files_to_remove)
	@echo "Cleaned"