import pytest
from ...helpers import validate_directories_files
from ...utils import sql_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_RAS_001_subcase1(test_name,load_scenario_data,scenarios,sql_read):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)
    dir_path = sql_read(folder_name,tn,scenarios)
    sql_util.test_sql_read(dir_path)
