FROM ubuntu:focal

RUN mkdir -p /opt/devxdev/

WORKDIR /opt/devxdev/

ADD ./ ./

RUN apt update && apt install python3 python3-pip -y

RUN pip3 install -r requirements.txt

WORKDIR /root/

CMD ["/bin/bash"]
