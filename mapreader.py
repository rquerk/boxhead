
class MapObject:
    
    def __init__(self, width: int = 10000, height: int = 5000):
        self.width = width
        self.height = height
        
    # used for testing, objects should be loaded by the MapReader    
    def set_surrounding_borders(self, border_strength = 20):
        self.border_strength = border_strength
        self.border_left    = (0,0, border_strength, height)
        self.border_right   = (width-border_strength, 0,
                               border_strength, self.height)
        self.border_up      = (border_strength ,0 ,
                               width-2*border_strength, border_strength)
        self.border_down    = (border_strength, height-border_strength,
                               width-2*border_strength, border_strength)

        self.borders = (border_left, border_right, border_up, border_down)

    def set_color_borders(self, color: int):
        self.borderColor = color
    
    def set_color_background(self, color: int):
        self.bgColor = color
        
        
class MapReader:
    
    def read_map_from_file(self, filename: str):
        with open(filename, 'r') as mapFile:
            map_data = mapFile.readlines()
            names, values = [], []
            for line in map_data:
                name_value = line.strip().split('=')
                names.append(name_value[0])
                # an exception could occure here
                values.append(int(name_value[1]))
            
            #TODO
            #save translated values into quadrupels
            
            print("Names: ", names)
            print("Values: ", values)
            self.is_same_lenght(names = names, values = values)
    
    def is_same_lenght(self, names, values):
        error_msg = ["input file for map is invalid",
                    "len(names) don't match len(values)",
                    "mapreader.py save_values()"]
        if len(names) != len(values):
            raise RuntimeError(error_msg)
        return True
    
    
if __name__ == "__main__":
    
    mapObj = MapReader()
    mapObj.read_map_from_file("map")
