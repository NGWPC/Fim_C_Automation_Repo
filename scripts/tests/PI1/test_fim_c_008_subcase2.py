import pytest
from ..helpers import validate_directories_files

def test_fim_c_008_subcase2(test_name,load_scenario_data,scenarios):
    tn = test_name + '.json'
    folder_name = 'PI1/data'
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents)
