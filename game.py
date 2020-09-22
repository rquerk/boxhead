import pygame

import objects 
import coordinates
import background

class Szenario:
    
    def __init__(self):
        pygame.init()
        self.camera = self.init_camera()
        self.screen = pygame.display.set_mode(
                        (self.camera.width, self.camera.height))
        
        pygame.display.set_caption("boxhead")
        
        pygame.event.set_blocked(None)
        self.allowedTypes: [int] = [pygame.QUIT]
        pygame.event.set_allowed(self.allowedTypes)
        
        self.map = self.init_Map()
        self.player = self.init_player()
    
    # ------------ more init functions --------------------------------- #
    def init_camera(self) -> objects.Camera:
        camera = objects.Camera()
        camera.set_keys_move(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
        camera.set_movement_rectangle()
        camera.set_speed()
        return camera
        
    def init_Map(self) -> background.Map:
        map = background.Map()
        self.map_surface = pygame.Surface((map.width, map.height))
        map.set_color_background(pygame.Color("black"))
        map.set_color_borders(pygame.Color("white"))
        return map
    
    def init_player(self) -> objects.Player:
        player = objects.Player()
        player.set_speed()
        self.player_surface = pygame.Surface((player.width, player.height))
        player.set_keys_move(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d)
        player.set_color_player(pygame.Color("white"))
        player.set_walking_rectangle(self.map)
        
        return player
    
    def draw_player_surface(self) -> None:
        """using the draw function to paint the player surface,
        having that surcafe so i can use blit() for player movement"""
        player_rect = pygame.Rect(0, 0, self.player.width, self.player.height)
        pygame.draw.rect(self.player_surface, self.player.color, player_rect)
        self.blit_player_on_map()
        
    def draw_map_surface(self) -> None:
        for rect in self.map.borders:
            pygame.draw.rect(self.map_surface, self.map.borderColor,
                                                            pygame.Rect(rect))
        self.blit_map_on_screen()
    
    # drawing the objects on surfaces once in the beginning
    def draw_startSzenario(self) -> None: 
        self.screen.fill(pygame.Color("black"))
        self.draw_map_surface()
        self.draw_player_surface()
        self.update_screen()
        
    # ------------- Moving and changeing the screen ----------------------- #
    def move_player_and_camera(self, key: int) -> None:
        player_onMap = pygame.Rect(self.player.get_area())
        allowed_movement_zone_map = pygame.Rect(self.player.walking_rectangle)
        
        if allowed_movement_zone_map.contains(player_onMap):
            self.player.move(key)
        
        player_onCam = pygame.Rect(
            self.player.position_onCamera(self.camera))
        allowed_movement_zone_cam = pygame.Rect(self.camera.movement_rectangle)
        
        if not allowed_movement_zone_cam.contains(player_onCam):
            self.camera.move(key)
    
    def blit_player_on_map(self) -> None:
        x_pos = self.player.x_onMap
        y_pos = self.player.y_onMap
        player_area = (0, 0, self.player.width, self.player.height)
        effected_rects = self.map_surface.blit(
            source = self.player_surface,
            dest = (x_pos, y_pos),
            area = player_area)
        self.map.new_rectangles.append(effected_rects)
        
    def blit_map_on_screen(self) -> None:
        effected_rects = self.screen.blit(
            source = self.map_surface,
            dest = (0,0),
            area = self.camera.compute_area_onMap())
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
