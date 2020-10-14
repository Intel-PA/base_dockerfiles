
user 					= 1000:0
ports 					= -p 8888:8888 -p 6006:6006
volume_dir 				= /home/kari:/home
dataset_dir 			= /media/kari/DATA2/Datasets/:/home/Datasets
Docker_name				= knoriy/tensorflow-gpu
container_name 			= tensorflow-gpu
files_to_remove 		= __pycache__ .ipynb_checkpoints saved_images/ logs/
other_files_to_remove 	= cache/ model/


build:
	@docker-compose build 

notebook:
	@docker run -it --rm --gpus=all $(ports) -e type=notebook -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name)

lab:
	@docker run -it --rm --gpus=all $(ports) -e type=lab -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name)

bash:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash

bashDisplay:
	@docker run -it --rm --gpus=all $(ports) --net=host --env="DISPLAY" --rm -v /home/.Xauthority:/root/.Xauthority:rw -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash

predict:
	@python predict.py -i ./content.jpg

clean:
	@rm -rf $(files_to_remove) || sudo rm -rf $(files_to_remove)
	@echo "Cleaned"

cleanall:
	@sudo rm -rf $(files_to_remove) $(other_files_to_remove)
	@echo "Cleaned"