import pygame as pg
from settings import *
from Items import *
from PIL import Image
from settings import *
from Items import *
from PIL import Image
import random
import os

pg.font.init()
item = 0
screenfilename ='txt/screen.txt'
screenfilemode = 'r'
screenfile = open (screenfilename , screenfilemode)
screenfile1 =screenfile.readlines()

hero_filename = 'txt/hero.txt'
hero_filemode = 'r'
hero_file = open (hero_filename , hero_filemode)
hero_file1 = hero_file.readlines()
hero_file.close()

for i in screenfile1:
    screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]

pistol_mags = 3
max_pistol_mags = 3
pistol_ammo = 10
pistol_ammo_full = 10

mags = pistol_mags
ammo =  pistol_ammo
ammo_full =  pistol_ammo_full

gender = 'female'
head = '1'
body = '0'
legs = '0'
boots = '0'
lefthand = 'pistol'
righthand = '0'
name = 2
state = 'idle'
turn = 'left'
animation = 0
shots = 0
hero_speed = 3
health , max_health = 10 , 10
armor , max_armor = 10 , 10

hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')

hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2



big_font = pg.font.Font( None , 30)
small_font = pg.font.Font( None , 15 )
unit_types = os.listdir('Objects/characters/')
unit_type_num = 0

show_hero_armor = big_font.render( str( armor ) + "/" +  str( max_armor ) , False , ( 250 , 0, 0 ) )
current_ammo_counter = big_font.render( str(ammo ) + "/" + str( ammo_full * mags ) , False , ( 250 , 0 , 0 ) )
show_health = big_font.render( str( health )  + "/" + str( max_health ) , False , ( 255 , 0 , 0 ) )

units_filename = 'txt/units.txt'
unitsfilemode = 'r'
units_file = open (units_filename , unitsfilemode)
units_file1 = units_file.readlines()

unitslist = []

units_categories = []

units_coords_x = []

units_coords_y = []
"""
units_images_list = [

pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),


pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png'),
pg.image.load('Objects/characters/Mutants/0/left/0.png')

]"""



class Units:
    def __init__( self , x , y , image  ) : 
        self.x = x
        self.y = y
        self.image = image

for i in units_file1:
    x , y = i.split(',')[0] , i.split(',')[1]
    units_coords_x.append(x)
    units_coords_y.append(y)

class  units1(Units):
    def __init__( self , x , y ) : 
        self.x = x
        self.y = y
        self.image = pg.image.load('Objects/characters/Mutants/0/left/0.png')
        self.color = (255,0,0)

for i in range(len(unitslist)):
    i = Units( units_coords_x[i] , units_coords_y[i] )
    unitslist.append( i )