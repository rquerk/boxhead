import sys
import pygame

import game
#import pdb
#pdb.set_trace()

def init_game() -> game.Szenario:
    """we create a Szenario object
    and draw the first frame"""
    gameObject = game.Szenario()
    gameObject.draw_startSzenario()
    return gameObject

def move(gameObject: game.Szenario, key: int):
    """input is a Szenario object and a pygame key.
    pygame represents keys in certain integers"""
    gameObject.move_player_and_camera(key)
    update(gameObject)
    
def update(gameObject: game.Szenario):
    """makes changes visible"""
    gameObject.update_screen()
    
def cross_got_clicked() -> bool:
    """use the event queue to test for quit event
    return True if quit was found"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def move_if_keys_are_pressed(gameObject: game.Szenario):
    """input is a Szenario object
    the function calls move() if at
    least one of the keys,
    set to move the player and camera,
    is pressed just on funtion call"""
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()
        # that for loop allowes to walk diagonal...
        # ...we call move multiple times, it's a loop
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
