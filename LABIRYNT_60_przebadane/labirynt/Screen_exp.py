 #!/usr/bin/env python

import pygame, sys, os
from pygame.locals import *
import time
from Level_exp import Level
pygame.mixer.init()
import os, pygame.mixer
pygame.font.init
import numpy as np

from arrows import DrawArrow

class Screen:   
    def __init__(self, file_):
        self.size = 45
        self.pouse_stop = 0
        self.pouse_start = 0
        self.time_penalty = 0
        self.FRAME_RATE = 30
        self.file_name = './labirynt/wyniki.npy'
        self.data= list(file_)
        self.score = {}
        self.data.append(self.score)
        self.x_offset = 0
        self.y_offset = 0

        self.level = Level()
        self.score['kolejnosc']=self.level.random_levels
        self.calcGridOffsets()

        self.current_level = 1
        self.lives = 5
        
        self.animation_offset_x = 0
        self.animation_offset_y = 0

        self.stop_moving = False
        self.restart = False

        pygame.init()
        self.screen = pygame.display.set_mode((640, 480), FULLSCREEN)
        pygame.display.set_caption('Labirynt')
        pygame.mouse.set_visible(0)
        pygame.display.init()


        #Font
        self.font = pygame.font.Font(os.path.join('labirynt/data','impact.ttf'), 16)

        #Sounds
        self.intro_sound = pygame.mixer.Sound(os.path.join('labirynt/data','Main.wav'))
        self.enter_sound = pygame.mixer.Sound(os.path.join('labirynt/data','Enter.wav'))
        self.hit_wall_sound = pygame.mixer.Sound(os.path.join('labirynt/data','Boom.wav'))
        self.game_over_sound = pygame.mixer.Sound(os.path.join('labirynt/data','GameOver.wav'))
        self.fall_sound = pygame.mixer.Sound(os.path.join('labirynt/data','Fall.wav'))
        self.game_intro_sound = pygame.mixer.Sound(os.path.join('labirynt/data','Logo.ogg'))

        #Images
        self.ball_1 = pygame.image.load(os.path.join("labirynt/data","ball.png"))
        self.ball_2 = pygame.image.load(os.path.join("labirynt/data","ball.png"))
        self.intro_image = pygame.image.load(os.path.join("labirynt/data","Intro.gif"))
        self.intro_image_2 = pygame.image.load(os.path.join("labirynt/data","Intro2.gif"))
        self.you_lose_image = pygame.image.load(os.path.join("labirynt/data","YouLose.gif"))
        self.menu_image = pygame.image.load(os.path.join("labirynt/data","Menu2_exp.gif"))
        self.block = pygame.image.load(os.path.join("labirynt/data","block.gif"))
        self.horizontal_block = pygame.image.load(os.path.join("labirynt/data","Horizblock.gif"))
        self.vertical_block = pygame.image.load(os.path.join("labirynt/data","Vertblock.gif"))
        self.floor_block = pygame.image.load(os.path.join("labirynt/data","floor.gif"))
        self.hole_block = pygame.image.load(os.path.join("labirynt/data","hole.gif"))
        self.start_block = pygame.image.load(os.path.join("labirynt/data","start.gif"))
        self.finish_block = pygame.image.load(os.path.join("labirynt/data","finish.gif"))
        self.black_screen = pygame.image.load(os.path.join("labirynt/data","blank.gif"))
        self.you_win_image = pygame.image.load(os.path.join("labirynt/data","YouWin_exp.gif"))
        self.instructions = pygame.image.load(os.path.join("labirynt/data","instructions_exp.png"))
        self.przerwa = pygame.image.load(os.path.join("labirynt/data","break.gif"))
        
        self.arrow_right = DrawArrow(self.screen, 'right')
        self.arrow_left = DrawArrow(self.screen, 'left')
        self.arrow_top = DrawArrow(self.screen, 'top')
        self.arrow_down = DrawArrow(self.screen, 'down')

    def update_file_score(self):
        np.save(self.file_name, self.data)

    def update_score(self):
        try:
            self.score[self.level.get_level_number(self.current_level)].append(self.get_timelevel())
        except:
            self.score[self.level.get_level_number(self.current_level)]=[self.get_timelevel()]
        self.data[-1]=self.score
        self.update_file_score()

    def displayMainMenu(self):
        button_position = 1
        not_done = True
        while (not_done):
            if button_position == 1:
                self.screen.blit(self.black_screen, (0,0))
                self.screen.blit(self.menu_image, (0, 0))
                self.screen.blit(self.ball_1, (225,270))#(163, 282))
                self.screen.blit(self.ball_1, (368, 270))
                pygame.display.flip()
            if button_position == 2:
                self.screen.blit(self.black_screen, (0,0))
                self.screen.blit(self.menu_image, (0, 0))
                self.screen.blit(self.ball_1, (200, 315))
                self.screen.blit(self.ball_1, (393, 315))
                pygame.display.flip()
            if button_position == 3:
                self.screen.blit(self.black_screen, (0,0))
                self.screen.blit(self.menu_image, (0, 0))
                self.screen.blit(self.ball_1, (165, 362))
                self.screen.blit(self.ball_1, (425, 362))
                pygame.display.flip()
            if button_position == 4:
                self.screen.blit(self.black_screen, (0,0))
                self.screen.blit(self.menu_image, (0, 0))
                self.screen.blit(self.ball_1, (173, 410))
                self.screen.blit(self.ball_1, (419, 410))
                pygame.display.flip()
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    if (event.key == K_DOWN) and button_position == 3:
                        button_position = 4
                    if (event.key == K_DOWN) and button_position == 2:
                        button_position = 3
                    if (event.key == K_DOWN) and button_position == 1:
                        button_position = 2
                    if (event.key == K_UP) and button_position == 2:
                        button_position = 1
                    if (event.key == K_UP) and button_position == 3:
                        button_position = 2
                    if (event.key == K_UP) and button_position == 4:
                        button_position = 3               
                    if (event.key == K_RETURN) and button_position == 1:
                        return
                    if (event.key == K_RETURN) and button_position == 2:
                        pygame.quit()
                        sys.exit()            
                    if (event.key == K_RETURN) and button_position == 3:
                        self.screen = pygame.display.set_mode((640, 480), FULLSCREEN)
                    if (event.key == K_RETURN) and button_position == 4:
                        self.screen = pygame.display.set_mode((640, 480))

    def drawLevel(self):
        self.screen.blit(self.black_screen, (0, 0))
        self.drawUI()
        for ym in range(0, len(self.getLevelObject().getLevelArray()), 1):
            for xm in range(0, len(self.getLevelObject().getLevelArray()[0]), 1):
                if self.getLevelObject().getLevelArray()[ym][xm] == 0:
                    self.screen.blit(self.floor_block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
                if self.getLevelObject().getLevelArray()[ym][xm] == 1:
                    self.screen.blit(self.block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
                if self.getLevelObject().getLevelArray()[ym][xm] == 2:
                    self.screen.blit(self.hole_block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
                if self.getLevelObject().getLevelArray()[ym][xm] == 3:
                    self.screen.blit(self.start_block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
                if self.getLevelObject().getLevelArray()[ym][xm] == 4:
                    self.screen.blit(self.finish_block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
                if self.getLevelObject().getLevelArray()[ym][xm] == 5:
                    self.screen.blit(self.horizontal_block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
                if self.getLevelObject().getLevelArray()[ym][xm] == 6:
                    self.screen.blit(self.vertical_block, (xm * self.size + self.x_offset, ym * self.size + self.y_offset))
        self.screen.blit(self.ball_1, ((self.getLevelObject().getBallX() * self.size) + self.animation_offset_x + self.x_offset, (self.getLevelObject().getBallY()* self.size) + self.animation_offset_y + self.y_offset))
        self.screen.blit(self.ball_2, ((self.getLevelObject().getBallX() * self.size) + self.animation_offset_x + self.x_offset, (self.getLevelObject().getBallY()* self.size) + self.animation_offset_y + self.y_offset))
        

    def update(self):
        self.drawLevel()
        pygame.display.flip()
        for event in pygame.event.get():                    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):            
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                                    
                if (event.key == K_RIGHT):
                    self.arrow_right.init_position((self.getLevelObject().getBallX()*self.size+self.x_offset+self.size,self.getLevelObject().getBallY()*self.size+ self.y_offset+int(0.5*self.size)))
                    self.arrow_right.init_draw_arrow()
                    time.sleep(0.2)
                    self.moveRight()
                    key_down=True
      
                if (event.key == K_LEFT):
                    self.arrow_left.init_position((self.getLevelObject().getBallX()*self.size+self.x_offset,self.getLevelObject().getBallY()*self.size+ self.y_offset+int(0.5*self.size)))
                    self.arrow_left.init_draw_arrow()
                    time.sleep(0.2)
                    self.moveLeft()                 
                      
                if (event.key == K_DOWN):
                    self.arrow_down.init_position((self.getLevelObject().getBallX()*self.size+self.x_offset+int(0.5*self.size),self.getLevelObject().getBallY()*self.size+ self.y_offset+self.size))
                    self.arrow_down.init_draw_arrow()
                    time.sleep(0.2)
                    self.moveDown()
                         
                if (event.key == K_UP):
                    self.arrow_top.init_position((self.getLevelObject().getBallX()*self.size+self.x_offset+int(0.5*self.size),self.getLevelObject().getBallY()*self.size+ self.y_offset))
                    self.arrow_top.init_draw_arrow()
                    time.sleep(0.2)
                    self.moveUp()

                if (event.key == K_q):
                    self.skip_maze()


        self.stop_moving = False;



    def moveDown(self):
        self.animation_offset_y = 0
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 2) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 6)):
            self.die()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 1) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 5)):
            self.hit_wall_sound.play()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 0) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 3)):
            if(self.stop_moving != True):
                for i in range(0, 4, 1):
                    self.animation_offset_y+=8
                    self.drawLevel()
                    time.sleep(0.025)
                    pygame.display.flip()
                self.getLevelObject().setBallY(self.getLevelObject().getBallY() + 1)
                self.moveDown()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() + 1)][(self.getLevelObject().getBallX())] == 4)):
            self.winLevel()
            
    def moveUp(self):
        self.animation_offset_y = 0
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 2) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 6)):
            self.die()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 1) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 5)):
            self.hit_wall_sound.play()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 0) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 3)):
            if(self.stop_moving != True):
                for i in range(0, 4, 1):
                    self.animation_offset_y-=8
                    self.drawLevel()
                    time.sleep(0.025)
                    pygame.display.flip()
                self.getLevelObject().setBallY(self.getLevelObject().getBallY() - 1)
                self.moveUp()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY() - 1)][(self.getLevelObject().getBallX())] == 4)):
            self.winLevel()

    def moveRight(self):
        self.animation_offset_x = 0
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 2) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 5)):
            self.die()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 1) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 6)):
            self.hit_wall_sound.play()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 0) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 3)):
            if(self.stop_moving != True):
                for i in range(0, 4, 1):
                    self.animation_offset_x+=8
                    self.drawLevel()
                    time.sleep(0.025)
                    pygame.display.flip()
                self.getLevelObject().setBallX(self.getLevelObject().getBallX() + 1)
                self.moveRight()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() + 1)] == 4)):
            self.winLevel()

    def moveLeft(self):
        self.animation_offset_x = 0
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 2) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 5)):
            self.die()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 1) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 6)):
            self.hit_wall_sound.play()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 0) or (self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 3)):
            if(self.stop_moving != True):
                for i in range(0, 4, 1):
                    self.animation_offset_x-=8
                    self.drawLevel()
                    time.sleep(0.025)
                    pygame.display.flip()
                self.getLevelObject().setBallX(self.getLevelObject().getBallX() - 1)
                self.moveLeft()
        if((self.getLevelObject().getLevelArray()[(self.getLevelObject().getBallY())][(self.getLevelObject().getBallX() - 1)] == 4)):
            self.winLevel()

    def getLevelObject(self):
        return self.level

    def die(self):
        self.time_stop_level()
        self.update_score()
        self.set_time_penalty()
        self.stop_moving = True
        self.fall_sound.play()

        self.time_start_level()
        self.getLevelObject().loadLevel(self.current_level)

    def gameOver(self):
        self.drawUI()
        pygame.display.flip()
        time.sleep(0.5)
        self.game_over_sound.play()
        self.screen.blit(self.black_screen, (0, 0))
        self.screen.blit(self.you_lose_image, (0, 170))
        pygame.display.flip()
        time.sleep(3)
        self.restart = True

    def calcGridOffsets(self):
        self.x_offset = (320 - (((len(self.getLevelObject().getLevelArray())) * self.size)/2))
        self.y_offset = (240 - (((len(self.getLevelObject().getLevelArray()[0])) * self.size)/2))

    def winLevel(self):
        self.time_stop_level()
        self.update_score()
        self.enter_sound.play()
        self.current_level+=1
        self.setCurrentLevel(self.current_level)
        if(self.current_level == 61):
            self.score['wynik'] = time.time() - self.start_game_time + 10 * self.time_penalty - (self.pouse_stop - self.pouse_start)
            self.win()
            self.restart = True
        elif(self.current_level == 30):
            self.set_start_pouse()
            self.pouse()
            self.set_stop_pouse()
        self.getLevelObject().loadLevel(self.current_level)
        self.calcGridOffsets()
        self.time_start_level()
        self.stop_moving = True

    def update_skip(self):
        try:
            self.score[self.level.get_level_number(self.current_level)].append(-1)
        except:
            self.score[self.level.get_level_number(self.current_level)]=[-1]
        self.data[-1]=self.score
        self.update_file_score()

    def skip_maze(self):
	self.time_stop_level()
        self.update_skip()
        self.current_level+=1
        self.setCurrentLevel(self.current_level)
        if(self.current_level == 61):
            self.score['wynik'] = time.time() - self.start_game_time + 10 * self.time_penalty - (self.pouse_stop - self.pouse_start)
            self.win()
            self.restart = True
        elif(self.current_level == 30):
            self.set_start_pouse()
            self.pouse()
            self.set_stop_pouse()
        self.getLevelObject().loadLevel(self.current_level)
        self.calcGridOffsets()
        self.time_start_level()
        self.stop_moving = True

    def pouse(self):
        time.sleep(0.5)
        self.screen.blit(self.black_screen, (0, 0))
        self.screen.blit(self.przerwa, (0, 170))
        pygame.display.flip()

        done=False
        while done == False:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.key==K_SPACE:
                    done = True     

    def win(self):
        for i in range(0, 5, 1):
            time.sleep(0.5)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.flip()
            time.sleep(0.5)
            self.screen.blit(self.you_win_image, (0, 170))
            pygame.display.flip()

    def playIntro(self):
        notDone = True
        self.game_intro_sound.play()
        for event in pygame.event.get():
            while notDone:
                for introy in range(-300, 60, 1):
                    self.screen.blit(self.intro_image, (0, introy))
                    pygame.display.flip()
                    time.sleep(.008)
                self.screen.blit(self.intro_image_2, (0, introy))
                pygame.display.flip()
                notDone = False
            time.sleep(1.5)

    def showInstructions(self):
        notDone = True
        self.screen.blit(self.instructions, (0, 0))
        pygame.display.flip()
        while notDone:
            for event in pygame.event.get():                    
                if (event.type == KEYDOWN):            
                    notDone = False

    def drawUI(self):
        level_text = self.font.render("POZIOM " + str(self.current_level) +"/60", 1, (250, 250, 250))
        lives_text = self.font.render("Czas:" + str(self.get_current_time()), 1, (250, 250, 250))
        self.screen.blit(level_text, (0, 20))
        self.screen.blit(lives_text, (0, 420))


    def setLives(self, _lives):
        self.lives = _lives

    def setCurrentLevel(self, _level):
        self.current_level = _level
        #self.level.loadLevel(self.current_level)

    def getRestartStatus(self):
        return self.restart

    def setRestartStatus(self):
        self.restart = False
    
    def time_start_level(self):
        self.time_start = time.time()

    def time_stop_level(self):
        self.time_stop = time.time()

    def set_start_pouse(self):
        self.pouse_start = time.time()

    def set_stop_pouse(self):
        self.pouse_stop = time.time()

    def get_timelevel(self):
        return self.time_stop - self.time_start

    def set_start_game_time(self):
        self.start_game_time=time.time()

    def set_time_penalty(self):
        self.time_penalty+=1

    def get_current_time(self):
        value = int(time.time() - self.start_game_time + 10 * self.time_penalty - (self.pouse_stop - self.pouse_start))
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(abs(value)/(60*60), abs(value)/60, abs(value)%60)


    def main(self):    
        while(True):
            self.setRestartStatus()
            self.displayMainMenu()
            self.showInstructions()
            self.setLives(5)
            self.setCurrentLevel(1)
            self.level.loadLevel(self.current_level)
            self.set_start_game_time()
            self.time_start_level()
            while(self.getRestartStatus() == False):
                self.update()
                time.sleep(1/self.FRAME_RATE)
    
if __name__ == "__main__":
    main()
