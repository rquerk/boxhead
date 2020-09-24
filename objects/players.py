import objects.movingObj as movingObj
import objects.dataStructs.rectangles as rects

import pdb

class Player(movingObj.MovingObject):
    
    # having many arguments here,
    # mybe creating an object to store
    # the values would be good
    def __init__(self, rectangle: rects.Rectangle):
        super().__init__(rectangle)
        
        self.is_visible = True
        self.cameraObj: movingObj.MovingObject
    
    # Start visibility----------------------------------------------------
    def position_onCamera(
        self, cameraObj: movingObj.MovingObject) -> (int, int, int, int):
        """helper function to keep track of things
        on the map that should be shown to the camera.
        :param Camera: or another MovingObject
        :return (): either a touple indicating the position
                    on the camera, or None,
                    if the object is not visible
                    
        gets called in game.Engine.move_player_and_camera()"""
        self.cameraObj = cameraObj
        self.x_onCamera = self.x - cameraObj.x
        self.y_onCamera = self.y - cameraObj.y
        self.rectangle = (self.x_onCamera, self.y_onCamera,
                          self.width, self.height)
        # pdb.set_trace()
        
        self.compute_visibilty()
        
        # pdb.set_trace()
        
        if self.is_visible:
            return self.rectangle
        else:
            return None
    
    # You can use x_onCamera or x_onMap,
    # second felt like a double compution.
    # But that way,
    # following functions dedend on the one above.
    def obj_is_right_from_left_screen_border(self) -> None:
        if self.x_onCamera + self.width < 0:
            self.is_visible = False
    
    def obj_is_left_from_right_screen_border(self) -> None:
        if self.x_onCamera > self.cameraObj.width:
            self.is_visible = False
        
    def obj_is_under_top_screen_border(self) -> None:
        if self.y_onCamera < 0:
            self.is_visible = False

    def obj_is_over_bottom_screen_border(self) -> None:
        if self.y_onCamera > self.cameraObj.height:
            self.is_visible = False
    
    # this function brings the four quistions
    # out of the if statement in is_visible()
    def compute_visibilty(self) -> None:
        self.is_visible = True
        self.obj_is_left_from_right_screen_border()
        self.obj_is_over_bottom_screen_border()
        self.obj_is_right_from_left_screen_border()
        self.obj_is_under_top_screen_border()
    
    def set_color_player(self, color: int) -> None:
        self.color = color
        
    # End visibility------------------------------------------------
    # having walking_rectangle[xy] very often, not so butiful
    def set_walking_rectangle(self, mapObj) -> (int, int, int, int):    
        self.walking_rectangle = mapObj.allowed_walking_area()
        
    def can_move_up(self) -> bool:
        if self.y > self.walking_rectangle[1] + self.speed:
            return True
        else: return False
    
    def can_move_left(self) -> bool:
        if self.x > (self.walking_rectangle[0] + self.speed):
            return True
        else: return False
    
    def can_move_down(self) -> bool:
        pos = self.y + self.height + self.speed
        if pos < (self.walking_rectangle[1]
                + self.walking_rectangle[3]):
            return True
        else: return False
    
    def can_move_right(self) -> bool:
        pos = self.x + self.width + self.speed 
        if pos < (self.walking_rectangle[0]
                + self.walking_rectangle[2]):
            return True
        else: return False
    
    def move_up(self) -> None:
        if self.can_move_up():
            self.y-= self.speed
    
    def move_left(self) -> None:
        if self.can_move_left():
            self.x -= self.speed
        
    def move_down(self) -> None:
        if self.can_move_down():
            self.y += self.speed
    
    def move_right(self) -> None:
        if self.can_move_right():
            self.x += self.speed
