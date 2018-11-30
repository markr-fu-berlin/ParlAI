#! /usr/bin/env bash



if [ ! "$(docker ps -q -f name=parlai)" ]; then
    docker run -d --name parlai --mount type=bind,source="$(pwd)"/data,target=/app/data parlai_docker \
    --mount type=bind,source="$(pwd)"/parlai/tasks/hotpotqaintegrationtest,target=/app/parlai/tasks/hotpotqaintegrationtest parlai_docker
fi

docker exec -it parlai bash
