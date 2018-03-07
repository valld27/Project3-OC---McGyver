#-*- coding: utf-8 -*-
import pygame
from pygame.locals import *

from class_map import *
from class_player import *
from class_object import *
from variables import *

pygame.init()

screen = pygame.display.set_mode((screen_dimension, screen_dimension))

pygame.display.set_caption(title)


continue_game = 1

while continue_game == 1:

    continue_home_page = 1

    while continue_home_page == 1:

        accueil = pygame.image.load("images/accueil.png")
        screen.blit(accueil, (0, 0))
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

        ether = Object("images/ether.png", "ether")
        needle = Object("images/needle.png", "needle")
        tube = Object("images/tube.png", "tube")

        ether.generate_random_position(my_level_map.my_map)
        needle.generate_random_position(my_level_map.my_map)
        tube.generate_random_position(my_level_map.my_map)

        my_level_map.afficher(screen)
        pygame.display.flip()

        mcgyver = Player("images/macgyver.png", "s")
        murdoc = Player("images/murdoc.png", "o")

        mcgyver.generer(my_level_map.my_map)
        murdoc.generer(my_level_map.my_map)

        screen.blit(mcgyver.image, (mcgyver.x_pix, mcgyver.y_pix))
        pygame.display.flip()


    while continue_jeu == 1:

        for event in pygame.event.get():

            if event.type == QUIT:
                continue_game = 0
                continue_jeu = 0

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    continue_jeu = 0
                    continue_game = 0

                elif event.key == K_UP:
                    mcgyver.moove("up", my_level_map.my_map)
                elif event.key == K_DOWN:
                    mcgyver.moove("down", my_level_map.my_map)
                elif event.key == K_LEFT:
                    mcgyver.moove("left", my_level_map.my_map)
                elif event.key == K_RIGHT:
                    mcgyver.moove("right", my_level_map.my_map)

                if mcgyver.position == ether.position:
                    mcgyver.inventory.append(ether)
                    my_level_map.my_map[ether.position] = "f"
                elif mcgyver.position == needle.position:
                    mcgyver.inventory.append(needle)
                    my_level_map.my_map[needle.position] = "f"
                elif mcgyver.position == tube.position:
                    mcgyver.inventory.append(tube)
                    my_level_map.my_map[tube.position] = "f"

                my_level_map.afficher(screen)
                pygame.display.flip()
                screen.blit(mcgyver.image, (mcgyver.x_pix, mcgyver.y_pix))
                pygame.display.flip()

        if mcgyver.position == murdoc.position:

            if ether in mcgyver.inventory and needle in mcgyver.inventory and tube in mcgyver.inventory:
                continue_home_page = 1
                continue_jeu = 0
            else :
                continue_game = 0
                continue_jeu = 0