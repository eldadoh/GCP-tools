VM_DATA_CSV_PATH = 'Data/VMs/vms-data-bq.csv'
OUTPUT_PATH = 'Outputs'
PROJECT_NAME_STR = 'shelfauditdec19'
VM_DATA_CSV = 'Data/vm_metadata.csv'
SCRIPT_NAME = 'run_commands.sh'

SSH_COMMAND_BY_VM_NUMBER_DICT = {'23': f'gcloud beta compute ssh --zone "southamerica-east1-c" "instance-23"  --project "shelfauditdec19"'}