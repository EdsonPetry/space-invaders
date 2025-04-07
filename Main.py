import pygame
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))

class Main():
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.main()
    
    def main(self):

        running = True

        while running:
            window.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False


if __name__ == "__main__":
    Main(width, height)