import pytest
import os
import shutil
from ...helpers import validate_directories_files,validate_response,validate_downloaded_content,update_aws_credentials
from ...utils import csv_util,gpkg_util,txt_file_validation_util

# @pytest.mark.skip(reason="skipping this test for now")
#Run it from the autoeval-coordinator directory.Also check for 
def test_fim_c_TP_A_EVAL_subcase2(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,read_csv,fetch_data_file_details,fetch_txt_details,fetch_directory_details,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI7/data'
    
    directory = fetch_directory_details(folder_name,tn,scenarios)
    docker_commands,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    print(shutil.which("docker"))
    for i,docker_command in enumerate(docker_commands):
         if i==3:
           print("Here")
           print(repr(docker_command))
           docker_command=update_aws_credentials(docker_command)
         run_docker_script(folder_name,tn,scenarios,docker_command)
         print("The command ran successfully.")
    text,dir_paths = fetch_txt_details(folder_name,tn,scenarios)
    for txt, dir_path in zip([each_text for each_text in text],[os.path.expanduser(each_dir_path_file) for each_dir_path_file in dir_paths]):
      for text_file in txt:
           txt_file_validation_util.txt_file_validation(text_file,dir_path)