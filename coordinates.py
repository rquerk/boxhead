
class MovingObject:
    
    def __init__(self, x: int, y : int):
        self._x_onMap = x
        self._y_onMap = y
        
    @property
    def x_onMap(self) -> int:
        return self._x_onMap
    
    @property
    def y_onMap(self) -> int:
        return self._y_onMap
    
    @x_onMap.setter
    def x_onMap(self, x: int) -> None:
        self._x_onMap = x
    
    @y_onMap.setter
    def y_onMap(self, y: int) -> None:
        self._y_onMap = y

    def set_keys_move(self, Key_move_up, Key_move_left, Key_move_down, Key_move_right):
        self.Key_move_up = Key_move_up
        self.Key_move_left = Key_move_left
        self.Key_move_down = Key_move_down
        self.Key_move_right = Key_move_right
        
        self.controls = (self.Key_move_up, self.Key_move_left,
                        self.Key_move_down, self.Key_move_right)
    
    def update_coordinates(self, key: int):
        if key == self.Key_move_up:
            self.move_up()
        elif key == self.Key_move_down:
            self.move_down()
        
        if key == self.Key_move_left:
            self.move_left()
        elif key == self.Key_move_right:
            self.move_right()
    
    def move(self, key: int):
        self.update_coordinates(key)
