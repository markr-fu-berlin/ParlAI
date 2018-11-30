FROM anibali/pytorch:cuda-9.2

USER root

# TODO set user correctly

RUN apt-get update && apt-get install -y python-pip

COPY ./requirements.txt /app/requirements.txt
RUN sudo pip install -r requirements.txt
COPY . /app


RUN python setup.py develop

ENTRYPOINT ["sh" , "docker-entrypoint.sh"]