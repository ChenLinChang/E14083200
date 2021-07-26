import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()
# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (50, 50))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH,BTN_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH,BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_WIDTH))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))

#set window caption
pygame.display.set_caption("My first game")
#clock
clock=pygame.time.Clock()
start=time.time()
print("time=",start)



class Game:
    def __init__(self):
        #window
        self.win=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            # draw background
            self.win.blit(background_image,(0,0))

            # draw enemy and health bar
            self.win.blit(enemy_image, (0, 280))
            pygame.draw.rect(self.win,(255,0,0),[5,270,60,10])
            # draw menu (and buttons)
            pygame.draw.rect(self.win, (0, 0, 0), [0, 0, 1024, 80])
            self.win.blit(continue_image, (870, 0))
            self.win.blit(muse_image, (730, 0))
            self.win.blit(pause_image, (940, 0))
            self.win.blit(sound_image, (800, 0))
            place=380
            for i in range(0,5,1):
                self.win.blit(hp_image, (place, 0))
                place=place+50
            place=380
            for j in range(0,5,1):
                if j>=2:
                    self.win.blit(hp_gray_image, (place, 40))
                else:
                    self.win.blit(hp_image, (place, 40))

                place=place+50



            # draw time
            time_record=time.time()
            time_pass=int(time_record-start)
            #製作時間字串
            min=str(time_pass//60).zfill(2)
            sec=str(time_pass%60).zfill(2)
            time_str=min+":"+sec
            pygame.draw.rect(self.win, (0, 0, 0), [0, 530, 130, 70])
            font1=pygame.font.SysFont('arial',48)
            text_time=font1.render(time_str,True,WHITE)
            self.win.blit(text_time, (15,540))
            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



