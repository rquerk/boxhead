import coordinates

# in these two classes there are too many actually used default values
# i will start making all this more dynamic and depending on one thing
# like the window size

class Player(coordinates.MovingObject):
    
    def __init__(
            self, x: int = 400, y: int = 500, width: int = 30, height: int = 10):
        super().__init__(x = x, y = y)
        self.width = width
        self.height = height
        self.is_visible = True
       
    
    # Start visibility----------------------------------------------------
    def get_area(self) -> ():
        player_area = (self.x_onMap, self.y_onMap, self.width, self.height)
        return player_area
    
    def position_onCamera(self, cameraObj):
        """helper function to keep track of things
        on the map that should be shown to the camera.
        :param Camera: or another MovingObject
        :return (): either a touple indicating the position
                    on the camera, or None,
                    if the object is not visible
        """
        self.x_onCamera = self.x_onMap - cameraObj.x_onMap
        self.y_onCamera = self.y_onMap - cameraObj.y_onMap
        self.rectangle = (self.x_onCamera, self.y_onCamera,
                          self.width, self.height)
        if self.is_visible(cameraObj):
            return self.rectangle
        else:
            return None
    
    # You can use x_onCamera or x_onMap,
    # second felt like a double compution.
    # But that way,
    # following functions dedend on the one above.
    def obj_is_right_from_left_screen_border(self, cameraObj) -> None:
        if self.x_onCamera + self.width < 0:
            self.is_visible = False
    
    def obj_is_left_from_right_screen_border(self, cameraObj) -> None:
        if self.x_onCamera > cameraObj.width:
            self.is_visible = False
        
    def obj_is_under_top_screen_border(self, cameraObj) -> None:
        if self.y_onCamera < 0:
            self.is_visible = False

    def obj_is_over_bottom_screen_border(self, cameraObj) -> None:
        if self.y_onCamera > cameraObj.height:
            self.is_visible = False
    
    # this function brings the four quistions
    # out of the if statement in is_visible()
    def compute_visibilty(self) -> None:
        is_visible = True
        obj_is_left_from_right_screen_border()
        obj_is_over_bottom_screen_border()
        obj_is_right_from_left_screen_border
        obj_is_under_top_screen_border
    
    def is_visible(self, cameraObj) -> bool:
        self.compute_visibilty()
        if self.is_visible:
            return True
        else:
            return False
    
    def set_color_player(self, color: int) -> None:
        self.color = color
        
    # End visibility------------------------------------------------
        
    def set_walking_rectangle(self, mapObj) -> (int, int, int, int):    
        self.walking_rectangle = mapObj.allowed_walking_area()
        
    def can_move_up(self) -> bool:
        if self.y_onMap > self.walking_rectangle[1] + self.speed:
            return True
        else: return False
    
    def can_move_left(self) -> bool:
        if self.x_onMap > (self.walking_rectangle[0] + self.speed):
            return True
        else: return False
    
    def can_move_down(self) -> bool:
        pos = self.y_onMap + self.height + self.speed
        if pos < (self.walking_rectangle[1]
                + self.walking_rectangle[3]):
            return True
        else: return False
    
    def can_move_right(self) -> bool:
        pos = self.x_onMap + self.width + self.speed 
        if pos < (self.walking_rectangle[0]
                + self.walking_rectangle[2]):
            return True
        else: return False
    
    def move_up(self) -> None:
        if self.can_move_up():
            self.y_onMap -= self.speed
    
    def move_left(self) -> None:
        if self.can_move_left():
            self.x_onMap -= self.speed
        
    def move_down(self) -> None:
        if self.can_move_down():
            self.y_onMap += self.speed
    
    def move_right(self) -> None:
        if self.can_move_right():
            self.x_onMap += self.speed

# made a own camera class because pygame
# writes they dont recomend thier own...?
class Camera(coordinates.MovingObject):

    def __init__(
            self, x: int = 0, y: int = 0, width: int = 1800, height: int = 950):
        super().__init__(x = x, y = y)
        self.width: int = width     # could exclude width and height too
        self.height: int = height
        
        self.size: (int, int) = (width, height)
        # TODO:
        # same two lists used here and in map
        # planing to exclude stuff to a parent class
        self.new_rectangles = []
        self.old_rectangles = []
        
    def set_camera_speed(self, speed: int) -> None:
        self.speed = speed
    
    def set_movement_rectangle(
            self, width: int = 1500, height: int = 700) -> None:
        if width > self.width or height > self.height:
            error_msg = ["rectangle to limit player movement", 
                        "without camera movement is too big.", 
                        "objects.py set_movement_rectangle()"]
            raise RuntimeError(error_msg)
        x_pos = (self.width - width)/2
        y_pos = (self.height - height)/2
        self.movement_rectangle = (x_pos, y_pos, width, height)
        
    def compute_area_onMap(self) -> (int, int, int, int):
        camera_area = (self.x_onMap, self.y_onMap, self.width, self.height)
        return camera_area
        
    def move_up(self) -> None:
        self.y_onMap -= self.speed
    
    def move_left(self) -> None:
        self.x_onMap -= self.speed
        
    def move_right(self) -> None:
        self.x_onMap += self.speed
    
    def move_down(self) -> None:
        self.y_onMap += self.speed
    
    
