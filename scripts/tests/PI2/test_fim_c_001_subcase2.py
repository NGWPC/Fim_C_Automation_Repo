import pytest
from ..helpers import validate_directories_files,generate_dfo_data
from ..utils import txt_util

def test_fim_c_001_subcase2(test_name,load_scenario_data,scenarios,read_txt):
    tn = test_name + '.json'
    folder_name = 'PI2/data'
    generate_dfo_data()
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents)
