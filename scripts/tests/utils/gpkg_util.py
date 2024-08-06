import geopandas
import logging

def compare_gpkgs(source_file,destination_file):
    source_gdf = geopandas.read_file(source_file)
    destination_gdf = geopandas.read_file(destination_file)

    try:
        assert source_gdf.equals(destination_gdf),"Dataframes not equal"
        logging.info(f"Both gpkg files are same: {source_file} and {destination_file}")
    except AssertionError as e:
        # print(f"\n {str(e)} \n")
        logging.error(f"Both gpkg files are not same: {source_file} and {destination_file}")
        raise e

