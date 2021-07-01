#!/bin/bash

docker pull gcr.io/shelfauditdec19/my_darknet:latest 

echo "##############################################"
echo "              Done Pulling                    "
echo "##############################################"

# enter more commands ...

docker run --rm -it gcr.io/shelfauditdec19/my_darknet doralon_dairy-categories doralon_dairy 100 --use_new_mapping --email eldad@arpalus.com

echo "##############################################"
echo "              Done Training                   "
echo "##############################################"



exit 0 