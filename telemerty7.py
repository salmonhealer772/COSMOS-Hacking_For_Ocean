#run this in termanal when it breaks on launch
# sudo chmod -R 777 /dev/ttyUSB0 

import serial
import pandas as pd
import tkinter as tk
import os


os.system("sudo chmod -R 777 /dev/ttyUSB0")

file_name = "latlon0.csv"


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
    #data = b"S1@-011.1111111111111111@-022.2222222222222222%"
    print(data)
    try:
        data = str(data,"UTF-8")
        print(len(data) == 46)
        if True:
            if data[0:2] == "S1":
                data = data[2:]
                if data[0:1] == "@":
                    data = data[1:]
                    try:
                        print(data[0:20])
                        float(data[0:20])
                        write_csv("lat",row,data[0:20])
                        data = data[21:]
                        
                        if data[0:1] == "@":
                            data = data[1:]
                            try:
                                data[0:20].isnumeric
                                write_csv("lon",row,data[0:20])
                                data = data[20:]
                            except:
                                print( data[0:20] + "not acceptecd")
                        else:
                            print(data[0:1])
                            print("second @ error")

                    except:
                        print(data[0:20] + "not accepted")
                else:
                    print("first @ error")
            else:
                print("S1 error")
        else:
            print("wrong len")

    except:
        print("I hate louis1234")
    
    row = row + 1










