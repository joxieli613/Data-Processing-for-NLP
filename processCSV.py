import os
import glob
import pandas as pd
os.chdir("medical")
extension = 'csv'

import csv
import re

def SepWord(word):
    if word == "-DOCSTART-":
        return word
    parts = []
    for match in re.finditer(r'[^.,?!;:\s]+|[.,?!;:"]', word):
        parts.append(match.group())
    return parts

def FixQuotes(a):#this function takes in a list
    if a == "-DOCSTART-":
        return a
    else:
        if '\u201c' in a:
            a = a.replace('\u201c','"')
            print("left" + a)
        
        if '\u201d' in a:
            a = a.replace('\u201d','"')
            print("right" + a)
        
        if '"' in a:
            a = a.replace('"',' /" ')
            print(a)
        return a


df = pd.read_csv("combined_csv.csv")



df['-DOCSTART-'] = df['-DOCSTART-'].apply(FixQuotes)
df['-DOCSTART-'] = df['-DOCSTART-'].apply(SepWord)


        
df.rename(columns={'-DOCSTART-':'DOCSTART'}, inplace=True)

df.assign(DOCSTART=df.DOCSTART.str.split(",")).explode('DOCSTART')
df = df.apply(pd.Series.explode).reset_index(drop=True)
#df.loc[(df.DOCSTART == '/"'),'DOCSTART']= '\"'

df.to_csv("processed.csv")

        
        
    
