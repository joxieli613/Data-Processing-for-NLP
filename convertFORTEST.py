import csv
import pandas as pd 
# readinag given csv file
# and creating dataframe
txt_file = 'Legalpredict.txt'
with open(txt_file, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('"', '/"')

# Write the file out again
with open(txt_file, 'w') as file:
  file.write(filedata)

dataframe1 = pd.read_csv(txt_file, delimiter=' ')
# storing this dataframe in a csv file
dataframe1.to_csv('LegalLabeled.csv',
                  index = None)
