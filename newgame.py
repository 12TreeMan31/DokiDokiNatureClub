import pygame
import pygame_menu

pygame.init()
window = pygame.display.set_mode((1280,720))


def start():
    pass

menu = pygame_menu.Menu('Doki Doki Nature Club', 1280, 720, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button("Play", start)
menu.add.button("Quit", pygame_menu.events.EXIT)

menu.mainloop(window)