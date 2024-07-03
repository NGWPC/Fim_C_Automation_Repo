import pytest
from ..helpers import validate_directories_files

def test_fim_c_006_subcase1(test_name,load_scenario_data):
    tn = test_name + '.json'
    folder_name = 'PI1'
    directory_locations,directory_contents = load_scenario_data(folder_name,tn)
    validate_directories_files(directory_locations,directory_contents)
