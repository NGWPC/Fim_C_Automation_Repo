import pytest
from ...helpers import validate_directories_files

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_A_subcase1(test_name,load_scenario_data,scenarios):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents)
