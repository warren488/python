#!/bin/bash

image="python_flask:latest"
mountingpoint="/project"
name=$(pwd)
name=${name/\//}
name=${name//\//\_}.${image/:/-}
if [[ $(docker ps | grep $name) == *$name ]]
then
    read -p 'container from this folder is already running do you want to attach or restart?(A/r): ' answer
    if [[ $answer == [rR] ]]
    then
        echo 'restarting...'    
        docker kill $name && docker rm $name
        docker run -v $(pwd):$mountingpoint -dit -p 127.0.0.1:5000:5000 --name $name $image   
    else
        echo 'attaching...'    
        docker attach $name
    fi
elif [[ $(docker ps -a | grep $name) == *$name ]]
then 
    read -p 'container from this folder is already created do you want to start and attach or restart(S/r)?' answer
    if [[ $answer == [rR] ]]
    then
        echo 'restarting...'
    
        docker rm $name
        docker run -v $(pwd):$mountingpoint -dit -p 127.0.0.1:5000:5000 --name $name $image
    else
        echo 'starting...'
        docker start $name
    fi
else
    docker run -v $(pwd):$mountingpoint -dit -p 127.0.0.1:5000:5000 --name $name $image
    echo $?
fi

if [ -z "$1" ]
then
    docker exec -dit $name sh -c "echo $mountingpoint"
else
    docker exec $name python $mountingpoint/$1
fi
