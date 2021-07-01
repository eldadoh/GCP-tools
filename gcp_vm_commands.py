import os 
import subprocess
import time 

def start_vm(instance_name_str,zone_str):
    command = f'gcloud compute instances start --zone {zone_str}  {instance_name_str}'
    os.system(command)

def stop_vm(instance_name_str,zone_str):
    command = f'gcloud compute instances stop --zone {zone_str}  {instance_name_str}'
    os.system(command)
    
def ssh_login_and_run_commands_script(instance_name_str,zone_str ,project_name_str,script_name = r'./run_commands.sh'):
    
    script_commands = subprocess.call([ 'bash' , script_name ])
    # script_commands = subprocess.call([ 'bash' , './' + script_name ])
    # command = f'gcloud beta compute ssh --zone {zone_str} {instance_name_str}  --project {project_name_str} --command {script_commands}'
    command = f'gcloud beta compute ssh --zone {zone_str} {instance_name_str}  --project {project_name_str} --command={script_commands}'
    os.system(command)

def run_one_vm_cycle(instance_name_str,zone_str ,project_name_str,script_name):

    start_vm(instance_name_str,zone_str)
    ssh_login_and_run_commands_script(instance_name_str,zone_str,project_name_str,script_name)
    stop_vm(instance_name_str,zone_str)
