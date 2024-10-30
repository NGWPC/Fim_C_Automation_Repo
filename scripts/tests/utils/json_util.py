import json
from deepdiff import DeepDiff
import logging

def validate_json(source_file,destination_file):

    try:
        with open(source_file, 'r') as source_json_file , open(destination_file, 'r') as destination_json_file:
            json1 = json.load(source_json_file)
            json2 = json.load(destination_json_file)

            diff = DeepDiff(json1,json2, ignore_order=True)
            assert not diff, f"JSON Files are different: {diff}"
            logging.info(f"JSON Files are same: {source_file}")
    except Exception as e:
        logging.error("Assertion error for JSON files")
        raise e
