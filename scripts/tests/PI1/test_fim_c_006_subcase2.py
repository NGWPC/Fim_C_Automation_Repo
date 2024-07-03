import pytest
from ..helpers import run_commands

def test_fim_c_006_subcase3(test_name,run_shell_script,remove_file): #,change_dir
    folder_name = 'PI1'
    data_file = test_name + '.json'
    dir_path,output_file,expected_data_file = run_shell_script(folder_name,data_file)
    run_commands(dir_path,output_file,expected_data_file)
    remove_file(folder_name,data_file,dir_path)
