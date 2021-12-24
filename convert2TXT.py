import os
import glob
import pandas as pd
os.chdir("medical")
extension = 'csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#for f in all_filenames:
    #df = pd.read_csv(f)
    #new_row = pd.DataFrame({'-DOCSTART-':'-DOCSTART-', 'O':'O'},index =[0])
        # simply concatenate both dataframes
    #df = pd.concat([new_row, df]).reset_index(drop = True)
    #df.to_csv(f, index=False)
        
#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
#combined_csv.to_csv( "combined_csv.csv", encoding='utf-8-sig')

import csv
import re
csv_file = "processed.csv"
txt_file = "processed.txt"
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        
    my_output_file.close()

with open(txt_file, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('/"', '"')

# Write the file out again
with open(txt_file, 'w') as file:
  file.write(filedata)

