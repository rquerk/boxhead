import objects.dataStructs.rectangles as rects

class Map:
    """representation of a simple map used for testing"""
    
    def __init__(self, rectangle: rects.Rectangle):
        self.width = rectangle.width
        self.height = rectangle.height
        
        self.new_rectangles = []    # painted parts of the screen or map
        self.old_rectangles = []    # parts that need to be removed again
        
        self.set_surrounding_borders()
    
    def set_surrounding_borders(self, border_strength = 20) -> None:
        border_left = (0,0, border_strength, self.height)
        border_right = (self.width-border_strength, 0,
                        border_strength, self.height)
        border_up = (border_strength , 0,
                     self.width-2*border_strength, border_strength)
        border_down = (border_strength, self.height-border_strength,
                       self.width-2*border_strength, border_strength)

        self.borders = (border_left, border_right, border_up, border_down)
        self.border_strength = border_strength
    
    def set_color_borders(self, color: int) -> None:
        self.borderColor = color
    
    def set_color_background(self, color: int) -> None:
        self.bgColor = color
        
    def allowed_walking_area(self) -> (int, int, int, int):
        """Since there are no more things on the map than the borders,
        we have a rectangle shape on it that the player can move on.
        """
        width = self.width - (self.border_strength)*2
        height = self.height - (self.border_strength)*2
        
        allowed_rectangle = (self.border_strength, self.border_strength,
                                  width , height)
        return allowed_rectangle
