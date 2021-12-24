import os
import glob
import pandas as pd
os.chdir("medical")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

for f in all_filenames:
    df = pd.read_csv(f)
    new_row = pd.DataFrame({'-DOCSTART-':'-DOCSTART-', 'O':'O'},index =[0])
        # simply concatenate both dataframes
    df = pd.concat([new_row, df]).reset_index(drop = True)
    df.to_csv(f, index=False)
        
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv
combined_csv.to_csv( "combined_csv.csv", encoding='utf-8-sig')




