import pytest
import os
from ..utils import benchmark_stac_util
from ..helpers import validate_directories_files

@pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_GFM_subcase1_supplement(test_name,load_scenario_data,scenarios,fetch_stac_ui_details):
    print("Main test check")
    tn = test_name.rsplit("_",1)[0]
    tn = tn + '.json'
    folder_name = 'PI4/data'
    link,item = fetch_stac_ui_details(folder_name,tn,scenarios)
    benchmark_stac_util.verify_gfm_data(link, item)
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files([os.path.expanduser(each_dir_locations) for each_dir_locations in directory_locations],directory_contents,flag)

