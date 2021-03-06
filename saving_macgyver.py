#! /usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Game Saving MacGyver : this game is a simple labyrinth game with conditions of victory.

The movements will be made with the keyboard : right, left, up and down arrow keys.

The conditions of victory is simple : collect the 3 items on the map
before heading to the issue guarded by Murdoc. If you don't have all the items, you loose.

Others files used : class_map, class_player, class_object, variables, level and images.
"""


import pygame
import sys
from pygame.locals import *

# import my class
from class_map import *
from class_player import *
from class_object import *
from variables import *

pygame.init()

# initialize my screen
SCREEN = pygame.display.set_mode((screen_dimension, screen_dimension))

pygame.display.set_caption(title)


continue_program = 1
continue_win = 0
continue_loose = 0

# Program's loop
while continue_program == 1:

    continue_home_page = 1

    # home_page's loop
    while continue_home_page == 1:

        home_page = pygame.image.load(HOME)
        SCREEN.blit(home_page, (0, 0))
        pygame.display.flip()


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    sys.exit()

                # creating a multi-level game :
                # F1 = level1, F2 = level2....etc
                if event.key == K_F1:
                    choice = "level/level1.txt"
                    continue_home_page = 0
                    continue_game = 1

                if event.key == K_F2:
                    choice = "level/level2.txt"
                    continue_home_page = 0
                    continue_game = 1

                if event.key == K_F3:
                    choice = "level/level3.txt"
                    continue_home_page = 0
                    continue_game = 1

                if event.key == K_F4:
                    choice = "level/level4.txt"
                    continue_home_page = 0
                    continue_game = 1
                    
    # generation of my map
    if choice != 0:
        my_level_map = Level(choice)
        my_level_map.level_generator()

        # generation of my objects
        ether = Object("images/ether.png", "ether")
        needle = Object("images/needle.png", "needle")
        tube = Object("images/tube.png", "tube")

        # get random position for my objects
        ether.generate_random_position(my_level_map.my_map)
        needle.generate_random_position(my_level_map.my_map)
        tube.generate_random_position(my_level_map.my_map)

        # display my map
        my_level_map.afficher(SCREEN)
        pygame.display.flip()

        # generation of my characters
        mcgyver = Player("images/macgyver.png", "s")
        murdoc = Player("images/murdoc.png", "o")

        # attibute position to my characters according to the level design.
        mcgyver.generate(my_level_map.my_map)
        murdoc.generate(my_level_map.my_map)

        # update my display
        SCREEN.blit(mcgyver.image, (mcgyver.x_pix, mcgyver.y_pix))
        pygame.display.flip()

    # Game's loop
    while continue_game == 1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    sys.exit()
                # condition's loop for movement of the character according to pressed key
                elif event.key == K_UP:
                    mcgyver.moove("up", my_level_map.my_map)

                elif event.key == K_DOWN:
                    mcgyver.moove("down", my_level_map.my_map)

                elif event.key == K_LEFT:
                    mcgyver.moove("left", my_level_map.my_map)

                elif event.key == K_RIGHT:
                    mcgyver.moove("right", my_level_map.my_map)

                # events according to character's position in order to collect the items.
                # if character is on the same square as an object
                # he collect the object in his inventory and
                # the object is removed from the map
                ether.collect(mcgyver, my_level_map.my_map)
                needle.collect(mcgyver, my_level_map.my_map)
                tube.collect(mcgyver, my_level_map.my_map)

                # clean the screen before updating
                my_level_map.afficher(SCREEN)

                # update character's position on the map
                SCREEN.blit(mcgyver.image, (mcgyver.x_pix, mcgyver.y_pix))
                pygame.display.update()

        # conditions of victory
        if mcgyver.position == murdoc.position:

            if ether in mcgyver.inventory and needle in mcgyver.inventory \
            and tube in mcgyver.inventory:
                continue_win = 1
                continue_game = 0
            else:
                continue_loose = 1
                continue_game = 0

    # victory loop. provide the choice to continue or quit
    while continue_win == 1:
        
        page_win = pygame.image.load(WIN).convert()
        SCREEN.blit(page_win, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    sys.exit()

                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    continue_home_page = 1
                    continue_win = 0

    # defeat loop. provide the choice to continue or quit
    while continue_loose == 1:
        
        page_loose = pygame.image.load(LOOSE).convert()
        SCREEN.blit(page_loose, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    sys.exit()

                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    continue_home_page = 1
                    continue_loose = 0
                