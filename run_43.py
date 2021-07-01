import os 
import subprocess
# from parse_vm_data import parse_vm_csv
from gcp_vm_commands import run_one_vm_cycle,stop_vm

def main():
    
    PROJECT_NAME_STR = 'shelfauditdec19'
    SCRIPT_NAME_43 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_43.sh' 
                     
    run_one_vm_cycle('instance-43','us-west4-a',PROJECT_NAME_STR,SCRIPT_NAME_43)

if __name__ == "__main__":
    main()
