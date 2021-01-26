# set user
user 					= 1000:0

# docker image and container details
Docker_name				= knoriy/pythontestenv
container_name 			= pythontestenv

# forwards ports
ports 					= -p 8888:8888 -p 6006:6006

# set volume directory
volume_dir 				= $(shell pwd):/home
dataset_dir 			= /media/karinoriy/DATA/Datasets/:/Datasets
usb						= /dev/bus/usb/:/dev/bus/usb/



build:
	# Build the image using the the
	@docker-compose build

run:
	@docker run -it --rm --gpus=all $(ports) -v $(volume_dir) -v $(usb) --name $(container_name) $(Docker_name) bash || docker exec -it $(container_name) bash