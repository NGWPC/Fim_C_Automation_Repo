import pytest
import os
from ...helpers import validate_directories_files,verify_STAC_dashboard

# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_C_subcase2_supplement(test_name,load_scenario_data,scenarios):
    verfify_gfm_data()
