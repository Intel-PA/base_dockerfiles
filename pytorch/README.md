# Pytorch

This is an image build for pytorch with GPU support.

On start, the container will start in jupyter notebook, but can be changed by simply changing the docker run enviroment variable 'type' to 'lab' start the images using jupyter lab.

## Remove all dangling images

    docker rmi -f $(docker images -q --filter "dangling=true")

## Build dockerfile

    docker build --rm -t <-insert Image Name-> . 

## Start container with volume

     docker run --gpus all,capabilities=utility -ti --name <-Container Name-> -p 8888:8888 --rm -v /home/$USER:/home/ -e type=<-lab or notebook-> <-insert Image Name-> 

## Enter existing container

    docker stop <-Container Name->
    docker start <-Container Name->
    docker exec -it  myfirst bash

## Start jupyter notebook

    jupyter notebook --notebook-dir=../ --ip 0.0.0.0 --no-browser --allow-root
    jupyter lab --ip 0.0.0.0 --no-browser --allow-root