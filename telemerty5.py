#run this in termanal when it breaks on launch
# sudo chmod -R 777 /dev/ttyUSB0 

import serial
import pandas as pd
import tkinter as tk
import os


os.system("sudo chmod -R 777 /dev/ttyUSB0")

file_name = "testfile3.csv"


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
    #handshake
   # ser.open
  #  ser.write(bytes("check\n","UTF-8"))
    #ser.close

    #converts to string and cleans
    try:
        data = str(data,"UTF-8")
    except:
        print("bad ):")
    data = data[:-1]

    if data[0:2] == "S1":
        data = data[2:]
        len_of_colum_name = 0
        len_of_information = 0
        i = 0
        



    #parcese and commits data


        while True:
            if data[i] == "@":
                    
                while True:
                    if data[i + len_of_colum_name] == "#":
                        break
                    len_of_colum_name = len_of_colum_name + 1
                        



                colum_name = str(data[i + 1:i + int(len_of_colum_name)])
                    
                i = i + len_of_colum_name
                
                len_of_colum_name = 0


            if data[i] == "#":
                while True:
                    if data[i + len_of_information] == "$":
                        break
                    len_of_information = len_of_information + 1

                information = str(data[i + 1:i + int(len_of_information)])
                    
                i = i + len_of_information + 1
                
                len_of_information = 0

            print(colum_name)
            print(row)
            print(information)
            write_csv(colum_name,row,information)


            if data[i] == "%":
                row = row + 1
                break
            if i >= (len(data)-1):
                    
                break


    #-------------------------------------






    



