import os 
import subprocess
# from parse_vm_data import parse_vm_csv
from gcp_vm_commands import run_one_vm_cycle,stop_vm

def main():
    
    PROJECT_NAME_STR = 'shelfauditdec19'
    SCRIPT_NAME_44 = '/home/arpalus/Work_Eldad/Arpalus_Code/Eldad-Local/Eldad-GCP/Bash_scripts/run_44.sh'             
    run_one_vm_cycle('instance-44','us-east1-d',PROJECT_NAME_STR,SCRIPT_NAME_44)

if __name__ == "__main__":
    main()
