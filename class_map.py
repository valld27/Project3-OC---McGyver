#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from variables import *

class Level:
    
    def __init__(self, level):
        self.level = level
        self.my_map = {}
        self.my_level = []
        self.my_grid = []

    def level_generator(self):

        # création de la liste contenant les coordonnées de ma map
        y_max = sprites_number_on_line - 1
        y = -1
        x_max = sprites_number_on_line - 1
        
        
        while y < y_max:
            y += 1
            x = -1
            while x < x_max:
                x += 1
                my_coordinates = (y, x)
                self.my_grid.append(my_coordinates)
        
        # creation de la liste contenant la definition de mon niveau (sprites)
        with open(self.level, "r") as level_file:
	        for line in level_file:
		        for sprite in line:
			        if sprite != '\n' and sprite != ' ':
				        self.my_level.append(sprite)

        #creation de mon dict contenant les coordonnées associés à mes sprites
        self.my_map = dict(zip(self.my_grid,self.my_level))


    def afficher(self, screen):
        '''fonction permanttant d'afficher et de rafraichir la fenêtre de jeu'''

        floor = pygame.image.load("images/floor(40x40).png").convert()
        wall = pygame.image.load("images/wall.png").convert()
        starting = pygame.image.load("images/start.png").convert()
        out = pygame.image.load("images/out.png").convert()
        ether_image = pygame.image.load("images/ether.png").convert_alpha()
        needle_image = pygame.image.load("images/needle.png").convert_alpha()
        tube_image = pygame.image.load("images/tube.png").convert_alpha()


        for key,value in self.my_map.items():
        
            if value == "w":
                screen.blit(wall, (key[1] * sprites_size, key[0] * sprites_size))
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

            pygame.display.flip()