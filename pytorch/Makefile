ports 			= -p 8888:8888
volume_dir 		= /home/kari/:/home
dataset_dir		= /media/kari/DATA1/Datasets/:/home/Datasets
container_name	= pytorch-gpu
Docker_name		= knoriy/pytorch-gpu


run:
	@docker run -it --rm --gpus=all $(ports) -e type=lab -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name)


bash:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(dataset_dir) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash


build:
	@docker-compose build
