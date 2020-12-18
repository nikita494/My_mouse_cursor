import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    cursor = pygame.image.load('data\\arrow.png')
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_focused():
            rect = cursor.get_rect()
            rect.center = pygame.mouse.get_pos()
            screen.blit(cursor, rect)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
