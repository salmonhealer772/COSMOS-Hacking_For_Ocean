#run this in termanal when it breaks on launch
# sudo chmod -R 777 /dev/ttyUSB0 



import serial
import pandas as pd
import tkinter as tk
import os


os.system("sudo chmod -R 777 /dev/ttyUSB0")

file_name = "rawdata2.csv"


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




#mainloop
row = 0
while(True):
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=57600)
    ser.close 
    ser.open
    data = ser.readline()
    ser.close
    print(data)
    print(len(data))

    write_csv("colum1",row,data)
    row = row + 1







    



