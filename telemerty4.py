import serial
import pandas as pd


file_name = "testfile1.csv"


#returns value of a cell on the spreadsheet at position colum and row
def read_csv(colum,row):
    df = pd.read_csv(file_name, skipinitialspace = True, usecols = [colum])
    value = df["Text"].iloc[row]
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


while(True):
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=57600)
    ser.close
    ser.open
    data = ser.readline()
    ser.close
    write_csv("value1",0,data)
    break