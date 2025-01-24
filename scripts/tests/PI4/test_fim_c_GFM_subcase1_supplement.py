import pytest
import os
from ..utils import benchmark_stac_util
# @pytest.mark.skip(reason="skipping this test for now")
def test_fim_c_EVAL_TP_C_subcase2_supplement(test_name,load_scenario_data,scenarios):
    print("Main test")
    benchmark_stac_util.verify_gfm_data()
