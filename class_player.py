#! /usr/bin/env python3
#-*- coding: utf-8 -*-


from variables import *
import pygame
from pygame.locals import *


class Player:

    def __init__(self, image, position):
        """ initialize my character with some attribtutes like position """

        self.position = position
        self.x = 0         
        self.y = 0
        self.x_pix = 0
        self.y_pix = 0
        self.inventory = []

        self.image = pygame.image.load(image)

    def generer(self, level):
        """method that generate the position of my character according to the level design
        level mark out the level_map generating by the class_map"""
        c = 1

        while c == 1:
            for cle,valeur in level.items():

                if self.position == valeur:
                    self.position = cle
                    self.y = self.position[0]
                    self.x = self.position[1]
                    self.x_pix = self.x * sprites_size
                    self.y_pix = self.y * sprites_size
                    self.position = (self.y, self.x)
                c = 2

    def moove(self, direction, level):
        """ method that generate the new position of my character
        according to the key pressed by the user
        level mark out the level_map generating by the class_map"""

        if direction == "up":# key pressed by the user
            if self.y > 0:# verifying if the next square is not out of the map
                if level[self.y - 1, self.x] != 'w':# verifying if the next square is not a wall
                    self.y -= 1 # changing my position accordig to the movement
                    self.y_pix = self.y * sprites_size # converting in pixel for the pygame.blit
                    self.position = (self.y, self.x) # updating position for the condition

        if direction == "down":
            if self.y < sprites_number_on_line - 1:
                if level[self.y + 1, self.x] != 'w':
                    self.y += 1
                    self.y_pix = self.y * sprites_size
                    self.position = (self.y, self.x)

        if direction == "left":
            if self.x > 0:
                if level[self.y, self.x - 1] != 'w':
                    self.x -= 1
                    self.x_pix = self.x * sprites_size
                    self.position = (self.y, self.x)

        if direction == "right":
            if self.x < sprites_number_on_line -1:
                if level[self.y, self.x + 1] != 'w':
                    self.x += 1
                    self.x_pix = self.x * sprites_size
                    self.position = (self.y, self.x)
