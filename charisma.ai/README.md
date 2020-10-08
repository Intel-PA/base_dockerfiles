# Remove all dangling images

    docker rmi -f $(docker images -q --filter "dangling=true")

# Build dockerfile
    
    docker build --rm -t <-insert Image Name-> . 
    
# Start container with volume
    
     docker run --gpus all -ti --name <-Container Name-> -p 8888:8888 --rm -v /home/$USER:/home/ -e type=<-lab or notebook-> <-insert Image Name-> 
    
# Enter existing container
    
    docker stop <-Container Name->
    docker start <-Container Name->
    docker exec -it  myfirst bash

# start jupyter notebook
    
    jupyter notebook --notebook-dir=../ --ip 0.0.0.0 --no-browser --allow-root
    jupyter lab --ip 0.0.0.0 --no-browser --allow-root