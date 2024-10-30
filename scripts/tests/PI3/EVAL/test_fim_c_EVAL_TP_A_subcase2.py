import pytest
import os
from ...helpers import validate_directories_files
from ...utils import csv_util,tif_util,directory_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_A_subcase2(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,read_csv,read_tif,fetch_directory_details,remove_file):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory = fetch_directory_details(folder_name,tn,scenarios)
    directory_util.create_directory(directory)
    docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    run_docker_script(folder_name,tn,scenarios,docker_command)
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)

    validate_directories_files([os.path.expanduser(each_directory_locations) for each_directory_locations in directory_locations ],directory_contents)
    csv_file,output_csv_file = read_csv(folder_name,tn,scenarios)
    csv_util.test_extract_csv_data(os.path.expanduser(csv_file),os.path.expanduser(output_csv_file))

    tif_source_file,tif_destination_file = read_tif(folder_name,tn,scenarios)
    tif_util.test_tif_data(os.path.expanduser(tif_source_file),os.path.expanduser(tif_destination_file))

    remove_file(folder_name,tn,os.path.expanduser(directory),scenarios)
    
