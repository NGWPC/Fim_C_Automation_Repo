import pytest
import os
from ..helpers import validate_directories_files,generate_dfo_data
from ..utils import txt_util,readme_util,json_util,csv_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_001_subcase2(test_name,load_scenario_data,scenarios,read_me,json_read,read_csv):
    tn = test_name + '.json'
    folder_name = 'PI2/data'
    generate_dfo_data()
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    # print(str(directory_locations[0]))
    # remove_file(folder_name,'report.html',str(directory_locations[0]),scenarios)
    validate_directories_files([os.path.expanduser(each_directory_locations) for each_directory_locations in directory_locations ],directory_contents)
    source_read_me_location,destination_read_me_location = read_me(folder_name,tn,scenarios)
    readme_util.validate_readme( os.path.expanduser(source_read_me_location),os.path.expanduser(destination_read_me_location))
    source_json_file_location,destination_json_file_location = json_read(folder_name,tn,scenarios)
    json_util.validate_json( os.path.expanduser(source_json_file_location),os.path.expanduser(destination_json_file_location))
    csv_file,output_csv_file = read_csv(folder_name,tn,scenarios)
    csv_util.test_extract_csv_data(os.path.expanduser(csv_file),os.path.expanduser(output_csv_file))
