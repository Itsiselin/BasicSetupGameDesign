# Example file showing a circle moving on screen
import pygame

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1280, 720))
    self.clock = pygame.time.Clock()
    self.running = True
    self.dt = 0
    self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

  def process_input(self):
    # This is a function that runs every frame to process input
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.player_pos.y -= 300 * self.dt        
    if keys[pygame.K_s]:
      self.player_pos.y += 300 * self.dt
    if keys[pygame.K_a]:
      self.player_pos.x -= 300 * self.dt
    if keys[pygame.K_d]:
      self.player_pos.x += 300 * self.dt     
    

  def render(self):
    # This is a function that runs every frame to render the game state to the screen
    # fill the screen with a color to wipe away anything from last frame
    self.screen.fill("purple")
    
    
    pygame.draw.circle(self.screen, "red", self.player_pos, 40)

    # flip() the display to put your work on screen
    pygame.display.flip()

  def update(self):
    # This is a function that runs every frame to update the game state
    pass

  def game_loop(self):
    while self.running:
      self.process_input()
      self.update()
      self.render()

      # limits FPS to 60
      # dt is delta time in seconds since last frame, used for framerate-
      # independent physics.
      self.dt = self.clock.tick(60) / 1000

# main entry point for our program
if __name__ == "__main__":
  
  game = Game()
  
  game.game_loop()
  
  pygame.quit()
