import serial
import pandas as pd


#acces spreadsheet colum "Text" row in iloc[]
df = pd.read_csv("pandasattempt1.csv", skipinitialspace = True, usecols = ["Text"])
s = df["Text"].iloc[0]
del df
#--------------------------------



#wrights to spreadsheet at colum "Text" and row "0"
df = pd.read_csv("pandasattempt1.csv")
df.loc[268, 'Text'] = 'l'
df.to_csv("pandasattempt1.csv", index=False)
print(df)
del df
#---------------------------------



while(True):
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=57600)
    ser.close
    ser.open
    #data = ser.readline()
    ser.close
    break