

import pandas as pd
import numpy
import os
import random




saveFile=open('Insert_query_record.csv','w')




for i in range(1,1000):
    number = random.randint(1,100000)
    text= random.randint(1,100)
    query="INSERT INTO [dbo].[Full_DB_Data$] VALUES (%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text,text)
    saveFile.write(query)
    saveFile.write('\n')



saveFile.close()
