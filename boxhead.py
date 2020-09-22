import sys
import pygame

import game
#import pdb
#pdb.set_trace()

def init_game() -> game.Szenario:
    """draws first frame and returns a handle to control the screen"""
    gameSzenario = game.Szenario()
    gameSzenario.draw_startSzenario()
    return gameSzenario

def move(gameSzenario: game.Szenario, key: int):
    """a head fuction to move camera and player and update that on screen"""
    gameSzenario.move_player_and_camera(key)
    update(gameSzenario)
    
def update(gameSzenario: game.Szenario):
    """makes changes visible"""
    gameSzenario.update_screen()
    
def cross_got_clicked() -> bool:
    """use the event queue to test for quit event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def do_action_denending_on_pressed_keys(gameSzenario: game.Szenario):
    """function to find out wich keys got pressed
    and trigger required action"""
    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()
        # that for loop allowes to walk diagonal
        for key in gameSzenario.player.controls:
            if keys[key]:
                move(gameSzenario, key)

if __name__ == "__main__":
    
    #The game starts directly, no menu or so is available,
    #just drwaing the map and the player on it. map is surrounded by walls.
    
    gameSzenario = init_game()
    
    # main loop
    clock = pygame.time.Clock()
    FRAMERATE = 60
    done = False
    while not done:
        clock.tick(FRAMERATE)
        
        if cross_got_clicked():     # handling the quit event
            done = True             # extra here, is because
            pygame.quit()           # i want to set the "done"
            sys.exit()              # boolean to true
        
        do_action_denending_on_pressed_keys(gameSzenario)
