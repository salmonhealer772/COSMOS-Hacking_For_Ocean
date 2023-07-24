import tkinter
import tkintermapview
import time
import pandas as pd

import tkintermapview


file_name = "testfile1.csv"

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1920}x{1080}")
root_tk.title("dashboard")


#returns value of a cell on the spreadsheet at position colum and row
def read_csv(colum,row):
    df = pd.read_csv(file_name, skipinitialspace = True, usecols = [colum])
    value = df[colum].iloc[row]
    del df
    return value
#--------------------------------



# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)
map_widget.set_position(32.91597684204771, -117.10130323133365)


label = tkinter.Label(root_tk,text = "test101",width = 20,height = 2)



def marker_click(marker):
    map_widget.set_marker(32.91597684204771, -117.20130323133365)
    map_widget.update
    print(f"marker clicked - text: {marker.text}  position: {marker.position}")


map_widget.set_marker(32.91597684204771, -117.30130373133365, command=marker_click)
map_widget.set_marker(32.91597684204771, -117.10130323133365)






label.grid(column = 0 ,row = 0)

map_widget.grid(column = 0 ,row = 1)

root_tk.mainloop()




