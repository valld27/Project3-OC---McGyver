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
        self.inventory = []

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
            if self.y > 0:
                if fichier[self.y - 1, self.x] != 'w':
                    self.y -= 1
                    self.y_pix = self.y * sprites_size
                    self.position = (self.y, self.x)

        if direction == "down":
            if self.y < sprites_number_on_line - 1:
                if fichier[self.y + 1, self.x] != 'w':
                    self.y += 1
                    self.y_pix = self.y * sprites_size
                    self.position = (self.y, self.x)

        if direction == "left":
            if self.x > 0:
                if fichier[self.y, self.x - 1] != 'w':
                    self.x -= 1
                    self.x_pix = self.x * sprites_size
                    self.position = (self.y, self.x)

        if direction == "right":
            if self.x < sprites_number_on_line -1:
                if fichier[self.y, self.x + 1] != 'w':
                    self.x += 1
                    self.x_pix = self.x * sprites_size
                    self.position = (self.y, self.x)

        