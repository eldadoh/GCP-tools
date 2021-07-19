import os
import glob
import subprocess

""" 
    util script for asaf , list all the images names in a bucket/folder 
"""

BUCKET = 'gs://shelfauditdec19.appspot.com/march_2021_visualizations/doralon_sweets/V1/crops_by_class/Click_7290112494276'
OUTPUT_CSV_NAME = 'images_names.csv'

with open (f'{OUTPUT_CSV_NAME}' , 'a') as w : 

    util_list = []

    result = subprocess.run(['gsutil','ls', f'{BUCKET}'], stdout=subprocess.PIPE)
    result_long_str = result.stdout.decode("utf-8")
    result_long_list = result_long_str.splitlines()

    [util_list.append(item) for item in result_long_list if item.endswith('.jpg')]
    result_long_list = [item.split('/')[-1] + '\n'  for item in result_long_list if item.endswith('.jpg')]
    w.writelines(result_long_list)



