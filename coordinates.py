
class MovingObject:
    
    def __init__(self):
        pass

    def set_keys_move(self, Key_move_up, Key_move_left, Key_move_down, Key_move_right):
        self.Key_move_up = Key_move_up
        self.Key_move_left = Key_move_left
        self.Key_move_down = Key_move_down
        self.Key_move_right = Key_move_right
        
        self.controls = (self.Key_move_up, self.Key_move_left,
                        self.Key_move_down, self.Key_move_right)
    
    def update_coordinates(self, key):
        if key == self.Key_move_up:
            self.move_up()
        elif key == self.Key_move_down:
            self.move_down()
        
        if key == self.Key_move_left:
            self.move_left()
        elif key == self.Key_move_right:
            self.move_right()
    
    def move(self, key):
        self.update_coordinates(key)
