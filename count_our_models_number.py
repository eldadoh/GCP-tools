import os
import glob
import subprocess

""" 
    can read and process now output to the stdout of the terminal 
"""

Main_Bucket = 'gs://shelfauditdec19.appspot.com/CVModels/'

training_days_dirs = 'training_days.txt'
output_file_name = 'models_count.txt'

models_counter  = 0 

with open(f'{training_days_dirs}', 'r') as f :

    with open ( output_file_name, 'a') as w : 

        for i,line in enumerate(f) :
            util_list = []
            result = subprocess.run(['gsutil','ls', f'{line}'], stdout=subprocess.PIPE)
            result_long_str = result.stdout.decode("utf-8")
            result_long_list = result_long_str.splitlines()

            [util_list.append(item) for item in result_long_list if item.endswith('weights')]
            result_long_list = [item.split('/')[-1] + '\n'  for item in result_long_list if item.endswith('weights')]
            
            models_counter += len(util_list)
            w.writelines(result_long_list)

        print(f'\nTotal number of models trained so far is : {models_counter}')