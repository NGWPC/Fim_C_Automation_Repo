import pandas as pd
import os

def preprocess_df(df):
         return df.applymap(lambda x: x.strip() if isinstance(x,str) else x)

def test_extract_csv_data(csv_file,output_csv_file):
   try:
      pd.set_option('display.max_columns',None)
      df_output = pd.read_csv(csv_file, nrows=1)
      df_output = preprocess_df(df_output)

      df_refer = pd.read_csv(output_csv_file, nrows=1)
      df_refer = preprocess_df(df_refer)
      
      assert os.path.exists(csv_file) == True , "Directory does not exist"
      if df_output.empty:
         print("File is empty")
      else:
         records = len(df_output)
         print("Number of records in the file:")
         print(records)
      is_equal = df_output.equals(df_refer)
      print(is_equal)
   except pd.errors.EmptyDataError:
     print("CSV file is empty")
   except FileNotFounderror:
     print("File was not found")
