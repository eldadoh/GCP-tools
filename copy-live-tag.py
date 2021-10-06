import os

project = 'doralon_shelves2'
version = 'V05-10-21'
LIVE_TAG_PATHS_FILE = 'Data/live-tag-input/live_tag_example.txt'
LIVE_TAG_IMAGE_EXTENSION = '.jpg'

def move_live_tag_files_logs_format(config_file, live_tag_dir, live_tag_images):

    with open(config_file, 'r') as f:
        sessions_ = [line.strip() for line in f]
    for session_ in sessions_:
        if len(session_.strip()) > 0:
            print(f"downloading live tag session:")
            print(session_)
            session_root = os.path.split(session_)[0]

            os.system(f'gsutil ls gs://{session_root} > Data/live-tag-input/temp.txt')
            with open('Data/live-tag-input/temp.txt', 'r') as f:
                paths = [line.strip() for line in f]
                for path in paths : 
                    if path.endswith('Logs/') == False:         
                        session_root = path.split(sep='/')[-3]                                   
                        session_full_path = os.path.join(path,'Images') 
                        os.makedirs(os.path.join(live_tag_dir, session_root), exist_ok=True)
                        os.system(f"gsutil -m cp -n {session_full_path}/*.txt {live_tag_dir}/{session_root}")
                        os.system(f"gsutil -m cp -n {session_full_path}/*{LIVE_TAG_IMAGE_EXTENSION} {live_tag_images}/{session_root}")

def run():


    target_images_dir = f'gs://shelfauditdec19.appspot.com/march_2021/{project}/images/live_tag_local'
    target_annotations_dir = f'gs://shelfauditdec19.appspot.com/march_2021/{project}/{version}/annotations/live_tag_local'
    
    move_live_tag_files_logs_format(LIVE_TAG_PATHS_FILE, target_annotations_dir, target_images_dir)

run()