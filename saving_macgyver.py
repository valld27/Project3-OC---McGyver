#-*- coding: utf-8 -*-

"""
Game Saving MacGyver : this game is a simple labyrinth game with conditions of victory.

The movements will be made with the keyboard : right, left, up and down arrow keys.

The conditions of victory is simple : collect the 3 items on the map 
before heading to the issue guarded by Murdoc. If you don't have all the items, you loose.

Others files used : class_map, class_player, class_object, variables, level and images.
"""


import pygame, sys
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

# Program's loop
while continue_program == 1:

    continue_home_page = 1

    # home_page's loop
    while continue_home_page == 1:

        accueil = pygame.image.load("images/accueil.png")
        SCREEN.blit(accueil, (0, 0))
        pygame.display.flip()


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    sys.exit()

                #In anticipation of creating a multi-level game :
                # F1 = level1, F2 = level2....etc
                if event.key == K_F1:
                    choice = "level/level1.txt"
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
        mcgyver.generer(my_level_map.my_map)
        murdoc.generer(my_level_map.my_map)

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
                if mcgyver.position == ether.position:
                    mcgyver.inventory.append(ether)
                    my_level_map.my_map[ether.position] = "f"

                elif mcgyver.position == needle.position:
                    mcgyver.inventory.append(needle)
                    my_level_map.my_map[needle.position] = "f"

                elif mcgyver.position == tube.position:
                    mcgyver.inventory.append(tube)
                    my_level_map.my_map[tube.position] = "f"

                # clean the screen before updating 
                my_level_map.afficher(SCREEN)
                pygame.display.flip()

                # update character's position on the map
                SCREEN.blit(mcgyver.image, (mcgyver.x_pix, mcgyver.y_pix))
                pygame.display.flip()

        # conditions of victory
        if mcgyver.position == murdoc.position:

            if ether in mcgyver.inventory and needle in mcgyver.inventory \
            and tube in mcgyver.inventory:
                continue_home_page = 1
                continue_game = 0
            else :
                sys.exit()
                