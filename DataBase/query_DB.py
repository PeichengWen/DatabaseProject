

import pandas as pd
import numpy
import os
import random




saveFile=open('ID_query_record.csv','w')




for i in range(1,1000):
    number = random.randint(1,100000)
    query="SELECT ID FROM [dbo].[Full_DB_Data$] where ID = %d"%(number)
    saveFile.write(query)
    saveFile.write('\n')



saveFile.close()
