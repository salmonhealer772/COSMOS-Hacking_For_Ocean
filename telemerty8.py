#11111111111111111122222222222222222233333

32.881729205357686, -117.24854724922503

3288172920535768611724854724922503

#gps lat 18 numbers add 180 15 decimal
#gps lon 18 numbers add 180 15 decimal
#temperature 5 2 decimal
#ph 4 2 decimal
#orp 3 digits add 500 
#tds 3 digits 
#dissolved oxygen 3 digits 1 decimal 


#run this in termanal when it breaks on launch
# sudo chmod -R 777 /dev/ttyUSB0 



import serial
import pandas as pd
import tkinter as tk
import os


os.system("sudo chmod -R 777 /dev/ttyUSB0")

file_name = "rawdata2.csv"

nlist = [[18,3,180],[18,3,180],[5,3,0],[4,2,0],[3,0,500],[3,0,0],[3,2,0]]


#returns value of a cell on the spreadsheet at position colum and row
def read_csv(colum,row):
    df = pd.read_csv(file_name, skipinitialspace = True, usecols = [colum])
    value = df[colum].iloc[row]
    del df
    return value
#--------------------------------


#writes to spreadsheet at colum and row and replaces the the current value with value
def write_csv(colum,row,value):
    df = pd.read_csv(file_name)
    df.loc[row, colum] = value
    df.to_csv(file_name, index=False)
    del df
#---------------------------------

def fileter(data,n):
    if len(data) != n:
        return False
    if data.isnumeric():
        return data
    return False


#mainloop
c = 0
while(True):
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=57600)
    ser.close 
    ser.open
    data = ser.readline()
    ser.close
    


    try:
        data = str(data,"UTF-8")
    except:
        print("death")
    data = data[:-1]
    print(data)
    
    data = fileter(data,nlist[c % len(nlist)][0])
    if data == False:
        print('die')
    else:
        print(data)


    
    write_csv("colum1",c,data)
    c = c + 1








    



