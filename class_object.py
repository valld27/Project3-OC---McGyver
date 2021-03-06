#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import random
from variables import *

class Object:
    
    def __init__(self, image, nom):
        """ intitialize the objects"""

        self.x_obj = 0         
        self.y_obj = 0
        self.x_pix = 0
        self.y_pix = 0
        self.position = (self.x_pix, self.y_pix)
        self.nom = nom

        self.image = pygame.image.load(image)
     
    def generate_random_position(self, my_level):
        """ method that attribute random position to my objects """

        # attribute random position with randint
        self.x_obj = random.randint(0,sprites_number_on_line - 1)
        self.y_obj = random.randint(0,sprites_number_on_line -1)
        self.position = self.y_obj, self.x_obj
        self.x_pix = self.x_obj * sprites_size
        self.y_pix = self.y_obj * sprites_size
        
        
        # loop that permit to avoid attributing a position which
        # is the same as a wall, the starting or the issue 
        while my_level[self.position] == 'w' or my_level[self.position] == 'o' \
        or my_level[self.position] == 's':

            self.x_obj = random.randint(0,sprites_number_on_line - 1)
            self.y_obj = random.randint(0,sprites_number_on_line -1)
            self.position = self.y_obj, self.x_obj
            self.x_pix = self.x_obj * sprites_size
            self.y_pix = self.y_obj * sprites_size
            
        my_level[self.position] = self.nom

    def collect(self, character, level):

        if character.position == self.position:
            character.inventory.append(self)
            level[self.position] = "f"

