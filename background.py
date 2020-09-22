
class Map:
    """representation of a simple map used for testing"""
    
    def __init__(self, width: int = 2000, height: int = 1800):
        self.width = width
        self.height = height
        self.new_rectangles = []
        self.old_rectangles = []
        self.set_surrounding_borders()
    
    def set_surrounding_borders(self, border_strength = 20):
        border_left = (0,0, border_strength, self.height)
        border_right = (self.width-border_strength, 0,
                        border_strength, self.height)
        border_up = (border_strength , 0,
                     self.width-2*border_strength, border_strength)
        border_down = (border_strength, self.height-border_strength,
                       self.width-2*border_strength, border_strength)

        self.borders = (border_left, border_right, border_up, border_down)
        self.border_strength = border_strength
    
    def set_color_borders(self, color):
        self.borderColor = color
    
    def set_color_background(self, color):
        self.bgColor = color
        
    def allowed_walking_area(self) -> (int, int, int, int):
        width = self.width - (self.border_strength)*2
        height = self.height - (self.border_strength)*2
        
        walking_rectangle = (self.border_strength, self.border_strength,
                                  width , height)
        return walking_rectangle
