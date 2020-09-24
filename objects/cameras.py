import objects.movingObj

import pdb

# made a own camera class because pygame
# writes they dont recomend thier own...?
class Camera(objects.movingObj.MovingObject):
    
    # too many actually used default values
    def __init__(self, rectangle: objects.dataStructs.rectangles.Rectangle):
        super().__init__(rectangle)
        
        self.new_rectangles = []
        self.old_rectangles = []
        # TODO:
        # same two lists used here and in map
        # planing to exclude stuff to a parent class
        
    def set_camera_speed(self, speed: int) -> None:
        self.speed = speed
    
    def set_movement_rectangle(
            self, width: int = 1500, height: int = 700) -> None:
        """Set a invisible rectangle
        that triggers the camera to move,
        if the player crosses its borders."""
        
        if width > self.width or height > self.height:
            error_msg = ["rectangle to limit player movement", 
                        "without camera movement is too big.", 
                        "objects.py set_movement_rectangle()"]
            raise RuntimeError(error_msg)
        
        x_pos = (self.width - width)/2
        y_pos = (self.height - height)/2
        self.movement_rectangle = (x_pos, y_pos, width, height)
        
    def move_up(self) -> None:
        self.y -= self.speed
    
    def move_left(self) -> None:
        self.x -= self.speed
        
    def move_right(self) -> None:
        self.x += self.speed
    
    def move_down(self) -> None:
        self.y += self.speed
