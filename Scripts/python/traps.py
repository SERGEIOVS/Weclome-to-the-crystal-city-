import pygame as pg
class Traps:
    def __init__( self , x , y , image ) :
        self.x = x
        self.y = y
        self.image= image


traps = []

traps_categories = []

traps_coords_x = []

traps_coords_y = []

traps_filename ='txt/traps.txt'
traps_filemode = 'r'
traps_file = open (traps_filename , traps_filemode)
traps_file1 = traps_file.readlines()


for i in traps_file1:
    x , y,category = i.split(',')[0] , i.split(',')[1] , i.split(',')[2]
    traps_coords_x.append(x)
    traps_coords_y.append(y)
    traps_categories.append(category)


traps_images_list = [

pg.image.load( 'Objects/Traps/spikes/aluminum_spikes/spikes.png' ),
pg.image.load( 'Objects/Traps/spikes/aluminum_spikes/spikes.png' )

]

for i in range( len ( traps_file1 ) ) :
    i = Traps( traps_file1[ i ] , traps_file1[ i ] ,traps_images_list[i])
    traps.append(i)