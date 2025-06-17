import os
import shutil

def test_copy_all_files(source_dir,destination_dir):
    os.makedirs(destination_dir , exist_ok = True)
    for filename in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir,filename)
        destination_file_path = os.path.join(destination_dir,filename)
        print("SF",os.access(source_file_path, os.R_OK))
        print("DF",os.access(destination_file_path, os.W_OK))
        print("UID",os.getuid())
        print("Groups" , os.getgroups())
        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path,destination_file_path)
            print(f"copied {filename}")