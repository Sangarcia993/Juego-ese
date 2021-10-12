import pygame
from musica import musicaPlayer
from animations import move

def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(255, 0, 0) is red, to make black text
    text = font.render(string, True, (255, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    totalText = (text, textRect)
    return totalText

def battle( Monster, screen, player):
    battle = True
    musicaPlayer("musica", "play", 0.1)
    
    monster = Monster()

    attacked = False
    while battle:
        player_did_something = False
        if True: # esto deberia ser health
            pygame.draw.rect(screen, (0, 0, 0), (100, 100, 600, 500))

            knight = pygame.image.load("knight.png")
            knight.set_colorkey((255, 255, 255))
            new_knight = pygame.transform.scale(knight, (100, 100))
            screen.blit(new_knight, (150, 200))

            text = set_text(f"Player health = {player.hp}", 150, 400, 10)
            screen.blit(text[0], text[1])

            skeleton = pygame.image.load("skeleton.png")
            skeleton.set_colorkey((255, 255, 255))
            skeleton = pygame.transform.scale(skeleton, (100, 100))
            screen.blit(skeleton, (550, 200))

            text = set_text(f"Monster health = {monster.hp}", 550, 400, 10)
            screen.blit(text[0], text[1])

            #anouncment
            text = set_text("You have encountered an enemy", 400, 150, 30)
            screen.blit(text[0], text[1])


            #controls
            text = set_text("What will you do?", 400, 350, 30)
            screen.blit(text[0], text[1])

            text = set_text("[a]ttack?", 400, 400, 30)
            screen.blit(text[0], text[1])

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        musicaPlayer("musica", "stop")
                        battle = False
                    
                    if event.key == pygame.K_a:
                        monster.hp -= player.atk
                        attacked = True
                        player_did_something = True
                        musicaPlayer("sword_hit", "play")
                        move(screen, new_knight, 150, 200, 0, 300)
                        #envez de mover al night mueve una espada
                    
                        if monster.hp <= 0:
                            musicaPlayer("musica", "stop")
                            battle = False
            
            if player_did_something == True and monster.hp > 0:
                player.hp -= monster.atk
                player_did_something = False

            if player.hp < 1:
                player.death = True
                battle = False
                
            if attacked == True:
                text = set_text(f"You did {player.atk} attack", 400, 500, 30)
                screen.blit(text[0], text[1])
            
            pygame.display.update()
