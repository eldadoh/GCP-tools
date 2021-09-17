from genericpath import exists
import os
import subprocess
import argparse

""" 
    util script for asaf , list all the images names in a bucket/folder 
"""

def list_storage_dir_files_func(BUCKET,SUFFIX): 

    if not os.path.isdir('Outputs'):

        os.makedirs('Outputs', exist_ok=True)
    
    BUCKET = 'gs://' + f'{BUCKET}'

    OUTPUT_FILE_NAME = os.path.join('Outputs',os.path.basename(BUCKET) + '.csv')

    with open (f'{OUTPUT_FILE_NAME}' , 'a') as w : 

        util_list = []

        result = subprocess.run(['gsutil','ls', f'{BUCKET}'], stdout=subprocess.PIPE)
        result_long_str = result.stdout.decode("utf-8")
        result_long_list = result_long_str.splitlines() 
        
        [util_list.append(item) for item in result_long_list if item.endswith(SUFFIX)]
        result_long_list = [item.split('/')[-1] + '\n'  for item in result_long_list if item.endswith(SUFFIX)]
        w.writelines(result_long_list)

def main(): 
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--bucket', type=str)
    parser.add_argument('-s', '--suffix', type=str, default='.jpg')

    args = parser.parse_args()

    list_storage_dir_files_func(args.bucket,args.suffix)

    # BUCKET = 'shelfauditdec19.appspot.com/march_2021_visualizations/doralon_sweets/V1/crops_by_class/Click_7290112494276'
    # SUFFIX = '.jpg'

    # list_storage_dir_files_func(BUCKET,SUFFIX)

if __name__ == "__main__":
    
    main()
    
    #usage: python3 list_storage_dir_files.py -b {bucket} -s {suffix}
    #example : python3 list_storage_dir_files.py -b shelfauditdec19.appspot.com/march_2021_visualizations/doralon_sweets/V1/crops_by_class/Click_7290112494276 -s '.jpg'