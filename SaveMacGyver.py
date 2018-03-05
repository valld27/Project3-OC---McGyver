#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from class_map import *
from class_player import *
from class_object import *
from variables import *

pygame.init()

screen = pygame.display.set_mode((screen_dimension, screen_dimension))


continue_game = 1

while continue_game == 1:

    #afficher page d'accueil du jeu à définir

    continue_home_page = 1

    while continue_home_page == 1:

        accueil = pygame.image.load("images/macgyver.png")
        screen.blit(accueil, (300, 300))
        pygame.display.flip()


        for event in pygame.event.get():

            if event.type == QUIT:
                continue_home_page = 0
                continue_game = 0

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    continue_home_page = 0
                    continue_game = 0

                if event.key == K_F1:
                    choice = "level/level1.txt"
                    continue_home_page = 0
                    continue_jeu = 1

                    if choice != 0:
                        my_level_map = Level(choice)
                        my_level_map.level_generator()
                        my_level_map.afficher(screen)

                        obj1 = Object("images/start.png")
                        obj2 = Object("images/start.png")
                        obj3 = Object("images/start.png")

                        obj1.generate_random_position(my_level_map.my_map)
                        obj2.generate_random_position(my_level_map.my_map)
                        obj3.generate_random_position(my_level_map.my_map)

                        screen.blit(obj1.image, (obj1.x_pix, obj1.y_pix))
                        screen.blit(obj2.image, (obj2.x_pix, obj2.y_pix))
                        screen.blit(obj3.image, (obj3.x_pix, obj3.y_pix))
                        pygame.display.flip()

                        mcgyver = Player("images/macgyver.png", "s")
                        murdoc = Player("images/murdoc.png", "o")

                        mcgyver.generer(my_level_map.my_map)
                        murdoc.generer(my_level_map.my_map)

    while continue_jeu == 1:

        for event in pygame.event.get():

            if event.type == QUIT:
                continue_game = 0
                continue_jeu = 0

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    continue_jeu = 0

                elif event.key == K_UP:
                    mcgyver.moove("up", my_level_map.my_map)
                elif event.key == K_DOWN:
                    mcgyver.moove("down", my_level_map.my_map)
                elif event.key == K_LEFT:
                    mcgyver.moove("left", my_level_map.my_map)
                elif event.key == K_RIGHT:
                    mcgyver.moove("right", my_level_map.my_map)

                my_level_map.afficher(screen)
                pygame.display.flip()

                screen.blit(mcgyver.image, (mcgyver.x_pix, mcgyver.y_pix))
                screen.blit(murdoc.image, (murdoc.x_pix, murdoc.y_pix))
                screen.blit(obj1.image, (obj1.x_pix, obj1.y_pix))
                screen.blit(obj2.image, (obj2.x_pix, obj2.y_pix))
                screen.blit(obj3.image, (obj3.x_pix, obj3.y_pix))
                pygame.display.flip()
                pygame.time.delay(100)


            if mcgyver.position == murdoc.position:
                continue_game = 0
                continue_jeu = 0
