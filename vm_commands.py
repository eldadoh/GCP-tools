import json
import pandas as pd 
import os,subprocess,json
from constants import *
from google.cloud import storage

def get_vm_data_csv(csv_filename):
    df = pd.read_csv(csv_filename)
    df = df[['instance','zone']]
    df = df.sort_values('instance',ascending=True)
    insatnces = df['instance'].to_list()
    zones = df['zone'].to_list()
    return insatnces,zones 

def start_command(instance_name_str,zone_str):
    command = f'gcloud compute instances start --zone {zone_str}  {instance_name_str}&'
    os.system(command)

def start_all_vms(instances,zones):
    [start_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances,zones)]

def start_specific_range_vms(start_number,end_number:list):
    instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    [start_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances[start_number-1:end_number],zones[start_number-1:end_number])]

def start_specific_vms(vms_list:list):
    instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    instances_zones_as_tuple_pairs = dict(zip(instances,zones))
    vms_list = [f'instance-' + f'{str(vm_number)}'.zfill(2) for vm_number in vms_list]
    chosen_vms_data = [[vm,instances_zones_as_tuple_pairs[f'{vm}']] for vm in vms_list if vm in [instances,zones][0]]
    [start_command(instance_name,instance_zone) for (instance_name,instance_zone) in chosen_vms_data]
    return chosen_vms_data[0]

def stop_command(instance_name_str,zone_str):
    command = f'gcloud compute instances stop --zone {zone_str}  {instance_name_str}&'
    os.system(command)

def stop_all_vms(instances,zones):
    [stop_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances,zones)]

def stop_specific_range_vms(start_number,end_number:list):
    instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    [stop_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances[start_number-1:end_number],zones[start_number-1:end_number])]

def stop_specific_vms(vms_list:list):
    instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    instances_zones_as_tuple_pairs = dict(zip(instances,zones))
    vms_list = [f'instance-' + f'{str(vm_number)}'.zfill(2) for vm_number in vms_list]
    chosen_vms_data = [[vm,instances_zones_as_tuple_pairs[f'{vm}']] for vm in vms_list if vm in [instances,zones][0]]
    [stop_command(instance_name,instance_zone) for (instance_name,instance_zone) in chosen_vms_data]
    return chosen_vms_data

def ssh_login_and_run_commands_script(instance_name_str,zone_str ,project_name_str=PROJECT_NAME_STR):
    
    # script_commands = subprocess.call([ 'bash' , script_name ])
    command = f'gcloud beta compute ssh --zone {zone_str} {instance_name_str}  --project {project_name_str}' #--command={script_commands}'
    os.system(command)

def ssh_to_machine_via_number(vm_number:int): 
    return os.system(SSH_COMMAND_BY_VM_NUMBER_DICT[f'{vm_number}'])

def start_and_connect_to_vm(vm_number:int):
    start_specific_vms([f'{vm_number}'])
    ssh_to_machine_via_number(vm_number)

def main(): 

    instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    # stop_specific_range_vms(2,5)5-2+1 
    # chosen_vms_data = start_specific_vms([62,63])
    # ssh_login_and_run_commands_script(instance_name_str='instance-12',zone_str=chosen_vms_data['instance-12'])
    # start_specific_vms([23])
    # ssh_to_machine_via_number(23)
    # start_specific_vms([1,2,3,4,5])
    # stop_specific_vms([1,2,3,4,5])
    # # start_and_connect_to_vm(vm_number=23)
    # stop_all_vms(instances,zones)
    

if __name__ == "__main__":
    
    main()