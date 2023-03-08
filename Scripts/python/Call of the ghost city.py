#system/python modules
import pygame as pg , datetime , time , random , math , sys , pyautogui , pickle ; from PIL import Image ; import os ; import logging ; #1from cv2 import log

#my custom  files
from settings import * ; from MapController import * ; from Buildings import * ; from UnitManager import * ; from Items import * ; from traps import * ;
from VihiclesManager import * ; from PathManager import * ; from musicManager import * ;
from Controls import *

pg.init()
pg.font.init()