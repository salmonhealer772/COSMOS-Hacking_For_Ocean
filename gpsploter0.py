import webbrowser
import gmplot  



latitudeList = [ 28.691234, 28.818390, 29.089301 ]  
longitudeList = [ 77.193802, 77.023890, 76.865211 ]  
myGmap = gmplot.GoogleMapPlotter(28.691234, 77.193802, 11)  
myGmap.scatter( latitudeList, longitudeList, '#FF0000', size = 40, marker = False )  
 



myGmap.draw( "map0.html" )  

webbrowser.open_new_tab('map0.html')