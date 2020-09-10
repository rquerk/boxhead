import sys
import pygame

import game
#import pdb
#pdb.set_trace()

if __name__ == "__main__":
    
    #The game starts directly, no menu or so is available,
    #just drwaing the map and the player on it. map is surrounded by walls.
    
    boxhead = game.Szenario()
    boxhead.draw_startSzenario()
    
    # main loop
    clock = pygame.time.Clock()
    framerate = 120
    done = False
    while not done:
        clock.tick(framerate)
        
        # first we use the event queue
        for event in pygame.event.get():
            if event.type not in boxhead.allowedTypes:
                raise TypeError(
                    "found invalid event type in pygames event queue")
            
            elif event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
        
        # and here we check wich keys get pressed just now
        if pygame.key.get_focused():
            keys = pygame.key.get_pressed()
            
            for i in range(len(boxhead.player.controls)):
                if keys[boxhead.player.controls[i]]:
                    boxhead.move_player_and_camera(boxhead.player.controls[i])
            #rotate needs to call some init funcs again
            #if keys[pygame.K_e]:
            #    boxhead.player.rotate()
            boxhead.update_screen()
