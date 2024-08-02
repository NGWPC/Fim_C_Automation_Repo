import geopandas
def compare_gpkgs(source_file,destination_file):
    source_gdf = geopandas.read_file(source_file)
    destination_gdf = geopandas.read_file(destination_file)

    try:
        assert source_gdf.equals(destination_gdf),"Dataframes not equal"
        # print(f"the two df are {'equal' if are_equal else 'not equal'}.")
        # We only care about failures when FIM output directories are compared,
        # however if only two .gpkg files are compared, print success.
        # if verbose:
        #     print("\n Both files are the same. \n")

    except AssertionError as e:
        print(f"\n {str(e)} \n")
        raise e
        # print("  The following files failed assert_geodataframe_equal: ")
        # print(f"    {file1.rsplit('/', 1)[-1]} ")
