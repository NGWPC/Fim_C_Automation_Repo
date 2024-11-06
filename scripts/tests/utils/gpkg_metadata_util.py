import geopandas
import logging

def compare_gpkgs_metadata(source_file,fields):
    source_gdf = geopandas.read_file(source_file)
    # destination_gdf = geopandas.read_file(destination_file)

    try:
        field_names = source_gdf.columns.tolist()
        print(field_names)
        for field in fields:
            assert field in field_names
            logging.info(f"{field} is present in {field_names}")
    except AssertionError as e:
        logging.error("Expected fields not available")
        raise e
