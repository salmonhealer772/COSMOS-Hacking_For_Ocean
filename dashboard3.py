import random
import tkinter as tk
import tkintermapview
import time
import pandas as pd
import datetime
from PIL import Image, ImageTk

points_on_map = 0
gps_coords = []

file_name = "latlon0.csv"

#returns value of a cell on the spreadsheet at position colum and row
def read_csv(colum,row):
    df = pd.read_csv(file_name, skipinitialspace = True, usecols = [colum])
    value = df[colum].iloc[row]
    del df
    return value
#--------------------------------


size = 100



cycletime = 500


def marker_click(obj):
    print(obj.data)
    sterminal.insert(3,obj.data)




def main():
    global points_on_map
    df = pd.read_csv(file_name, skipinitialspace = True, usecols = ["lat"])
    total_points = len(df["lat"])
    del df 

    if points_on_map < total_points:
        print(str(total_points - points_on_map))
        for i in range(total_points - points_on_map):
            gps_coords.append([read_csv("lon",points_on_map + i),read_csv("lat",points_on_map + i),str(i + points_on_map)])
            print(gps_coords[i + points_on_map][0])
            print(gps_coords[i + points_on_map][1])
            map_widget.set_marker(float(gps_coords[i + points_on_map][1]),
                                  float(gps_coords[i + points_on_map][0]),
                                  data = gps_coords[i + points_on_map][2],
                                  command = marker_click,
                                  icon = ImageTk.PhotoImage(file="image4.png")
                                  )
        map_widget.update
        
        points_on_map = total_points







    window.title("cosmos                                                                                                                                                                                 "  +  str(datetime.datetime.now()))
    window.update


    ticker.after(cycletime,main)




window = tk.Tk()

window.geometry("1920x1080")

ticker = tk.Label(window,text = "e", width = 20 , height = 1)


seedentry = tk.Entry(window,width = 30)
sterminal = tk.Listbox(window, width = 20 , height = 40,bg = "black")

map_widget = tkintermapview.TkinterMapView(window, width=500, height=500, corner_radius=0)
map_widget.set_position(32.91597684204771, -117.10130323133365)






sterminal.grid(column = 1 ,row = 0)
seedentry.grid(column = 0 ,row = 5)
map_widget.grid(column = 0 ,row = 0,rowspan = 5)




main()


window.mainloop ()