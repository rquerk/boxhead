import pygame

import objects.cameras
import objects.players
import objects.background
import objects.dataStructs.rectangles as rects

import pdb

# got to exclude these dicts
CAM_SIZE = {"width": 1800, "height": 950}
CAM_START_POS = {"x": 0, "y": 0}
PLAYER_SIZE = {"width": 30, "height": 10}
PLAYER_START_POS = {"x": 500, "y": 500}
MAP_SIZE = {"width": 3000, "height": 2000}

class Engine:
    """Called this Engine, to show that I'm handling
    all the stuff pygame gives me to create a game
    and forming an own little libary of funcitons
    like init_player, or update_screen."""
    
    def __init__(self):
        pygame.init()
        
        self.camera = self.init_camera()
        self.screen = pygame.display.set_mode(
                        (self.camera.width,
                         self.camera.height))
        pygame.display.set_caption("boxhead")
        
        pygame.event.set_blocked(None)
        self.allowedTypes: [int] = [pygame.QUIT]
        pygame.event.set_allowed(self.allowedTypes)
        
        self.map = self.init_map()
        self.player = self.init_player()
    
    # ------------ more init functions --------------------------------- #
    # should be able to make following three functions into one
    def init_map_rect(self) -> rects.Rectangle:
        map_rectangle = rects.Rectangle()
        map_rectangle.width = MAP_SIZE["width"]
        map_rectangle.height = MAP_SIZE["height"]
        return map_rectangle
    
    def init_cam_rect(self) -> rects.Rectangle:
        cam_rectangle = rects.Rectangle()
        cam_rectangle.x = CAM_START_POS["x"]
        cam_rectangle.y = CAM_START_POS["y"]
        cam_rectangle.width = CAM_SIZE["width"]
        cam_rectangle.height = CAM_SIZE["height"]
        #pdb.set_trace()
        return cam_rectangle
    
    def init_player_rect(self) -> rects.Rectangle:
        player_rect = rects.Rectangle()
        player_rect.x = PLAYER_START_POS["x"]
        player_rect.y = PLAYER_START_POS["y"]
        player_rect.width = PLAYER_SIZE["width"]
        player_rect.height = PLAYER_SIZE["height"]
        return player_rect

    # even more init
    def init_camera(self) -> objects.cameras.Camera:
        camera_rect = self.init_cam_rect()
        camera = objects.cameras.Camera(camera_rect)
        camera.set_keys_move(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
        camera.set_movement_rectangle()
        camera.set_speed()
        return camera
        
    def init_map(self) -> objects.background.Map:
        map_rect = self.init_map_rect()
        map = objects.background.Map(map_rect)
        map.set_color_background(pygame.Color("black"))
        map.set_color_borders(pygame.Color("white"))
        self.map_surface = pygame.Surface((map.width, map.height))
        return map
    
    def init_player(self) -> objects.players.Player:
        player_rect = self.init_player_rect()
        player = objects.players.Player(player_rect)
        player.set_speed()
        player.set_keys_move(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
        player.set_color_player(pygame.Color("white"))
        player.set_walking_rectangle(self.map)
        self.player_surface = pygame.Surface((player.width,
                                              player.height))
        return player
    
    # ok end of all this init
    def draw_player_surface(self) -> None:
        """painting the player surface with the draw function"""
        width_height = self.player.rect_format()
        # 0, 0, mean we paint from that pos
        # on the surface => hole surface
        # dont use player.x/y
        player_prect = (0, 0, width_height[2], width_height[3])
        pygame.draw.rect(self.player_surface, self.player.color, player_prect)
        self.blit_player_on_map()
        
    def draw_map_borders(self) -> None:
        for rect in self.map.borders:
            pygame.draw.rect(self.map_surface, self.map.borderColor,
                                                            pygame.Rect(rect))
        self.blit_map_on_screen()
    
    # drawing the objects on surfaces once in the beginning
    def draw_first_frame(self) -> None: 
        self.screen.fill(pygame.Color("black"))
        self.draw_map_borders()
        self.draw_player_surface()
        self.update_screen()
        
    # ------------- Moving and changeing the screen ----------------------- #
    def move_player_and_camera(self, key: int) -> None:
        player_onMap = pygame.Rect(self.player.rect_format())
        allowed_movement_zone_map = pygame.Rect(self.player.walking_rectangle)
        
        if allowed_movement_zone_map.contains(player_onMap):
            self.player.move(key)
        
        player_onCam = pygame.Rect(
            self.player.position_onCamera(self.camera))
        allowed_movement_zone_cam = pygame.Rect(self.camera.movement_rectangle)
        
        if not allowed_movement_zone_cam.contains(player_onCam):
            self.camera.move(key)
    
    def blit_player_on_map(self) -> None:
        # 0, 0 because we want to blit the hole player surface
        # and player.width/height cuz we blit the full surface
        x_pos = self.player.x
        y_pos = self.player.y
        blitting_area = (0, 0, self.player.width,
                         self.player.height)
        effected_rects = self.map_surface.blit(
            source = self.player_surface,
            dest = (x_pos, y_pos),
            area = blitting_area)
        self.map.new_rectangles.append(effected_rects)
        
    def blit_map_on_screen(self) -> None:
        effected_rects = self.screen.blit(
            source = self.map_surface,
            dest = (0,0),
            area = self.camera.rect_format())
        self.camera.new_rectangles.append(effected_rects)
    
    
    def update_screen(self) -> None:
        self.remove_old_rects_from_map()
        self.remove_old_rects_from_screen()
        self.blit_player_on_map()
        self.blit_map_on_screen()
        effected_rects = (self.camera.new_rectangles
                        + self.camera.old_rectangles)
        pygame.display.update(effected_rects)
        
        self.swap_old_and_new_rects_then_clear_new()
        
    # -------------------------Removing logic ---------------------------- #
    # removing with draw istead of blit... not such good idea
    def remove_old_rects_from_screen(self) -> None:
        for old in self.camera.old_rectangles:
            pygame.draw.rect(self.screen, self.map.bgColor, old)
    
    def remove_old_rects_from_map(self) -> None:
        for old in self.map.old_rectangles:
            pygame.draw.rect(self.map_surface, self.map.bgColor, old)
            
    def swap_old_and_new_rects_then_clear_new(self) -> None:
        # new  rectangles, blitted or drawn to screen
        # will be old in next loop run,
        # and old is not effected anymore
        self.camera.old_rectangles.clear()
        self.camera.old_rectangles.extend(self.camera.new_rectangles)
        self.camera.new_rectangles.clear()
        # same with players traces
        self.map.old_rectangles.clear()
        self.map.old_rectangles.extend(self.map.new_rectangles)
        self.map.new_rectangles.clear()
