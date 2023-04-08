import pygame
import pygame_menu

pygame.init()
window = pygame.display.set_mode((1280,720))

pink = pygame_menu.themes.THEME_BLUE.copy()
pink.title_background_color=(245, 103, 176)
pink.title_font = pygame_menu.font.FONT_NEVIS




def start():
    pass

menu = pygame_menu.Menu('Doki Doki Nature Club', 1280, 720, theme=pink)
menu.add.button("Play", start)
menu.add.button("Quit", pygame_menu.events.EXIT)

menu.mainloop(window)