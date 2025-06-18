
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
        if file1 == file2:
            print('I am here 2')
            assert file1 == file2 , f"{f1} and {f2} are not identical tif files"
            logging.info(f"{f1} and {f2} are identical tif files")
        else:
          return f"Files differ at {offset}: {file1} vs {file2}"
          offset = offset + 1

  except AssertionError as e:
        logging.error("Non- identical tif files")
        raise e
        
