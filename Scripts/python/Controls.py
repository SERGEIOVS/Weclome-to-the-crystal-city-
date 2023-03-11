import pygame as pg
from settings import *
from PIL import Image
from UnitManager import *
import logging
from VihiclesManager import *
import pyautogui
from Buildings import *
import math
from PathManager import *

clock = pg.time.Clock()
quest_surf_color = colors[1]

#land level
ground = 0
floor = 0

step_sound = pg.mixer.Sound('Audio/sounds/knoks/knok_1.mp3')
rifle_sound = pg.mixer.Sound('Audio/sounds/firegun/auto_firing(3 times)_1.mp3')
spawn_sound = pg.mixer.Sound('Audio/sounds/spawn/bell.mp3')
scream_sound = pg.mixer.Sound('Audio/sounds/screams/far scream.mp3')
death_sound = pg.mixer.Sound('Audio/sounds/death/bell.mp3')

dx , dy = 1 , -1

#music
soundtracks = os.listdir('Audio/enviroment/')
#music = 'dead.mp3'
switch_music = 1
music = soundtracks[switch_music]

pg.mixer.music.load('Audio/enviroment/' + str(music))

minimap_border_offset = 10

bg_images = [

pg.image.load( 'wallpapers/0/0.png' ) , pg.image.load( 'wallpapers/0/1.png' ) ,
pg.image.load( 'wallpapers/0/2.png' ) , pg.image.load( 'wallpapers/0/3.png' )

]
anim_wait = 0
mags = 3

map_scale = 1
map_size = 3
show_map = 0
show_units = 0
show_buildings = 1
show_items = 1
show_interface = 1
open_backpack = 1

map_scale1 = 1

bg_num = 1
wallpapers = os.listdir('wallpapers/')
wallpaper = wallpapers[bg_num]

dark_level = 0
show_hero_stats = 1

mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
quests_surf = pg.Surface(( 600 , 500 ))
dark_surf = pg.Surface(( int(screen_width) , int(screen_height) ))
inteface_surf = pg.Surface(( 200 , 150 ))

hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
angle = 2
volume_levels = 10


ColorsCoords_x_1 = []
ColorsCoords_y_1 = []

ColorsCoords_x_2 = []
ColorsCoords_y_2 = []

for i in range(volume_levels) :
    i += 1 
    i = ColorsCoords_x_1.append( i * 100) 
    i = ColorsCoords_y_1.append(400)

for i in range(5) :
    i += 1 
    i = ColorsCoords_x_2.append( i * 100) 
    i = ColorsCoords_y_2.append(500)

def make_screenshot() :
    screenshots = 1
    screenshot = pyautogui.screenshot()

    for i in range(screenshots):
        screenshot.save( 'screenshots/' + str(d1) + str(i) + '.png' )

def start():
    if game_state == 'saving' and nickname_entered == 1 :
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )

        for i in range(len(saves_file1)):
                pg.draw.rect(screen , (45 , 45 , 45) , ( int(screen_width) /  2 - 100 , int(screen_height) / 10 + i * 40 , 90  , bigfont ))
                screen.blit(saves_list[i] , ( int(screen_width) /  2 - 70 , int(screen_height) / 10 + i * 40 , 100 , bigfont ) )
    
    if game_state == 'crafting' and nickname_entered == 1 :
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )

        for i in range(len(crafts_file1)):
                pg.draw.rect(screen , (45 , 45 , 45) , ( int(screen_width) /  2 - 100 , int(screen_height) / 10 + i * 40 , 300  , bigfont))
                screen.blit(crafts_list[i] , ( int(screen_width) /  2 - 70 , int(screen_height) / 10 + i * 40 , 100 , bigfont ) )

    if game_state == 'main_menu' and nickname_entered == 1 :
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        screen.blit( bg_images[bg_num] , ( 0 , 0 ) )
        screen.blit(show_game_title , ( 300 , 10 ) )
        screen.blit(show_game_version , ( 10 , 575 ) )
        screen.blit( show_update  , ( 600 , 10 ))

        for i in range(6):
            pg.draw.rect(screen , (45 , 45 , 45) , ( int(screen_width) /  10 , int(screen_height) / 10 + i * 40 ,int(screen_width) - 200 , 30 ))

    if game_state == 'play':        
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )
        
        
        

        if ground == 1:
            for i in range( len ( islands_file1 ) ) :
                screen.blit( Island_images[ 0 ] , ( -camera.rect[ 0 ] + int(islands_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(islands_file1[i].split(',')[1] ) ) )

            for i in range( len ( Vihicles_file1 ) ) :
                screen.blit( Vihicles_images_list[0] , ( -camera.rect[ 0 ] + int(Vihicles_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(Vihicles_file1[i].split(',')[1]) ) ) 
        
            for i in range( len(buildings_file1 )) :
                screen.blit( buildings_list[i], ( -camera.rect[ 0 ] + int(buildings_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(buildings_file1[ i ].split(',')[1] ) ))

        for i in range( len ( roads_file1 ) ) :
            screen.blit( roads_images[ 0 ] , ( -camera.rect[ 0 ] + int(roads_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[1] ) ) )

        for i in range(len(units_file1)):
            screen.blit( units_images_list[i], ( -camera.rect[ 0 ] + int(units_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(units_file1[i].split(',')[1])  ) )
        
        #for i in range(len(unitslist)):
        #   #screen.blit( units_images_list[i] , ( -camera.rect[ 0 ] + int(units_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(units_file1[i].split(',')[1])  ) )
        #    pg.image.load('Objects/Characters/' + str(unit_types[i]) + '/0/left/0.png'),


        inteface_surf.set_alpha(100)
        screen.blit( hero_image , ( hero_x / map_scale1 , hero_y/ map_scale1 ) )
        
        dark_surf.set_alpha(dark_level)
        
        screen.blit(dark_surf , ( 0 , 0 ) ) 
        #screen.blit(inteface_surf , ( 0 , 200 ) )

        if show_map == 1:
            mini_map_surf.fill((minimapBGcolor))
            quests_surf.fill((quest_surf_color))


            for i in range( len ( items_file1 ) ) :
                if show_items == 1:
                    pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_file1[i].split(',')[0]) / (100 * map_scale) , int(items_file1[i].split(',')[1]) / (100 * map_scale) , 1 / map_scale , 1/ map_scale ))

            for i in range( len ( Vihicles_file1 ) ) :
                pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(Vihicles_file1[i].split(',')[0]) / (100 * map_scale) , int(Vihicles_file1[i].split(',')[1]) / (100 * map_scale) , 5 / map_scale , 3 / map_scale ))

            for i in range( len ( buildings_file1 ) ) :
                if show_buildings == 1:
                    pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) ,  10 / map_scale, 10 / map_scale  ))

            for i in range( len ( roads_file1 ) ) :
                    pg.draw.rect(mini_map_surf , (45,45,45) , (int(roads_file1[ i ].split(',')[0]) / (100 * map_scale) , int(roads_file1[ i ].split(',')[1]) / (100 * map_scale) ,  10 / map_scale, 10 / map_scale  ))

            for i in range( len ( units_file1 ) ) :
                pg.draw.rect(mini_map_surf , (255,0,0) , ( int(units_file1[i].split(',')[0]) / (100 * map_scale) , int(units_file1[i].split(',')[1]) / (100 * map_scale) , 1 / map_scale , 1 / map_scale))
                
            hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , ( minimap_border_offset   + camera.rect[0] / (100 * map_scale) , minimap_border_offset + camera.rect[1] / (100 * map_scale)) ,1 / map_scale )
            screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )
            pg.draw.rect(screen , ( 255 , 0 , 0 ) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset  , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)
            
        inteface_surf.blit(show_health , ( 10 , 500 ) )
        inteface_surf.blit(current_ammo_counter  , ( 10 , 550 ) )
        inteface_surf.blit(show_hero_armor , ( 10 , 450 ) )


herojump , herojumpcounter = False , 10 # запрет на прыжок , высота прыжка
jump_height = 6
FPS = 60
fps_1 = 4
max_dark_level = 180
run = True

logging.info( msg = 'GAME STARTED!' )

while run :
    
    if animation <= max_dark_level:
        dark_level += 0.1
        clock.tick(FPS/fps_1)

    if animation >= max_dark_level :
        dark_level += 0.1
        clock.tick(FPS/fps_1)

    vector = [ 0 , 0 ]
    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION :
            pos = pg.mouse.get_pos()


            if game_state == 'main_menu':
                cursor = pg.image.load( 'Interface/icons/cursor/select.png' ) 
                mouse_visible = True
                screen.blit( cursor , ( pos[ 0 ] , pos[ 1 ] ) )
                

            if  pos[ 0 ] >= hero_x and game_state == 'play':
                turn = 'right'
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )
            
            if  pos[ 0 ] <= hero_x  and game_state == 'play':
                turn = 'left'
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                heroimage = Image.open(hero)
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

            pg.display.update()


            pressed = pg.mouse.get_pressed()
            pos = pg.mouse.get_pos()
            
        if event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1 and int(ammo) > 0 and game_state == 'play':
                ammo -= 1
                gun_shot = pg.mixer.Sound( 'Audio/sounds/firegun/single_1.mp3' ) ; gun_shot.play()
                show_health = big_font.render( str( health )  + "/" + str( max_health ) , False , colors[2] )
                show_hero_armor = big_font.render( str( armor ) + "/" +  str( max_armor ) , False , colors[2] )
                current_ammo_counter = big_font.render( str( ammo ) + "/" + str( ammo_full * mags ) , False , colors[2] )
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

            if event.button == 1 and int(ammo) <= 1 and game_state == 'play':
                ammo = 0 ; current_ammo_counter = big_font.render( str( ammo ) + '/' + str( ammo_full * mags ) , False , colors[2] ) 
                no_ammo = pg.mixer.Sound( 'Audio/sounds/firegun/no_ammo.wav' )
                no_ammo.play()
    
        if event.type == pg.QUIT:
            run = False



    keys = pg.key.get_pressed()

    if keys[pg.K_a] and game_state == 'play' and camera.rect[0] >= 0:
            
            angle += 1
            state = 'go'
            turn = 'left'
            hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
            hero_speed = 4
            vector[ 0 ] -= hero_speed
            if animation <= len(hero_animations_dir) -1:
                clock.tick(FPS/fps_1)
                animation += 1
                #print(animation)
                hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

            if animation >= len(hero_animations_dir) -1 :
                animation = 0
                state = 'go'
                turn = 'left'
                hero_animations_dir = os.listdir('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/')
                hero_speed = 4
                clock.tick(FPS/fps_1)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

    if keys[pg.K_a] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[0] >= 0:
            state = 'go'
            turn = 'left'
            hero_speed = 4
            vector[ 0 ] -= hero_speed
            if animation <= len(hero_animations_dir) -1:
                clock.tick(100)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

            if animation >= len(hero_animations_dir) -1 :
                animation = 0
                state = 'go'
                turn = 'left'
                hero_speed = 4
                clock.tick(100)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

    if keys[pg.K_w] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[1] >= 0:
        vector[ 1 ] -= hero_speed
        hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
        heroimage = Image.open( hero )
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
        #step_sound.play()

    if keys[pg.K_s] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[1] >= 0 :
        vector[ 1 ] += hero_speed
        hero_image =  pg.image.load( hero )
        heroimage = Image.open(hero)
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
        #step_sound.play()
    
    if keys[pg.K_e] and game_state == 'play' and camera.rect[1] >= 0 :
        BGcolor = (0,0,0)
        screen.fill( (BGcolor) )
        spawn_sound.play()
        ground = 0

    if keys[pg.K_q] and game_state == 'play' and camera.rect[1] >= 0 and ground == 0 :
        BGcolor = (0,0,255)
        screen.fill( (BGcolor) )
        spawn_sound.play()
        ground = 1

    if keys[pg.K_d] and game_state == 'play' and camera.rect[0] <= map_width:
            angle -= 1
            state = 'go'
            turn = 'right'
            hero_speed = 4
            vector[ 0 ] += hero_speed

            """            if animation <= len(hero_animations_dir) -1:
                state = 'go'
                turn = 'right'
                clock.tick(20)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

            if animation >= len(hero_animations_dir) -1 :
                state = 'go'
                turn = 'right'
                hero_speed = 4
                animation = 0
                vector[ 0 ] += hero_speed
                clock.tick(20)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )"""

    if keys[pg.K_d] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[0] <= map_width :
            turn = 'right'
            state = 'run'
            hero_speed = 4
            vector[ 0 ] += hero_speed
            
            if animation <= len(hero_animations_dir) -1:
                state = 'run'
                turn = 'right'
                clock.tick(20)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )
            
            if animation >= len(hero_animations_dir) -1 :
                state = 'run'
                turn = 'right'
                hero_speed = 4
                animation = 0
                clock.tick(20)
                animation += 1
                hero ='Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_image = pg.image.load( 'Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                heroimage = Image.open('Objects/Characters/Hero/' + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                screen.blit( hero_image , ( hero_x , hero_y ) )

    if not( herojump ) :
        if keys[pg.K_w] and game_state == 'play' and camera.rect[1] >= 0:
            vector[ 1 ] -= hero_speed
            hero_image =  pg.image.load( hero )
            heroimage = Image.open(hero)
            hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
  
        if keys[pg.K_s] and game_state == 'play' and camera.rect[1] >= 0:
            vector[ 1 ] += hero_speed
            
            hero_image =  pg.image.load( hero )
            heroimage = Image.open(hero)
            hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

        if keys[pg.K_SPACE] and game_state == 'play':
            herojump = True #можно прыгать

        ##  Если игрок ходил
        if vector != [ 0 , 0 ] and game_state == 'play':
            camera.move( vector )

    else:
        if herojumpcounter >= -jump_height :
            if herojumpcounter < 0 :
                
                hero_y += ( herojumpcounter ** 2 ) / 2
                clock.tick(FPS/2)

            else:
                hero_y-= ( herojumpcounter ** 2 ) / 2
            herojumpcounter -= 1
            clock.tick(FPS/2)

        else:
            herojump = False
            herojumpcounter = jump_height

    if keys [pg.K_r]and game_state == 'play':
        hero_status = 'reload'
        if hero_status =='reload' and mags >= 1:
            #print('mags was ' , mags)
            reloadsound = pg.mixer.Sound( 'Audio/sounds/firegun/reload.mp3' ) ; 
            reloadsound.play()
            mags -= 1
            #print('mags now : ' , mags)
            ammo = ammo_full  ; current_ammo_counter = big_font.render( str( ammo ) + '/' + str( ammo * mags ) , False , colors[2] )
            hero_filename = 'txt/hero.txt'
            hero_filemode = 'w'
            hero_file = open (hero_filename , hero_filemode)
            hero_file.write(str(ammo))
            hero_file.close()
            clock.tick(FPS/fps_1)
            
            pg.display.update()
            
            
    if keys [pg.K_F5] :
        make_screenshot() ; logging.info( msg = 'SCREENSHOT SAVED!')

    #save game and quit
    if keys [pg.K_F12] :
        camerafilemode = 'w'
        camera_file = open (screenfilename , camerafilemode)
        camera_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  )
        camera_file.close()
        logging.info(msg = 'GAME SAVED!' ) ; pg.quit() ; logging.info(msg = 'QUIT GAME!' )
    
    if keys [pg.K_F9] :
        screenfilemode = 'r' ; screenfile = open (screenfilename , screenfilemode)
        camera_file.close() ; logging.info(msg = 'GAME LOADED!' )


    #save game 
    if keys [pg.K_F5] :
        screenfilemode = 'w' ; screenfile = open (screenfilename , screenfilemode)
        screenfile.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  )
        camera_file.close() ; logging.info(msg = 'GAME SAVED!' )

    if keys [pg.K_p] :
        game_state = 'play'
        #pg.mixer.music.play()
    
    if keys [pg.K_s] and game_state == 'main_menu' :
        game_state = 'saving'
        #pg.mixer.music.play()
    
    if keys [pg.K_k] and game_state == 'main_menu' :
        game_state = 'crafting'
        #pg.mixer.music.play()

    if keys [pg.K_b] :
        open_backpack = 1

    if keys [pg.K_b]  and keys[pg.K_LSHIFT] :
        open_backpack = 0
    
    if keys [pg.K_ESCAPE] :
        bg_images[ random.randint( 0 , len(bg_images) - 1 ) ]
        game_state = 'main_menu'

    if keys [pg.K_UP] :
        show_map = 1
        for i in range(int( int(screen_width) / (meter/10))) :
            pg.draw.line(mini_map_surf , ( 0 , 0 , 0 ) , [i * meter/ 10 , 0  ] , [i * meter /10, int(screen_width)     ] , 1 )
        
        for i in range(int( int(screen_height) / (meter/10))) :
            pg.draw.line(mini_map_surf , ( 0 , 0 , 0 ) , [0 , i * meter /10  ] , [int(screen_width), i * meter  /10   ] , 1 )
        
    
    if keys [pg.K_DOWN] :
        show_map = 0


    if keys [pg.K_KP_7] :
        minimap_location = 'left_up'
        if minimap_location == 'left_up':
            minimap_x = 0
            minimap_y = 0
        
    if keys [pg.K_KP_9] :
        minimap_location = 'right_up'
        if minimap_location == 'right_up':
            minimap_x = int(screen_width) - int(screen_width) / 3
            minimap_y = 0
    
    if keys [pg.K_KP_3] :
        minimap_location = 'right_down'
        if minimap_location == 'right_down':
            minimap_x = int(screen_width) - int(screen_width) / 3
            minimap_y = int(screen_height) - int(screen_height) / 3
    
    if keys [pg.K_KP_1] :
        minimap_location = 'left_down'
        if minimap_location == 'left_down':
            minimap_x = 0
            minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_8] :
        minimap_location = 'left_up'
        if minimap_location == 'left_up':
            minimap_x = 0
            minimap_y = 0
        
    if keys [pg.K_KP_6] :
        minimap_location = 'right_up'
        if minimap_location == 'right_up':
            minimap_x = int(screen_width) - int(screen_width) / 3
            minimap_y = 0
    
    if keys [pg.K_KP_4] :
        minimap_location = 'right_down'
        if minimap_location == 'right_down':
            minimap_x = int(screen_width) - int(screen_width) / 3
            minimap_y = int(screen_height) - int(screen_height) / 3
    
    if keys [pg.K_KP_2] :
        minimap_location = 'left_down'
        if minimap_location == 'left_down':
            minimap_x = 0
            minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_5] :
        minimap_location = 'left_down'
        if minimap_location == 'left_down':
            minimap_x = 0
            minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_PLUS]:
        mini_map_surf.fill((minimapBGcolor))
        map_scale -= 0.1
        if show_map == 1:

            for i in range( len ( items_file1 ) ) :
                if show_items == 1:
                    pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_file1[i].split(',')[0]) / (100 * map_scale) , int(items_file1[i].split(',')[1]) / (100 * map_scale) , 1 / map_scale , 1/ map_scale ))

            for i in range( len ( Vihicles_file1 ) ) :
                pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(Vihicles_file1[i].split(',')[0]) / (100 * map_scale) , int(Vihicles_file1[i].split(',')[1]) / (100 * map_scale) , 5 / map_scale , 3 / map_scale ))

            for i in range( len ( buildings_file1 ) ) :
                if show_buildings == 1:
                    pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) ,  10 / map_scale, 10 / map_scale  ))

            hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , ( minimap_border_offset   + camera.rect[0] / (100 * map_scale) , minimap_border_offset + camera.rect[1] / (100 * map_scale)) ,1 / map_scale )
            
            for i in range( len ( units_file1 ) ) :
                if show_units == 1:
                    pg.draw.circle(mini_map_surf , ( 255 ,100 , 0 ) ,  (400 ,400) , 1 / map_scale )
            screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )

            pg.draw.rect(screen , ( 255 , 0 , 0 ) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset  , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)

        
    if keys [pg.K_KP_MINUS]:
        mini_map_surf.fill((minimapBGcolor))
        map_scale += 0.1
        if show_map == 1:
            for i in range( len ( islands_file1 ) ) :
                pg.draw.rect(mini_map_surf , (100 , 50 , 0) , (minimap_border_offset + int(islands_file1[ i ].split(',')[0]) / (100 * map_scale) ,  minimap_border_offset + int(islands_file1[ i ].split(',')[1]) / (100 * map_scale) ,  80 / map_scale ,  80 / map_scale ))
            
            for i in range( len ( items_file1 ) ) :
                if show_items == 1:
                    pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_file1[i].split(',')[0]) / (100 * map_scale) , int(items_file1[i].split(',')[1]) / (100 * map_scale) , 1 / map_scale , 1/ map_scale ))

            for i in range( len ( Vihicles_file1 ) ) :
                pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(Vihicles_file1[i].split(',')[0]) / (100 * map_scale) , int(Vihicles_file1[i].split(',')[1]) / (100 * map_scale) , 5 / map_scale , 3 / map_scale ))

            for i in range( len ( buildings_file1 ) ) :
                if show_buildings == 1:
                    pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) ,  10 / map_scale, 10 / map_scale  ))

            hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , ( minimap_border_offset   + camera.rect[0] / (100 * map_scale) , minimap_border_offset + camera.rect[1] / (100 * map_scale)) ,1 / map_scale )
            screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )
            pg.draw.rect(screen , ( 255 , 0 , 0 ) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset  , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)
    
    if keys [pg.K_ESCAPE]  and open_backpack == 1:
        open_backpack  = 0
    
    if keys [pg.K_1] :
        switch_music = 0
        music = soundtracks[switch_music]
        pg.mixer.music.load('Audio/enviroment/' + str(music))
        pg.mixer.music.play()

    if keys [pg.K_2] :
        switch_music = 1
        music = soundtracks[switch_music]
        pg.mixer.music.load('Audio/enviroment/' + str(music))
        pg.mixer.music.play()
    

    screen.fill( (BGcolor) )
    start()

    if game_state == 'play' and game_state == 'saving':
                
                mouse_visible = False
                cursor = pg.image.load( 'Interface\icons\курсор/crosshair.png' ) 
                screen.blit( cursor , ( pos[ 0 ] -5 , pos[ 1 ]  -5 ) )

    pg.display.update()