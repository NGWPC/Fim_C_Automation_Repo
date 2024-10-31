import pytest
import os
from ...helpers import validate_directories_files
from ...utils import tif_util

# @pytest.mark.skip(reason="skipping this test for now because it's been delayed")
def test_fim_c_EVAL_TP_D_subcase2(test_name,load_scenario_data,scenarios,read_tif):
    tn = test_name + '.json'
    folder_name = 'PI3/data'
    directory_locations,directory_contents = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents)
    # tif_source_files,tif_destination_files = read_tif(folder_name,tn,scenarios)
    # for tif_source_file , tif_destination_file in zip([os.path.expanduser(each_tif_source_file) for each_tif_source_file in tif_source_files],[os.path.expanduser(each_tif_destination_file) for each_tif_destination_file in tif_destination_files]):
    #     tif_util.test_tif_data(os.path.expanduser(tif_source_file),os.path.expanduser(tif_destination_file))
