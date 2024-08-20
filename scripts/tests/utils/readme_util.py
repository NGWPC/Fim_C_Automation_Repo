import filecmp
import logging

def validate_readme(source_file,destination_file):
    try:
        file1 = '/home/jyoti.mikkilineni/dfo_event_4230/README'
        file2  = '/home/jyoti.mikkilineni/pw/auto/scripts/tests/PI2/data/README'

        are_files_same = filecmp.cmp(file1, file2, shallow= False)
        # print(f"Shallow comparison result: {'Identical' if are_files_same else 'Different'}")
        assert are_files_same == True , "Files are not same"
        logging.info("Files are same")
    except Exception as e:
        logging.error("Unexpected error/File Not found")
        raise e  
    except AssertionError as e:
        logging.error("Record not found")
        raise e