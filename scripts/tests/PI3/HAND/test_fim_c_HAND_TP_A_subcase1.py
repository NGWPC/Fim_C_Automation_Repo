import pytest
import os
from ...helpers import validate_directories_files
from ...utils import gpkg_metadata_util,gpkg_util

@pytest.mark.skip(reason="No longer valid")
def test_fim_c_HAND_TP_A_subcase1(test_name,load_scenario_data,scenarios,fetch_data_file_metadata_details,fetch_data_file_details):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    source_file,expected_data_file,fields =fetch_data_file_metadata_details(folder_name ,tn, scenarios)
    gpkg_metadata_util.compare_gpkgs_metadata(source_file,fields)
    dir_path,output_file,expected_data_file,data_file_location = fetch_data_file_details(folder_name,tn,scenarios)
    gpkg_util.validate_geo_data(dir_path,output_file,os.path.expanduser(expected_data_file),os.path.expanduser(data_file_location))
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)