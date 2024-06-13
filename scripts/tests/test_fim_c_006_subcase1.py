import subprocess
import os
import json
import logging
### Adding Logger logic ##########
logging.basicConfig(level=logging.INFO,

  format = '%(asctime)s - %(levelname)s -%(message)s',

  handlers=[logging.FileHandler('app.log'), logging.StreamHandler()])

def test_execute_data_extraction_scripts():
    ##### Fetching Directories locations and expected files lists from JSON file #######
    directory_locations = []
    directory_contents = []

    with open('/home/jyoti.mikkilineni/pw/auto/scripts/tests/sample.json','r') as file:
        data = json.load(file)

        directory_locations = data['d_loc']
        directory_contents = data['d_files']

    for i in range(0,len(directory_locations)):

        dir_location = directory_locations[i]
        os.chdir(dir_location)
        assert os.getcwd() == dir_location, "Failed to load the directory" + dir_location
        dir_contents = sorted(os.listdir())
        try: 
            assert dir_contents ==directory_contents[i] , "Expected files not listed"
            logging.info("Expected files listed")
        except AssertionError as e:
            logging.error("Assertion failed for:")
        

if __name__ == "__main__":
    execute_data_extraction_scripts()
