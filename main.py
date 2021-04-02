# HELLO DO YOU SEE THIS?!


import sys, pygame
pygame.init()

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qix Game")

WHITE = (255, 255, 255)
ARROW_KEYS = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]
FPS = 60

def draw_window():
        WIN.fill(WHITE)
        pygame.display.update()

def main():
        clock = pygame.time.Clock()
        run = True
        while run: 
                clock.tick(FPS)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                draw_window()

        pygame.quit()

if __name__ == "__main__":
        main()