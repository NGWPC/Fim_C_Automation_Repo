# tests/conftest.py

import pytest
import os
import subprocess
import logging 
import json

#Logging code
### Adding Logger logic ##########
logging.basicConfig(level=logging.INFO,

  format = '%(asctime)s - %(levelname)s -%(message)s')

@pytest.fixture(scope="session")
def scenarios():
    def _scenarios(folder_name,data_file):
         with open(os.path.join(os.path.dirname(__file__), folder_name,data_file), 'r') as file:
          return json.load(file)
    return _scenarios

@pytest.fixture
def run_shell_script():
    def _run_shell_script(folder_name,data_file):
        with open(os.path.join(os.path.dirname(__file__),folder_name,data_file), 'r') as file:
            scenario = json.load(file)
    # print("Display param here " +request.param)
        shell_script = scenario['additional_data'][0].get('shell_script')
        result =  subprocess.run(['bash',shell_script],stdout = subprocess.PIPE , universal_newlines = True)
        variable_value = result.stdout.strip()
        dir_path = scenario['additional_data'][0].get('base_directory')+ variable_value.split('\n',1)[0]
        return dir_path,scenario['additional_data'][0].get('output_file'),scenario['additional_data'][0].get('expected_data_file')
    return _run_shell_script

@pytest.fixture
def change_dir(run_shell_script):
    dir_path , _  = run_shell_script
    os.chdir(dir_path)
    yield
    os.chdir(os.path.dirname(dir_path))

@pytest.fixture
def load_scenario_data():
    def _load_scenario_data(folder_name,scenario_name):
        with open(os.path.join(os.path.dirname(__file__),folder_name,scenario_name), 'r') as file:
            data = json.load(file)
            directory_locations = data['d_loc']
            directory_contents = data['d_files']
            return directory_locations,directory_contents
    return _load_scenario_data

@pytest.fixture
def test_name(request):
    print(f"Running test: {request.node.name}")
    return request.node.name

@pytest.fixture
def remove_file():
    def _remove_file(folder_name , data_file , file_name_path):
      print("file_name_path: "+file_name_path)
      assert os.path.exists(file_name_path)
      with open(os.path.join(os.path.dirname(__file__),folder_name,data_file), 'r') as file:
            scenario = json.load(file)
            shell_script = scenario['additional_data'][0].get('remove_file_shell_script')
            print("file_name_path1: "+file_name_path)
            result = subprocess.run(['bash',shell_script ,file_name_path ],stdout = subprocess.PIPE, universal_newlines = True)
            return result.stdout.strip()
    return _remove_file   

@pytest.fixture
def read_csv():
    def _read_csv(folder_name , data_file, scenarios):
         scenario = scenarios(folder_name , data_file)
         return scenario['additional_data'][0].get('csv_file') , scenario['additional_data'][0].get('output_csv_file')
    return _read_csv 

@pytest.fixture
def fetch_data_file_details():
    def _fetch_data_file_details(folder_name , data_file, scenarios):
         scenario = scenarios(folder_name , data_file)
         return scenario['additional_data'][0].get('base_directory') , scenario['additional_data'][0].get('output_file'), scenario['additional_data'][0].get('expected_data_file')
    return _fetch_data_file_details 
        
