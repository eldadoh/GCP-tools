#!/bin/sh
# -command="echo 'eldad' && docker ps && sleep 10"
# command1="echo 'eldad'"
# command2="docker ps"
# command3="sleep 10"
gcloud beta compute ssh --zone "us-west4-a" "instance-02"  --project "shelfauditdec19" \
 --command="echo 'eldad' && docker ps && sleep 30"