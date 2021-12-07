# set user
user 					= 1000:0

# docker image and container details
# Docker_name				= $(shell whoami)/mincraftserver
Docker_name				= itzg/minecraft-server:java8
container_name 			= minecraftserver

# forwards ports
ports 					= -p 25565:25565

# set volume directory
volume_dir 				= $(shell pwd)/serverFiles:/data

# Env Variables
# auto_pause = -e ENABLE_AUTOPAUSE=TRUE -e AUTOPAUSE_TIMEOUT_EST=700


run:
	@docker run -d --gpus=all $(ports) -e TYPE=FORGE -e VERSION=1.16.4 -e FORGEVERSION=35.1.4 $(auto_pause) -v $(volume_dir) --name $(container_name) -e EULA=TRUE $(Docker_name)

stop:
	@docker stop $(container_name)

start:
	@docker start $(container_name)

kill:
	@docker rm -f $(container_name)

restart: 
	@docker stop $(container_name)
	@docker start $(container_name)

backup:
	@cp -rf server.properties ops.json usercache.json worlds/ ../backup/

restore_backup:
	@cp -rf backup/* serverFiles/
	@rm -rf serverFiles/world/

