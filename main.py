import pygame, sys, time, random
from battle_func import battle
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(32)

musica = pygame.mixer.Sound("sonidos/musica2.ogg")
fireball = pygame.mixer.Sound("sonidos/Fireball.wav")
sword_hit = pygame.mixer.Sound("sonidos/Sword hit.wav")


pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 800),0,32)
display = pygame.Surface((300, 300))


grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))

knight_img = pygame.image.load('knight.png').convert()
knight_img.set_colorkey((255, 255, 255))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

#Texto
def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(255, 0, 0) is red, to make black text
    text = font.render(string, True, (255, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    totalText = (text, textRect)
    return totalText

#Places "Text in Pygame!" with an x,y coord of 500, 250 and 30 font size
#totalText = set_text("You have encountered an enemy", 500, 250, 30)


# setup mixer to avoid 
#pygame.mixer.init()


#player_cordinates = [0, 0]
clock = pygame.time.Clock()
encounters = pygame.time.Clock()

#monster_positions = [(4,0)]

class Player():
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)
        self.position = (self.x, self.y)
        self.image = grass_img
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        self.scrollx = 0
        self.scrolly = 0
        self.death = False

        self.hp = 10
        self.atk = 3

    def draw(self, screen):
        display.blit(knight_img, (150-10 , 150-14)) #antes le sumaba y restaba las cordenadas del personaje para hacerlo mover

    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed:
            self.velX = -self.speed
            player.scrollx += 4
        if self.right_pressed:
            self.velX = self.speed
            self.scrollx -= 4
        if self.up_pressed:
            self.velY = self.speed
            self.scrolly += 4
        if self.down_pressed:
            self.velY = -self.speed
            self.scrolly -=4
        
        self.x += self.velX/3
        self.y += self.velY/3

        self.position = (self.x, self.y)

        self.image = grass_img

player = Player(0, 0)

class Monster():
    def __init__(self) -> None:
        self.hp = 10
        self.atk = 2


def menu():
    menu1 = True
    player.left_pressed = False
    player.right_pressed = False
    player.up_pressed = False
    player.down_pressed = False
    while menu1:
        screen.fill((0, 0, 0))
        inventario = pygame.image.load('inventario.png')
        inventario.set_colorkey((255, 255, 255))
        screen.blit(inventario, (0 , 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu1 = False
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_e:
                  menu1= False
                  
        
        option1 = pygame.Rect(100, 100, 100, 100)
        pygame.draw.rect(screen, (255, 0, 0), option1)
        #display.blit()
        pygame.display.update()
        #clock.tick(60)


print(map_data)
while True:
  display.fill((0,0,0))

  for y, row in enumerate(map_data):
      for x, tile in enumerate(row):
          if tile == 1:
              #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
              display.blit(grass_img, (150 + x * 10 - y * 10 + player.scrollx, -390 + x * 5 + y * 5 + player.scrolly))
              if player.scrollx > 200:
                  player.scrollx = -400
              elif player.scrollx < -400:
                  player.scrollx = 200
              elif player.scrolly > 300:
                  player.scrolly = -200
              elif player.scrolly < -200:
                  player.scrolly = 300

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              player.left_pressed = True
          if event.key == pygame.K_RIGHT:
              player.right_pressed = True
          if event.key == pygame.K_UP:
              player.up_pressed = True
          if event.key == pygame.K_DOWN:
              player.down_pressed = True
          if event.key == pygame.K_e:
              menu()
      if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
              player.left_pressed = False
          if event.key == pygame.K_RIGHT:
              player.right_pressed = False
          if event.key == pygame.K_UP:
              player.up_pressed = False
          if event.key == pygame.K_DOWN:
              player.down_pressed = False
    
  """if (player.position) in monster_positions:
    monster_positions.pop()
    menu()"""
    #NO FUNCIONAAAAA
        
  #print((player.position)) #esta no es la pocision real, es relativa a donde partio (150, 100)

  #print(player.scrollx, player.scrolly)

  x = 0    
  if x == random.randint(0, 100):
    player.left_pressed = False
    player.right_pressed = False
    player.up_pressed = False
    player.down_pressed = False
    battle(musica, Monster, screen, player)
    

  #print(pygame.time.get_ticks())
  player.draw(screen)
  player.update()
  pygame.display.flip() #porque????????????????????????????????????

  clock.tick(120) #porque????????????????????????????????????

  screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0)) # esta cosa esta causando problemas pero me da lata arreglarlo
  pygame.display.update()
  #time.sleep(1)

while player.death == True:
  display.fill((0,0,0))

  text = set_text(f"You died", 150, 100, 40)
  display.blit(text[0], text[1])

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

  clock.tick(120)

  player.draw(screen)
  player.update()
  pygame.display.flip()
  screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0)) # esta cosa esta causando problemas pero me da lata arreglarlo
  pygame.display.update()