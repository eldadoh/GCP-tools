import json
import pandas as pd 
import time

def parse_vm_csv(csv_filename):
    
    df = pd.read_csv(csv_filename)
    df = df[['instance','zone']]
    df = df.sort_values('instance',ascending=True)
    df.to_csv('Data/vm_parsed_data.csv')
    
    df_dict = df.to_dict()

    insatnces = list(df_dict['instance'].values())
    zones = list(df_dict['zone'].values())

    return insatnces,zones 

def parse_vm_json(json_filename): 

    f = open(json_filename)

    data = json.load(f)

    for i,vm_sample in enumerate(data):
        if not vm_sample['instance'].startswith('instance-'):
            data.pop(i)
        
    f.close()
