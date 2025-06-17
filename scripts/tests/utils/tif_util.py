
import os
import logging



def test_tif_data(source_tif_file,destination_tif_file):
  try:
    with open(source_tif_file ,'rb') as f1 , open(destination_tif_file, 'rb') as f2 :
        print(source_tif_file)
        print(destination_tif_file)
        offset = 0
        file1 = f1.read()
        file2 = f2.read()
        print('I am here 1')
        if file1 == file2:
            print('I am here 2')
            assert file1 == file2 , f"{f1} and {f2} are not identical tif files"
            print('I am here 3')
            logging.info(f"{f1} and {f2} are identical tif files")
        else:
          print('I am here 11')
          return f"Files differ at {offset}: {file1} vs {file2}"
          offset = offset + 1

  except AssertionError as e:
        print('I am here 4')
        logging.error("Non- identical tif files")
        raise e
        
