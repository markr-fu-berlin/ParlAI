#! /usr/bin/env bash

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    echo "Usage: docker_build.sh or bash docker_build.sh"
    echo "Builds a docker image for parlAI"
fi


if [ "$(docker ps -q -f name=parlai)" ]; then
    echo "Docker is currently running, do you want to override with a new one?(y/n)"
    read answer

    if [ "$answer" != "${answer#[Yy]}" ] ;then
        docker stop parlai
        docker rm parlai
        echo docker removed
    else
        echo exiting
        exit
    fi
fi

docker pull anibali/pytorch:cuda-9.2

if [ "$1" != "sample" ]; then
    docker build  -t 'parlai_docker' .
    echo "use docker_exec.sh to run and enter docker-container"
fi