import pygame as pg

class Items:
    def __init__( self , x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image= image

items_list = []
items_filename ='txt/items.txt'

itemsfilemode = 'r'

items_file = open (items_filename , itemsfilemode)

items_file1 = items_file.readlines()

items_images_list = [

pg.image.load( 'Objects\Items/weapons/ammo/pistol_ammo.png' ) ,

pg.image.load( 'Objects/Items/weapons/ammo/rifle_ammo.png' ) ,

pg.image.load( 'Objects/Items/tools/toolboxes/0.png' ) ,

pg.image.load( 'Objects/Items/accums/car_battery.png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,

pg.image.load( 'Objects\Items/food/canned_food/консервы(рыба).png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,

pg.image.load( 'Objects\Items/food/canned_food/сухпай_походный.png' ) ,

pg.image.load( 'Objects/Items/drinks/бутылка_воды.png' ) ,

pg.image.load( 'Objects/Items/lighting/flashlights/white/flashlight_turned_right.png' ) ,


pg.image.load( 'Objects/Items/tools/axes/0/axe_turned_right.png' ) ,

pg.image.load( 'Objects/Items/weapons/rifles/sniper_rifle.png' ) ,

pg.image.load( 'Objects/Items/weapons/mg/0.png' ),

pg.image.load( 'Objects/Items/weapons/ammo/pistol_ammo.png' ) ,

pg.image.load( 'Objects/Items/weapons/ammo/rifle_ammo.png' ) ,

pg.image.load( 'Objects/Items/tools/toolboxes/0.png' ) ,

pg.image.load( 'Objects/Items/accums/car_battery.png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,

pg.image.load( 'Objects\Items/food/canned_food/консервы(рыба).png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters/gas_lighter.png' ) ,


pg.image.load( 'Objects/Items/food/canned_food/сухпай_походный.png' ) ,

pg.image.load( 'Objects/Items/drinks/бутылка_воды.png' ) ,

pg.image.load( 'Objects/Items/lighting/flashlights/white/flashlight_turned_right.png' ) ,

pg.image.load( 'Objects/Items/tools/axes/0/axe_turned_right.png' ) ,

pg.image.load( 'Objects/Items/weapons/rifles/sniper_rifle.png' ) ,

pg.image.load( 'Objects/Items/weapons/mg/0.png' )

]

for i in range( len ( items_file1 ) ) :
    i = Items( items_file1[i].split(',')[0] , items_file1[i].split(',')[1] , 50 , 50 , items_images_list[ i ] ) 
    items_list.append( i )