import subprocess
import os
import json

def test_run(file_name , output_file,expected_data_file):
    file_path = os.path.join(file_name,output_file)
    print("file_path is "+file_path)
    assert os.path.exists(file_path)

    command = "SELECT table_name FROM gpkg_contents;"
    result = subprocess.run(['sqlite3',file_path,command],stdout = subprocess.PIPE,universal_newlines = True)
    if result.returncode != 0:
        return none
    if result:

        print(result)

    command = f"SELECT * FROM {output_file.split('.')[0]};"
    result = subprocess.run(['sqlite3',file_path,command],stdout = subprocess.PIPE,universal_newlines = True)
###### Add this for extracting data in the form of a list #########
    result_list = result.stdout.strip().split('\n',-1)
##############################################################
    if result.returncode != 0:
        print(f"Error {result.stderr}")
        return none
    if result:
        print("Data available")

    with open(expected_data_file,'r') as file:
        data = json.load(file)
        geo_data = data['geo_data']
    for i in range(0,len(geo_data)):
        assert result_list[i] ==geo_data[i] , "Expected data not listed"
  
    print("Validation successful")
