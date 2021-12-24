# -*- coding: utf-8 -*-
import csv
import numpy as np
import pandas as pd

tensortext = "['O', 'O', 'B-PER', 'I-PER', 'I-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-LOC', 'O', 'B-LOC', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O', 'O', 'B-MISC', 'I-MISC', 'O', 'B-MISC', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-PER', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-LOC', 'I-LOC', 'O', 'I-ORG', 'O', 'O', 'B-LOC', 'I-LOC', 'O', 'I-LOC', 'O', 'B-LOC', 'O', 'O', 'O', 'O', 'O', 'O', '[SEP]', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']"
tensortext = tensortext.replace("‘","'")
tensortext = tensortext.replace("’","'")

tensor = eval(tensortext)

with open('TESTresultNER.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in tensor:
        writer.writerows([[i]])
        
#df = pd.DataFrame(t_np) #convert to a dataframe
#df.to_csv("resultNER",index=False) #save to file

#Then, to reload:
#data = pd.read_csv("resultNER.csv")

#data2 = pd.read_csv("combined_csv.csv")

#data = pd.concat([data, data2])

#data.to_csv("NERresultsJOINED.csv")
