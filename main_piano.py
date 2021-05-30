# Alexander Carpio Mamani
import pygame, sys
from pygame.locals import *
from playsound import playsound
from threading import Thread

clock = pygame.time.Clock()
pygame.init()

WINDOW_SIZE = (500,190)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)


def play_note(note):

        function = Thread(target = playsound, args=('music_notes\\'+note+'.wav',))
        function.start()


class Piano:
        
        width = 60
        height = 180

        top = {8: 30, 9: 110, 10: 210, 11: 290, 12: 370}
        bot = 100

        notes = ['C','D','E','F','G','A','B','C1','C_s','D_s','F_s','G_s','Bb']
        lenght = len(notes)
        state_notes = [False]*lenght
        time_notes = [0]*lenght
        key_notes = [K_a,K_s,K_d,K_f,K_g,K_h,K_j,K_k,K_w,K_e,K_y,K_u,K_i]

        color_on = (0,255,0)
        color_off_bot = (255,255,255)
        color_off_top = (0,0,0)
        color = None

        font = pygame.font.Font(None,20)
        
        def down_key(self,key):
                for i in range(self.lenght):
                        if key == self.key_notes[i]:
                                self.state_notes[i] = True
   
        def up_key(self,key):
                for i in range(self.lenght):
                        if key == self.key_notes[i]:
                                self.state_notes[i] = False

        def set_states(self, i):
                if self.state_notes[i]:
                        self.time_notes[i] += 1
                        if self.time_notes[i] > 1:
                                play_note(self.notes[i])
                                self.color = self.color_on
                else:
                        self.time_notes[i] = 0
                        if i < 8:
                                self.color = self.color_off_bot
                        else:
                               self.color = self.color_off_top
                        
        def update_piano(self, display):
                for i in range(8):
                        self.set_states(i)
                        pygame.draw.rect(display, self.color, [10 + self.width*i,5, self.width,self.height])
                        message = self.font.render(self.notes[i], 1, (0,0,0))
                        display.blit(message, (self.width*i + 30, self.height - 10))

                for i in range(8,13):
                        self.set_states(i)
                        pygame.draw.rect(display, self.color, [self.top[i], 5, self.width,self.height-60])
                        message = self.font.render(self.notes[i], 1, (255,255,255))
                        display.blit(message, (self.top[i] + 20, self.height - 70))

piano = Piano()

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit() 
                        sys.exit()
                if event.type == KEYDOWN:
                        piano.down_key(event.key)
                        
                if event.type == KEYUP:
                        piano.up_key(event.key)
                        

        screen.fill((128, 128, 128))

        piano.update_piano(screen)
        
        pygame.display.update()
        clock.tick(30)
