import os 
import subprocess
from vm_commands import get_vm_data_csv
from gcp_vm_commands import run_one_vm_cycle,stop_vm

def main():
    
    PROJECT_NAME_STR = 'shelfauditdec19'
    VM_DATA_CSV = 'Data/vm_metadata.csv'
    SCRIPT_NAME = 'run_commands.sh'
    

    SCRIPT_NAME_41 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_41.sh'
    SCRIPT_NAME_42 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_42.sh'
    SCRIPT_NAME_43 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_43.sh'
    SCRIPT_NAME_44 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_44.sh'
    
    run_one_vm_cycle('instance-41','asia-east1-a',PROJECT_NAME_STR,SCRIPT_NAME_41)
    run_one_vm_cycle('instance-42','asia-northeast1-c',PROJECT_NAME_STR,SCRIPT_NAME_42)
    run_one_vm_cycle('instance-43','us-west4-a',PROJECT_NAME_STR,SCRIPT_NAME_43)
    run_one_vm_cycle('instance-44' ,'us-east1-d',PROJECT_NAME_STR,SCRIPT_NAME_44)
    
    # Option1: run exp on single machine 
    # run_one_vm_cycle(instance_name_str = 'instance-17',zone_str = 'us-west4-a' ,project_name_str=PROJECT_NAME_STR,script_name=SCRIPT_NAME)

    # Option2: run exp on all the machines from the csv 
    # instance_names,zones_names  = parse_vm_csv(VM_DATA_CSV)
    # instance_names,zones_names = instance_names[30:50],zones_names[30:50] #new machines 
    # for instance,zone in zip(instance_names,zones_names):
        # stop_vm(instance,zone)
        #  run_one_vm_cycle(instance ,zone ,PROJECT_NAME_STR,SCRIPT_NAME)
    
if __name__ == "__main__":
    main()
