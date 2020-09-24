import objects.dataStructs.rectangles as rects

class MovingObject():
    """Parent object for the Player and Camera objects."""
    
    def __init__(self, rectangle: rects.Rectangle):
        self._x = rectangle.x
        self._y = rectangle.y
        self._width = rectangle.width
        self._height = rectangle.height
    
    # i read, that the way to implement
    # getters and setters in python  
    # accsess self._x = ... with self.x = ...
    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y
    
    @property
    def width(self) -> int:
        return self._width
    
    @property
    def height(self) -> int:
        return self._height
    
    @x.setter
    def x(self, x: int) -> None:
        self._x = x
        
    @y.setter
    def y(self, y: int) -> None:
        self._y = y
        
    @width.setter
    def width(self, width: int) -> None:
        self._width = width
        
    @height.setter
    def height(self, height: int) -> None:
        self._height = height
    
    # hopefully that uses the getters
    def rect_format(self) -> (int, int, int, int):
        return (self.x, self.y, self.width, self.height)
    
    # no getter and setter needed here,
    # following setters are called only once
    def set_speed(self, speed: int = 5):
        self.speed = speed

    # values saved here are used
    # in the two functions underneath
    def set_keys_move(self, up: int, left: int, down: int, right: int) -> None:
        self.Key_move_up = up
        self.Key_move_left = left
        self.Key_move_down = down
        self.Key_move_right = right
        
        self.set_control_quadrupel() # is that the word^^?
    
    # needed in boxhead.py to indicate the instruction
    def set_control_quadrupel(self) -> None:
        self.controls = (self.Key_move_up, self.Key_move_left,
                        self.Key_move_down, self.Key_move_right)
    
    # calls child classes move(),
    # to avoid that "stuck in the wall"
    # bug on player side -> got an extra if
    def update_coordinates(self, key: int) -> None:
        if key == self.Key_move_up:
            self.move_up()
        elif key == self.Key_move_down:
            self.move_down()
        
        if key == self.Key_move_left:
            self.move_left()
        elif key == self.Key_move_right:
            self.move_right()
    
    def move(self, key: int) -> None:
        self.update_coordinates(key)
