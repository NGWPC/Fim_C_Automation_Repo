import pytest
from ..helpers import validate_directories_files
from ..utils import txt_util

def test_fim_c_001_subcase1(test_name,load_scenario_data,scenarios,read_txt):
    tn = test_name + '.json'
    folder_name = 'PI2/data'
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents)
    txt_file,total_records,expected_record_value = read_txt(folder_name,tn,scenarios)
    txt_util.extract_txt_data(txt_file,total_records)
    txt_util.check_txt_data(txt_file,expected_record_value)
