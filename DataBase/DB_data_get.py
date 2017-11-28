import pandas as pd
import os
import random


df = pd.DataFrame(columns = ["ID","Name","Result","Class"])
for i in range(1,100001):
    df=df.append({"ID": i,
                  "Name": str("n%d"%(i)),
                  "Result" : random.randint(0,100),
                  "Class": random.choice(['A','B','C','D','E','F','G']),
                  "C1":random.randint(0,1000),
                  "C2":random.randint(0,1000),
                  "C3":random.randint(0,1000),
                  "C4":random.randint(0,1000),
                  "C5":random.randint(0,1000),
                  "C6":random.randint(0,1000),
                  "C7":random.randint(0,1000),
                  "C8":random.randint(0,1000),
                  "C9":random.randint(0,1000),
                  "C10":random.randint(0,1000),
                  "C11":random.randint(0,1000),
                  "C12":random.randint(0,1000),
                  "C13":random.randint(0,1000),
                  "C14":random.randint(0,1000),
                  "C15":random.randint(0,1000),
                  "C16":random.randint(0,1000),
                  "C17":random.randint(0,1000),
                  "C18":random.randint(0,1000),
                  "C19":random.randint(0,1000),
                  "C20":random.randint(0,1000),
                  },ignore_index = True)

df.to_csv('Full_DB_Data.csv')
    
    
