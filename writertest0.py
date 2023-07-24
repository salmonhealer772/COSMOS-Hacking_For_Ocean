import pandas as pd
import time
import random
file_name = "testfile1.csv"






def write_csv(colum,row,value):
    df = pd.read_csv(file_name)
    df.loc[row, colum] = value
    df.to_csv(file_name, index=False)
    del df


for i in range(100):
    write_csv("lat",i,random.randint(0,5))
    write_csv("lon",i,random.randint(0,5))
    time.sleep(2)
    print(i)