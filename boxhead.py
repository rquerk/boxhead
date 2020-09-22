import sys
import pygame

import game
#import pdb
#pdb.set_trace()

def init_game() -> game.Szenario:
    """draws first frame and returns a handle to control the screen"""
    gameObject = game.Szenario()
    gameObject.draw_startSzenario()
    return gameObject

def move(gameObject: game.Szenario, key: int):
    """a head fuction to move camera and player and update that on screen"""
    gameObject.move_player_and_camera(key)
    update(gameObject)
    
def update(gameObject: game.Szenario):
    """makes changes visible"""
    gameObject.update_screen()
    
def cross_got_clicked() -> bool:
    """use the event queue to test for quit event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def move_if_keys_are_pressed(gameObject: game.Szenario):
    """function to finf out wich keys got pressed"""
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()
        # that for loop allowes to walk diagonal...
        for key in gameObject.player.controls:
            if keys[key]:
                move(gameObject, key)

if __name__ == "__main__":
    
    #The game starts directly, no menu or so is available,
    #just drwaing the map and the player on it. map is surrounded by walls.
    
    boxhead = init_game()
    
    # main loop
    clock = pygame.time.Clock()
    FRAMERATE = 60
    done = False
    while not done:
        clock.tick(FRAMERATE)
        
        if cross_got_clicked():
            done = True
            pygame.quit()
            sys.exit()
        
        move_if_keys_are_pressed(boxhead)
