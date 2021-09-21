import json
import pandas as pd ,numpy as np
import os,subprocess,json
from constants import *
from google.cloud import storage

def list_all_buckets_names():
    os.system('gsutil ls')

def list_bucket_files(bucket_name) : 
    os.system(f'gsutil ls -r gs://{bucket_name}/**')

def copy_blob(bucket_name, blob_name, destination_bucket_name, destination_blob_name):

    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(source_blob, destination_bucket, destination_blob_name)

    print("Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name))


def get_vm_data_csv(csv_filename):
    df = pd.read_csv(csv_filename)
    df = df[['instance','zone']]
    df = df.sort_values('instance',ascending=True)
    df = df.reset_index(drop=True)
    insatnces = df['instance'].to_list()  
    zones = df['zone'].to_list()
    return df, insatnces,zones
    
def start_command(instance_name_str,zone_str):
    command = f'gcloud compute instances start --zone {zone_str}  {instance_name_str}&'
    os.system(command)

def start_all_vms(instances,zones):
    [start_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances,zones)]

def start_specific_range_vms(start_number,end_number):
    _,instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    [start_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances[start_number-1:end_number],zones[start_number-1:end_number])]

def start_specific_vms(vms_list:list):
    _,instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
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
    _,instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    [stop_command(instance_name,instance_zone) for (instance_name,instance_zone) in zip(instances[start_number-1:end_number],zones[start_number-1:end_number])]

def stop_specific_vms(vms_list:list):
    _,instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    instances_zones_as_tuple_pairs = dict(zip(instances,zones))
    vms_list = [f'instance-' + f'{str(vm_number)}'.zfill(2) for vm_number in vms_list]
    chosen_vms_data = [[vm,instances_zones_as_tuple_pairs[f'{vm}']] for vm in vms_list if vm in [instances,zones][0]]
    [stop_command(instance_name,instance_zone) for (instance_name,instance_zone) in chosen_vms_data]
    return chosen_vms_data

def ssh_login_and_run_commands_script(df,vm_number,command = SCRIPT_NAME_ON_ALL_VM_BASE_PATH_RUN_COMMAND, project_name_str=PROJECT_NAME):

    # SCRIPT_NAME_ON_ALL_VM_BASE_PATH_RUN_COMMAND = "./pull_docker.sh"

    instance_name, zone = get_vm_attributes_from_vm_number(df,vm_number)
    if command is not None : 
        return os.system (f'gcloud beta compute ssh --zone {zone} {instance_name}  --project {project_name_str} --command={command}')
    else : 
        return os.system (f'gcloud beta compute ssh --zone {zone} {instance_name}  --project {project_name_str}')

def ssh_to_machine_via_number(vm_number:int): 
    return os.system(SSH_COMMAND_BY_VM_NUMBER_DICT[f'{vm_number}'])

def start_and_connect_to_vm(vm_number:int):
    start_specific_vms([f'{vm_number}'])
    ssh_to_machine_via_number(vm_number)

def get_vm_attributes_from_vm_number(df, vm_number : int): 
    instance_name = f'instance-' + str(vm_number).zfill(2)
    instance_idx = list(np.where(df['instance'] == instance_name)[0])
    zone = df.iloc[instance_idx]['zone'].item()
    return instance_name,zone

def send_script_to_vm(df,vm_number,src_path = None , dest_path = None): 

    instance_name , zone = get_vm_attributes_from_vm_number(df, vm_number)
    if src_path == None : src_path = './pull_docker.sh'
    if dest_path == None : dest_path = f'{instance_name}:~'
    return os.system(f'gcloud compute scp --project {PROJECT_NAME} --zone {zone} {src_path} {dest_path} ')

def send_script_to_all_vms(df):

    #currently serial and not parallel

    df['vm_number'] = df['instance'].apply(lambda x : str(int(x.split(sep='-')[-1].strip())))
    vm_numbers = df['vm_number'].to_list()
    [send_script_to_vm(df,vm_number) for vm_number in vm_numbers[5:7]]

def main(): 

    df,instances,zones = get_vm_data_csv(VM_DATA_CSV_PATH)
    
    # start_specific_vms([21])
    # ssh_login_and_run_commands_script(df,21,command="bash pull_docker.sh")
    
    # ssh_login_and_run_commands_script(df,21,command = SCRIPT_NAME_ON_ALL_VM_BASE_PATH_RUN_COMMAND)
    # ssh_login_and_run_commands_script(df,command = "ls")
    # ssh_login_and_run_commands_script(df,21,command = f'docker pull gcr.io/shelfauditdec19/my_darknet:live-tag')
    
    # stop_specific_range_vms(2,5)5-2+1 
    # chosen_vms_data = start_specific_vms([62,63])
    # ssh_login_and_run_commands_script(instance_name_str='instance-12',zone_str=chosen_vms_data['instance-12'])
    # start_specific_vms([23])
    # ssh_to_machine_via_number(23)
    # send_script_to_vm(df,21)
    # start_specific_vms([1,2,3,4,5])
    # send_script_to_all_vms(df)
    stop_specific_vms([1,2,3,4,5,6])

    


if __name__ == "__main__":
    
    main()