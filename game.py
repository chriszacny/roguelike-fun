import pygame
import os


def main():
    pygame.init()
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Zelda Dungeon")

    image = pygame.image.load(os.path.join('images', 'link-down64x64.png'))
    screen = pygame.display.set_mode((800, 600))
    screen.blit(image, (50, 50))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
