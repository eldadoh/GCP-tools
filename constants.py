VM_DATA_CSV_PATH = 'Data/VMs/vms-data-bq.csv'
OUTPUT_PATH = 'Outputs'
PROJECT_NAME = 'shelfauditdec19'
VM_DATA_CSV = 'Data/vm_metadata.csv'
SCRIPT_NAME = 'run_commands.sh'
SCRIPT_NAME_ON_ALL_VM_BASE_PATH_RUN_COMMAND = "./pull_docker.sh"
COMMANDS_TXT_FILE = 'Data/Commands-txt-files/example-commands.txt'
BASH_SCRIPTS_PATH = 'Data/Bash-scripts-generated'

SSH_COMMAND_BY_VM_NUMBER_DICT = {
    '1':f'gcloud beta compute ssh --zone "asia-northeast1-c" "instance-01"  --project "shelfauditdec19"',
    '2':f'gcloud beta compute ssh --zone "us-west4-a" "instance-02"  --project "shelfauditdec19"',
    '3':f'gcloud beta compute ssh --zone "us-west1-b" "instance-03"  --project "shelfauditdec19"',
    '4':f'gcloud beta compute ssh --zone "us-east1-c" "instance-04"  --project "shelfauditdec19"',
    '5':f'gcloud beta compute ssh --zone "europe-west1-b" "instance-05"  --project "shelfauditdec19"',
    '6':f'gcloud beta compute ssh --zone "asia-south1-b" "instance-06"  --project "shelfauditdec19"',
    '7':f'gcloud beta compute ssh --zone "us-central1-a" "instance-07"  --project "shelfauditdec19"',
    '8':f'gcloud beta compute ssh --zone "asia-northeast1-c" "instance-08"  --project "shelfauditdec19"',
    '9':f'gcloud beta compute ssh --zone "asia-northeast3-b" "instance-09"  --project "shelfauditdec19"',
    '10':f'gcloud beta compute ssh --zone "us-central1-a" "instance-10"  --project "shelfauditdec19"',
    '11':f'',
    '12':f'gcloud beta compute ssh --zone "us-central1-f" "instance-12"  --project "shelfauditdec19"',
    '13':f'gcloud beta compute ssh --zone "asia-east1-a" "instance-13"  --project "shelfauditdec19"',
    '14':f'gcloud beta compute ssh --zone "asia-east1-a" "instance-14"  --project "shelfauditdec19"',
    '15':f'gcloud beta compute ssh --zone "asia-northeast1-c" "instance-15"  --project "shelfauditdec19"',
    '16':f'gcloud beta compute ssh --zone "asia-east1-a" "instance-16"  --project "shelfauditdec19"',
    '17':f'',
    '18':f'gcloud beta compute ssh --zone "asia-south1-b" "instance-18"  --project "shelfauditdec19"',
    '19':f'gcloud beta compute ssh --zone "asia-southeast1-b" "instance-19"  --project "shelfauditdec19"',
    '20':f'gcloud beta compute ssh --zone "asia-southeast1-b" "instance-20"  --project "shelfauditdec19"',
    '21':f'gcloud beta compute ssh --zone "asia-southeast2-a" "instance-21"  --project "shelfauditdec19"',
    '22':f'gcloud beta compute ssh --zone "australia-southeast1-c" "instance-22"  --project "shelfauditdec19"',
    '23':f'gcloud beta compute ssh --zone "southamerica-east1-c" "instance-23"  --project "shelfauditdec19"',
    '24':f'',
    '25':f''}