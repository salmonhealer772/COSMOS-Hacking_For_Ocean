import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1920}x{1080}")
root_tk.title("dashboard")





# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=500, height=500, corner_radius=0)


label = tkinter.Label(root_tk,text = "test101",width = 20,height = 2)



def marker_click(marker):
    print(f"marker clicked - text: {marker.text}  position: {marker.position}")


marker_2 = map_widget.set_marker(52.516268, 13.377695, text="Brandenburger Tor", command=marker_click)
marker_3 = map_widget.set_marker(52.55, 13.4, text="52.55, 13.4")

path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.568, 13.4), (52.569, 13.35)])




label.grid(column = 0 ,row = 0)

map_widget.grid(column = 0 ,row = 1)

root_tk.mainloop()
