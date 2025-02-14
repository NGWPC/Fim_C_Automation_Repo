import pytest
import os
from ...helpers import validate_directories_files
from ...utils import benchmark_stac_util

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_C_subcase2_supplement(test_name,load_scenario_data,scenarios,fetch_stac_ui_details):
    tn = test_name.rsplit("_",1)[0]
    tn = tn + '.json'
    folder_name = 'PI3/data'
    link,item = fetch_stac_ui_details(folder_name,tn,scenarios)
    benchmark_stac_util.verify_STAC_dashboard(link)
