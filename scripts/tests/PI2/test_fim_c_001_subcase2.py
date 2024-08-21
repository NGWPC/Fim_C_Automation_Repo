import pytest
from ..helpers import validate_directories_files,generate_dfo_data
from ..utils import txt_util,readme_util

def test_fim_c_001_subcase2(test_name,load_scenario_data,scenarios,read_me):
    tn = test_name + '.json'
    folder_name = 'PI2/data'
    generate_dfo_data()
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    # print(str(directory_locations[0]))
    # remove_file(folder_name,'report.html',str(directory_locations[0]),scenarios)
    validate_directories_files(directory_locations,directory_contents)
    source_read_me_location,destination_read_me_location = read_me(folder_name,tn,scenarios)
    readme_util.validate_readme( source_read_me_location,destination_read_me_location)
