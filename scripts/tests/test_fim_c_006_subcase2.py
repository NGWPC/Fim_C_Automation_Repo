import subprocess
import os
import time
import logging
import qgis

def test_run_commands():
  

   shell_script = '/home/jyoti.mikkilineni/pw/auto/scripts/tests/ana_run.sh'
   result = subprocess.run(['bash',shell_script],stdout = subprocess.PIPE , universal_newlines = True) #capture_output = True,, text=True
   
   variable_value = result.stdout.strip()
   print(variable_value)
   dir_path = '/efs/translated_ras_libraries/temp/'+ variable_value
   #time.sleep(400)
   sep ='\n'
   dir_path = dir_path.split(sep,1)[0]
   assert os.path.isdir(dir_path) == True , "Directory1 does not exist"+dir_path
   assert os.path.exists(dir_path) == True , "Directory does not exist"+dir_path
   os.chdir(dir_path)
   print("Current working directory" +os.getcwd())

  # assert os.getcwd() == dir_path, "Failed to load the directory" + dir_path

   dir_contents = sorted(os.listdir())
   file_path = os.path.join(dir_path,'output_ras2inundation.gpkg')
   assert os.path.isfile(file_path) == True , "File does not exist"

   print("STDOUT:", result.stdout)
   print("STDERR:", result.stderr)
   qgis.test_run(dir_path)

if __name__ == "__main__":
    test_run_commands()
