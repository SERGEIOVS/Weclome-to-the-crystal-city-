import pygame as pg,datetime
from MapController import *
from UnitManager import *
from Items import*
from traps import *


pg.init()
pg.font.init()

import pygame as pg
import os

nickname = ''
nickname_entered = 0

if nickname_entered == 0 :
    nickname = input('enter a nickname : ')
    nickname_entered = 1


game_states_list = ['enter_name' , 'main_menu' , 'play' , 'screenshots_menu' , 'achievements_menu' , 'mini_map' , 'saving' , 'loading' ]
game_state_num = 0
game_state = game_states_list[game_state_num]
screenfilename ='txt/screen.txt'
screenfilemode = 'r'
screenfile = open (screenfilename , screenfilemode)
screenfile1 =screenfile.readlines()

for i in screenfile1:
    screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]


islands_list = []
islands_filename ='txt/islands.txt'
islands_filemode = 'r'
islands_file = open (islands_filename , islands_filemode)
islands_file1 = islands_file.readlines()

checkpoints_list = []
checkpoints_filename ='txt/checkpoints.txt'
checkpoints_filemode = 'r'
checkpoints_file = open (checkpoints_filename , checkpoints_filemode)
checkpoints_file1 = checkpoints_file.readlines()

achievements_list = []
achievements_filename ='txt/achievements.txt'
achievements_filemode = 'r'
achievements_file = open (achievements_filename , achievements_filemode)
achievements_file1 = achievements_file.readlines()

saves_list = []
saves_filename ='txt/saves/03_12_2022-15_04.txt'
saves_filemode = 'r'
saves_file = open (saves_filename , saves_filemode)
saves_file1 = saves_file.readlines()

crafts_list = []
crafts_filename ='txt/crafts/03_12_2022-15_04.txt'
crafts_filemode = 'r'
crafts_file = open (crafts_filename , crafts_filemode)
crafts_file1 = crafts_file.readlines()

bg_images = [
pg.image.load( 'wallpapers/0/0.png' ) , pg.image.load( 'wallpapers/0/1.png' ) ,
pg.image.load( 'wallpapers/0/2.png' ) , pg.image.load( 'wallpapers/0/3.png' )]


bg_num = 1
wallpapers_dir = os.listdir('wallpapers/')
wallpaper = wallpapers_dir[bg_num]

map_grid = 1
dark_level = 0
show_interface = 1
open_backpack = 1
show_hero_stats = 1

meter = 100
km = meter * 1000

map_width , map_height = meter * km , meter * km
map_scale = 1
map_size = 3
show_map = 1
show_units = 1
show_buildings = 1
show_items = 1
show_islands = 0
mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))

checkpoint_size = 50

Island_images = [ 
pg.image.load( 'Objects/islands/0/0.png' ) ,
pg.image.load( 'Objects/islands/0/0.png')]

class Background :
    def __init__(self , x , y , image) :
        self.x = x
        self.y = y
        self.image = image

for i in range( len ( islands_file1) ) :
    i =Background( islands_file1[i].split(',')[0] , islands_file1[i].split(',')[1] ,Island_images[0] )
    islands_list.append( i )

d1 = datetime.datetime.today()

d1 += datetime.timedelta( hours = 0 )

screen = pg.display.set_mode( (int( screen_width) , int(screen_height ) )   )
Game_title = 'Call of the ghost city!'
Game_version = d1.date()
update_name = 'fear in the dark'
pos = pg.mouse.get_pos()

cursor_x = pos[0]
cursor_y = pos[1]

bigfont = 30
smallfont = 15

f1 = pg.font.SysFont('arial', bigfont)

f2 = pg.font.SysFont('arial', smallfont)

show_game_title = big_font.render(   str( Game_title) , False , ( 250 , 0 , 0 ) )

show_game_version = big_font.render( 'version : ' + str( Game_version) , False , ( 250 , 0 , 0 ) )

show_update = big_font.render(  str( update_name ) , False , ( 250 , 0 , 0 ) )

for i in range(len(saves_file1)):
        i = big_font.render(  saves_file1[i] , False , ( 250 , 0 , 0 ) )
        saves_list.append(i)

for i in range(len(crafts_file1)):
        i = big_font.render(  crafts_file1[i] , False , ( 250 , 0 , 0 ) )
        crafts_list.append(i)

d1 = datetime.datetime.today()

colors = [ ( 0 , 0 , 255 ) , ( 0 , 0 , 0 ) , (250 , 0 , 0)  , (255 , 255 , 255) , (45 , 45 , 45 ) ]
BGcolor = colors[0]
minimapBGcolor = colors[0]

screen.fill(BGcolor)
pg.display.set_caption(Game_title)

minimap_location = 'right_up'
minimap_x = 15 / 2
minimap_y = 15 / 2

if minimap_location == 'left_up':
    minimap_x = 0
    minimap_y = 0

class cam :

    def __init__( self , x , y ) :
        self.rect = pg.Rect( int(camera_x) , int(camera_y) , int(screen_width) / 3 , int(screen_height) / 3 )

    def move( self , vector ) :
        self.rect[ 0 ] += vector[ 0 ]
        self.rect[ 1 ] += vector[ 1 ]

camera = cam( 0 , 0 )
vector = [ 0 , 0 ]

#show_time = big_font.render( ' Время : ' + str( d1.hour ) + " : " + str( d1.minute ) + " : " + str( d1.second ) , False , ( 250 , 0 , 0 ) )
#show_radiation = big_font.render(  str( radiation_level ) + '/' + str( max_radiation_level ) , False , ( 250 , 0 , 0 ) )
#show_cursor_location = big_font.render( 'x : ' + str( cursor_x) + 'y : ' + str(cursor_y) , False , ( 250 , 0 , 0 ) )

#print(d1)
#d1 += datetime.timedelta( hours = 0 )

#time_units = [ d1.hour , d1.minute ]

#current_time_unit = time_units[1] 