import pytest
import os
import time
from ...helpers import validate_directories_files,validate_geo_data
from ...utils import gpkg_metadata_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_HAND_TP_A_subcase2(test_name,load_scenario_data,scenarios,run_shell_script_from_directory):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    run_shell_script_from_directory(folder_name,tn,scenarios)
    print("Adding wait time")
    time.sleep(780)
    print("Wait time ended")
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios) #,flag
    validate_directories_files(directory_locations,directory_contents) #,flag