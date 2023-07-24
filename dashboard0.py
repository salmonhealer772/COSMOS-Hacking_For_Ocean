import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1920}x{1080}")
root_tk.title("dashboard")





# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)
map_widget.set_position(32.91597684204771, -117.10130323133365)


label = tkinter.Label(root_tk,text = "test101",width = 20,height = 2)

start_button = tkinter.button()

def marker_click(marker):
    map_widget.set_marker(32.91597684204771, -117.20130323133365)
    map_widget.update
    print(f"marker clicked - text: {marker.text}  position: {marker.position}")


map_widget.set_marker(32.91597684204771, -117.30130373133365, command=marker_click)
map_widget.set_marker(32.91597684204771, -117.10130323133365)





label.grid(column = 0 ,row = 0)

map_widget.grid(column = 0 ,row = 1)

root_tk.mainloop()
