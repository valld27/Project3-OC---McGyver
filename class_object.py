import pygame
from pygame.locals import *
import random
from variables import *

class Object:
    
    def __init__(self, image, nom):

        self.x_obj = 0         
        self.y_obj = 0
        self.x_pix = 0
        self.y_pix = 0
        self.position = (self.x_pix, self.y_pix)
        self.nom = nom

        self.image = pygame.image.load(image)
     
    def generate_random_position(self, my_level):

        self.x_obj = random.randint(0,sprites_number_on_line - 1)
        self.y_obj = random.randint(0,sprites_number_on_line -1)
        self.position = self.y_obj, self.x_obj
        self.x_pix = self.x_obj * sprites_size
        self.y_pix = self.y_obj * sprites_size
        
        

        while my_level[self.position] == 'w' or my_level[self.position] == 'o' or my_level[self.position] == 's':

            self.x_obj = random.randint(0,sprites_number_on_line - 1)
            self.y_obj = random.randint(0,sprites_number_on_line -1)
            self.position = self.y_obj, self.x_obj
            self.x_pix = self.x_obj * sprites_size
            self.y_pix = self.y_obj * sprites_size
            
        my_level[self.position] = self.nom

        
        