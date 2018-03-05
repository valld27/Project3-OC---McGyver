#-*- coding: utf-8 -*-
from variables import *
import pygame
from pygame.locals import *


class Player:

    def __init__(self, image, position):

        self.position = position
        self.x = 0         
        self.y = 0
        self.x_pix = 0
        self.y_pix = 0

        self.image = pygame.image.load(image)

    def generer(self, fichier):

        c = 1

        while c == 1:
            for cle,valeur in fichier.items():

                if self.position == valeur:
                    self.position = cle
                    self.y = self.position[0]
                    self.x = self.position[1]
                    self.x_pix = self.x * sprites_size
                    self.y_pix = self.y * sprites_size
                    self.position = (self.y, self.x)
                c = 2

    def moove(self, direction, fichier):

        if direction == "up":
            if fichier[self.y - 1, self.x] != 'm':
                self.y -= 1
                self.y_pix = self.y * sprites_size
                self.position = (self.y, self.x)

        if direction == "down":
            if fichier[self.y + 1, self.x] != 'm':
                self.y += 1
                self.y_pix = self.y * sprites_size
                self.position = (self.y, self.x)

        if direction == "left":
            if fichier[self.y, self.x - 1] != 'm':
                self.x -= 1
                self.x_pix = self.x * sprites_size
                self.position = (self.y, self.x)

        if direction == "right":
            if fichier[self.y, self.x + 1] != 'm':
                self.x += 1
                self.x_pix = self.x * sprites_size
                self.position = (self.y, self.x)

        