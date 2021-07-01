#!/bin/bash

docker pull gcr.io/shelfauditdec19/my_darknet:latest 

echo "##############################################"
echo "              Done Pulling                    "
echo "##############################################"

# enter more commands ...

# docker run --name doralon_all -ti --rm gcr.io/shelfauditdec19/my_darknet doralon-all doralon 5000
docker run --name doralon_all -t --rm gcr.io/shelfauditdec19/my_darknet doralon-all doralon 5000 # for jupyter notebooks
echo "##############################################"
echo "              Done Training                    "
echo "##############################################"



exit 0 