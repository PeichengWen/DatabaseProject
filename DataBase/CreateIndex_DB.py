

import pandas as pd
import numpy
import os
import random




saveFile=open('Create_Index.csv','w')




for i in range(1,21):
    
    query = "create nonclustered index Index_%d_colums on  [dbo].[Full_DB_Data$](C%d)"%(i,i)
    saveFile.write(query)
    saveFile.write('\n')



saveFile.close()
