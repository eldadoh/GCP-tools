import os 
import subprocess
# from parse_vm_data import parse_vm_csv
from gcp_vm_commands import run_one_vm_cycle,stop_vm

def main():
    
    PROJECT_NAME_STR = 'shelfauditdec19'
    SCRIPT_NAME_41 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_41.sh' 
                     
    run_one_vm_cycle('instance-41','asia-east1-a',PROJECT_NAME_STR,SCRIPT_NAME_41)

if __name__ == "__main__":
    main()
