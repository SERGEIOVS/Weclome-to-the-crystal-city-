import pygame as pg

class Vihicles :
    def __init__( self , x , y , image , title) :
        self.x = x
        self.y = y    
        self.image = image
        self.title = title

Vihicles_list = []

Vihicles_coords_x = []
Vihicles_coords_y = []

Vihicles_filename ='txt/vihicles.txt'

Vihiclesfilemode = 'r'

Vihicles_file = open (Vihicles_filename ,Vihiclesfilemode)

Vihicles_file1 = Vihicles_file.readlines()

for i in range( len ( Vihicles_file1) ) :

    Vihicles_images_list = [

pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) ,
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) ,
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) ,
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) ,
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) ,
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) , 
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) ,
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ) , 
pg.image.load( 'Objects/Vihicles/cars/1/0.png' ),
pg.image.load( 'Objects/Vihicles/cars/1/0.png' )

]

for i in Vihicles_file1:
    x , y = i.split(',')[0] , i.split(',')[1]
    Vihicles_coords_x.append(x)
    Vihicles_coords_y.append(y)

for i in range(len(Vihicles_file1)):
    i = Vihicles( Vihicles_coords_x[i] , Vihicles_coords_x[i] , Vihicles_images_list[0] , 'test' )
    Vihicles_list.append( i )