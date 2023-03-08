import pygame as pg
import math
from UnitManager import *
import logging


logfilename= 'logs/log.txt'

mylevel = logging.INFO

myformat = '%(asctime)s - %(levelname)s - %(message)s'

my1=logging.basicConfig(filename = logfilename ,level = mylevel , format= myformat)



class Paths():
    def __init__(self,x1,x2,y1,y2,lenght,need):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.lenght = lenght
        self.need = need

x1list = []
x2list = []
y1list = []
y2list = []

lenghts = []

for i in range(len(x1list)):
    i = Paths(x1list[i],x2list[i],y1list[i],y2list[i],math.sqrt( ((x2list[i]-x1list[i])**2) +  ((y2list[i]-y1list[i])**2)     ) , math.sqrt( ((x2list[i]-x1list[i])**2) +  ((y2list[i]-y1list[i])**2)     ) )
    lenghts.append(i.lenght)
    
    if i.lenght == i.need:
        print('len = ' , str(i.need))
    else:
        print('не равно!')



class Roads :
    def __init__( self , x , y , image) :
        self.x = x
        self.y = y    
        self.image = image

roads_list = []

roads_coords_x = []
roads_coords_y = []

roads_filename ='txt/roads.txt'

roadsfilemode = 'r'

roads_file = open (roads_filename , roadsfilemode)

roads_file1 = roads_file.readlines()

for i in range( len ( roads_file1) ) :
    
    roads_images = [

pg.image.load( 'Objects/roads/0.png' ) ,
pg.image.load( 'Objects/roads/0.png' ) ,
pg.image.load( 'Objects/roads/0.png' ) ,
pg.image.load( 'Objects/roads/0.png' ) ,
pg.image.load( 'Objects/roads/0.png' ) 

]

for i in roads_file1:
    x , y = i.split(',')[0] , i.split(',')[1]
    roads_coords_x.append(x)
    roads_coords_y.append(y)

for i in range(len(roads_file1)):
    i = Roads( roads_coords_x[i] , roads_coords_x[i] , roads_images[0])
    roads_list.append( i )