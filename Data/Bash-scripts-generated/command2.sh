#!/bin/sh
docker run --env EXP_NAME='Demo-V5-salties' --net=host --rm --gpus all -it gcr.io/shelfauditdec19/my_darknet:live-tag   hybrid-dubonim-kefli-cheetos doralon 5000 --use_new_mapping --dataset_version V29-8-21-all --base_model fastest --input_size 96 --train_on_crops --visual_crop_spare 0.1 --crop_mode none --live_tag live_tag_example.txt
exit 0
