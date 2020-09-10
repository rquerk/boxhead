import coordinates

class Player(coordinates.MovingObject):
    
    def __init__(self, x = 750, y = 350, speed = 3, width = 30, height = 10):
        self.x_onMap = x
        self.y_onMap = y
        self.speed = speed
        self.width = width
        self.height = height
       
    def get_area(self):
        player_area = (self.x_onMap, self.y_onMap, self.width, self.height)
        return player_area
    
    def allowed_walking_area(self, width, height, border_strength):
        move_width = width - border_strength*2
        move_height = height - border_strength*2
        
        self.walking_rectangle = (border_strength, border_strength,
                                  move_width , move_height)
        
        return self.walking_rectangle
    
    def position_onCamera(self, cameraObj):
        self.x_onCamera = self.x_onMap - cameraObj.x_onMap
        self.y_onCamera = self.y_onMap - cameraObj.y_onMap
        self.rectangle = (self.x_onCamera, self.y_onCamera,
                          self.width, self.height)
        return (self.rectangle)
    
    def set_color_player(self, color):
        self.color = color
        
    
    def can_move_up(self):
        if self.y_onMap > self.walking_rectangle[1] + self.speed:
            return True
        else: return False
    
    def can_move_left(self):
        if self.x_onMap > (self.walking_rectangle[0] + self.speed):
            return True
        else: return False
    
    def can_move_down(self):
        pos = self.y_onMap + self.height + self.speed
        if pos < (self.walking_rectangle[1]
                + self.walking_rectangle[3]):
            return True
        else: return False
    
    def can_move_right(self):
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

    def __init__(self, x = 0, y = 0, width = 1800, height = 950):
        self.x_onMap = x
        self.y_onMap = y
        self.width = width
        self.height = height
        
        self.size = (width, height)
        
        self.old_rectangles = []
        self.new_rectangles = []
    
    def get_camera_area(self):
        camera_area = (self.x_onMap, self.y_onMap, self.width, self.height)
        return camera_area
    
    def set_movement_rectangle(self, width = 1500, height = 700):
        if width > self.width or height > self.height:
            error_msg = ["rectangle to limit player movement", 
                        "without camera movement is too big.", 
                        "objects.py set_movement_rectangle()"]
            raise RuntimeError(error_msg)
        x_pos = (self.width - width)/2
        y_pos = (self.height - height)/2
        self.movement_rectangle = (x_pos, y_pos, width, height)
    
    def set_camera_speed(self, speed):
        self.speed = speed
        
    def move_up(self):
        self.y_onMap -= self.speed 
    
    def move_left(self):
        self.x_onMap -= self.speed
        
    def move_right(self):
        self.x_onMap += self.speed
    
    def move_down(self):
        self.y_onMap += self.speed
