import pygame as pg
from PIL import Image
import os
from settings import *
import math




class Buildings :
    
    def __init__( self , x , y , image ) :
        self.x = x
        self.y = y    
        self.image = image

buildings_types = os.listdir('Objects/Buildings/' )


buildings_list = []
buildings_filename ='txt/buildings.txt'
buildings_filemode = 'r'
buildings_file = open (buildings_filename , buildings_filemode)
buildings_file1 = buildings_file.readlines()

buildings_images_list = [

pg.image.load( 'Objects/Buildings/houses/0/0.png' ) , 
pg.image.load( 'Objects/Buildings/houses/0/1.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/1.png' ) ,

pg.image.load( 'Objects/Buildings/houses/0/7.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/4.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/5.png' ) ,

pg.image.load( 'Objects/Buildings/houses/0/6.png' ),
pg.image.load( 'Objects/Buildings/houses/0/7.png' ) , 
pg.image.load( 'Objects/Buildings/houses/0/8.png' ),

pg.image.load( 'Objects/Buildings/houses/0/0.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/0.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/0.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/0.png' ),
pg.image.load( 'Objects/Buildings/houses/0/0.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/0.png' ) ,
pg.image.load( 'Objects/Buildings/houses/0/0.png' ),
pg.image.load( 'Objects/Buildings/houses/0/0.png' )

]

for i in range( len ( buildings_file1 ) ) :
    i =Buildings( buildings_file1[i].split(',')[0] , buildings_file1[i].split(',')[1] , buildings_images_list[i])

    buildings_list.append( i )

