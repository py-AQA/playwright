FROM ubuntu:latest
LABEL authors="konst"

#ENTRYPOINT ["top", "-b"]

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    nano\
    python3\
    pip\
    git\
    net-tools
#git init
#git branch -m main
#git config --global user.name "Grom-Zadira85"
#git config --global user.email Trall18111985@gmail.com
#git config --global core.editor "nano -w"
#git config --global user.password GromZadira1985

WORKDIR /root

ENTRYPOINT ["/bin/bash"]