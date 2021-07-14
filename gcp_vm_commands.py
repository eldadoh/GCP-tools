import os 
import subprocess
import time 
from google.cloud import storage



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

def list_all_buckets_names():
    os.system('gsutil ls')

def list_bucket_files(bucket_name) : 
    os.system(f'gsutil ls -r gs://{bucket_name}/**')

def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name
):
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )
