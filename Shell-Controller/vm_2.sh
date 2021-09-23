#!/bin/sh
gcloud beta compute ssh --zone "europe-west1-b" "instance-05"  --project "shelfauditdec19" \
 --command="echo 'eldad' && docker ps && sleep 30"
