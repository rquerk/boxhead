import coordinates

class Player(coordinates.MovingObject):
    
    def __init__(self, x: int = 50, y: int = 50, speed: int = 3, width: int = 30, height: int = 10):
        super().__init__(x = x, y = y)
        self.speed = speed
        self.width = width
        self.height = height
       
    def get_area(self) -> ():
        player_area = (self.x_onMap, self.y_onMap, self.width, self.height)
        return player_area
        
    def position_onCamera(self, cameraObj):
        self.x_onCamera = self.x_onMap - cameraObj.x_onMap
        self.y_onCamera = self.y_onMap - cameraObj.y_onMap
        self.rectangle = (self.x_onCamera, self.y_onCamera,
                          self.width, self.height)
        return (self.rectangle)
    
    def set_walking_rectangle(self, mapObj) -> (int, int, int, int):    
        self.walking_rectangle = mapObj.allowed_walking_area()
        
    def set_color_player(self, color):
        self.color = color
        
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
    
    def move_up(self):
        if self.can_move_up():
            self.y_onMap -= self.speed
    
    def move_left(self):
        if self.can_move_left():
            self.x_onMap -= self.speed
        
    def move_down(self):
        if self.can_move_down():
            self.y_onMap += self.speed
    
    def move_right(self):
        if self.can_move_right():
            self.x_onMap += self.speed
            
    def rotate(self):
        tmp = self.width
        self.width = self.height
        self.height = tmp


class Camera(coordinates.MovingObject):

    def __init__(self, x: int = 0, y: int = 0, width: int = 1800, height: int = 950):
        super().__init__(x = x, y = y)
        self.width: int = width
        self.height: int = height
        
        self.size: (int, int) = (width, height)
        
        self.old_rectangles = []
        self.new_rectangles = []
        
    def set_camera_speed(self, speed: int) -> None:
        self.speed = speed
    
    def set_movement_rectangle(self, width: int = 1500, height: int = 700) -> None:
        if width > self.width or height > self.height:
            error_msg = ["rectangle to limit player movement", 
                        "without camera movement is too big.", 
                        "objects.py set_movement_rectangle()"]
            raise RuntimeError(error_msg)
        x_pos = (self.width - width)/2
        y_pos = (self.height - height)/2
        self.movement_rectangle = (x_pos, y_pos, width, height)
        
    def compute_camera_area(self) -> (int, int, int, int):
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
    
    
