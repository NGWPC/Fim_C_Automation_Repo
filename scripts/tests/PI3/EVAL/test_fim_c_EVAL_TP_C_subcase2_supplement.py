import pytest
import os
from ...helpers import validate_directories_files,verify_STAC_dashboard

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_C_subcase2_supplement(test_name,load_scenario_data,scenarios):
    # tn = test_name + '.json'
    # folder_name = 'PI3/data'
    # docker_command,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    # run_docker_script(folder_name,tn,scenarios,docker_command)
    verify_STAC_dashboard()
