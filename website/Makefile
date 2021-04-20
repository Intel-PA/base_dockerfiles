# set user
user 					= 1000:0

# docker image and container details
Docker_name				= knoriy/website
container_name 			= website

# forwards ports
ports 					= -p 8080:80

# set volume directory
volume_dir 				= $(shell pwd):/home
site	 				= $(shell pwd)/startbootstrap-new-age://usr/share/nginx/html


build:
	@docker build . -t $(Docker_name)

run:
	@docker run -it --rm -d --gpus=all $(ports) -v $(site) --name $(container_name) $(Docker_name) || docker exec -it $(container_name) bash

stop:
	@docker stop $(container_name)