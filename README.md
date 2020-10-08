# Remove all dangling images
    <pre>
    <code>docker rmi -f $(docker images -q --filter "dangling=true")</code>
    </pre>

# Build dockerfile -
    <pre>
    <code>docker build --rm -t <-insert Image Name-> . </code>
    </pre>
# Start container with volume
    <pre>
    <code> docker run --gpus all,capabilities=utility -ti --name <-Container Name-> -p 8888:8888 --rm -v /home/$USER:/home/ -e type=<-lab or notebook-> <-insert Image Name-> </code>
    </pre>
# Enter existing container
    <pre>
    <code>docker stop <-Container Name->
    docker start <-Container Name->
    docker exec -it  myfirst bash</code>
    </pre>

# start jupyter notebook
    <pre>
    <code>jupyter notebook --notebook-dir=../ --ip 0.0.0.0 --no-browser --allow-root
    jupyter lab --ip 0.0.0.0 --no-browser --allow-root<code>
    </pre>