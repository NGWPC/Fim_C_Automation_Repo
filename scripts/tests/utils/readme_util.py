import filecmp
import logging

def validate_readme(source_file,destination_file):
    try:
        files_same = filecmp.cmp(source_file, destination_file, shallow= False)
        # print(f"Shallow comparison result: {'Identical' if are_files_same else 'Different'}")
        assert files_same == True , "README Files are not same"
        logging.info(f"README Files are same: {source_file}")
    except Exception as e:
        logging.error("Unexpected error/File Not found for README file")
        raise e  
    except AssertionError as e:
        logging.error("Assertion error for README files")
        raise e
