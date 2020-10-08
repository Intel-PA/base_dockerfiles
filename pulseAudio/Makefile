
user 					= 1000:0
Docker_name				= knoriy/pulseaudio
container_name 			= pulseaudio


build:
	@docker-compose build 

run:
	@docker run -u $(id -u):$(id -g) -it --rm --name $(container_name) $(Docker_name)