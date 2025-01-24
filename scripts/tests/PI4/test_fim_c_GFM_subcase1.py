import pytest
import os

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_GFM_subcase1(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script):
    tn = test_name + '.json'
    folder_name = 'PI4/data'
    docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    run_docker_script(folder_name,tn,scenarios,docker_command)
