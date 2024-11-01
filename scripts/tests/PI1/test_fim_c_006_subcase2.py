import pytest
import os
from ..helpers import validate_geo_data

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_006_subcase2(test_name,run_shell_script,remove_file,scenarios): #,change_dir
    folder_name = 'PI1/data'
    data_file = test_name + '.json'
    dir_path,output_file,expected_data_file,data_file_location = run_shell_script(folder_name,data_file,scenarios)
    validate_geo_data(dir_path,output_file,os.path.expanduser(expected_data_file),os.path.expanduser(data_file_location))
    remove_file(folder_name,data_file,dir_path,scenarios)

