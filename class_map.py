#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from variables import *

class Level:
    
    def __init__(self, level):
        """ initialize the attribute of the map """
        self.level = level
        self.my_map = {}
        self.my_level = []
        self.my_grid = []

    def level_generator(self):
        """ method that generate :
        1/ a grid in a list with coordinates x and y in tuple as value
        2/ a level_design in a list according to the level_design file
        3/ a level_map wich is the merger of my two previous list in a new dict  """
        
        y_max = sprites_number_on_line - 1
        y = -1
        x_max = sprites_number_on_line - 1
        
        # generating the grid in a list
        while y < y_max:
            y += 1
            x = -1
            while x < x_max:
                x += 1
                my_coordinates = (y, x)
                self.my_grid.append(my_coordinates)
        
        # generating the level design with the sprites in a list
        with open(self.level, "r") as level_file:
	        for line in level_file:
		        for sprite in line:
			        if sprite != '\n' and sprite != ' ':
				        self.my_level.append(sprite)

        # merging the two list in a dict. coordinates and sprites are associated together.
        self.my_map = dict(zip(self.my_grid,self.my_level))


    def afficher(self, screen):
        ''' method that display the map according to the dict generated previously.
        read the sequence in the dict and blit an image at the good coordinates 
        according to the sprites '''

        floor = pygame.image.load("images/floor(40x40).png").convert()
        wall = pygame.image.load("images/wall.png").convert()
        starting = pygame.image.load("images/start.png").convert()
        out = pygame.image.load("images/out.png").convert()
        ether_image = pygame.image.load("images/ether.png").convert_alpha()
        needle_image = pygame.image.load("images/needle.png").convert_alpha()
        tube_image = pygame.image.load("images/tube.png").convert_alpha()

        # loop that read the sequence in my map dictionnary
        # 1/ for a sprite read in value in the dict
        # 2 /generate an image of the sprite at the coordinate indicated in the key of the dict
        for key,value in self.my_map.items():
        
            if value == "w":# 1/
                screen.blit(wall, (key[1] * sprites_size, key[0] * sprites_size))# 2/
            if value == "f":
                screen.blit(floor, (key[1] * sprites_size, key[0] * sprites_size))
            if value == "s":
                screen.blit(starting, (key[1] * sprites_size, key[0] * sprites_size))
            if value == "o":
                screen.blit(out, (key[1] * sprites_size, key[0] * sprites_size))
            if value == "ether":
                screen.blit(ether_image, (key[1] * sprites_size, key[0] * sprites_size))
            if value == "needle":
                screen.blit(needle_image, (key[1] * sprites_size, key[0] * sprites_size))
            if value == "tube":
                screen.blit(tube_image, (key[1] * sprites_size, key[0] * sprites_size))