import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(32)

musica = pygame.mixer.Sound("sonidos/musica2.ogg")
fireball = pygame.mixer.Sound("sonidos/Fireball.wav")
sword_hit = pygame.mixer.Sound("sonidos/Sword hit.wav")


def musicaPlayer(name, action, volume = 1):
    if action == "play":
        if name == "musica":
            musica.play()
            musica.set_volume(volume)
        elif name == "fireball":
            fireball.play()
        elif name == "sword_hit":
            sword_hit.play()

    if action == "stop":
        if name == "musica":
            musica.stop()
        elif name == "fireball":
            fireball.stop()
        elif name == "sword_hit":
            sword_hit.stop()

