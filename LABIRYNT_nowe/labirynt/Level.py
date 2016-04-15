 #!/usr/bin/env python

import pygame
pygame.mixer.init()
import os, pygame.mixer
pygame.font.init
import random

class Level:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.current_level = 1
        self.loadLevel(self.current_level)

    def get_level_number(self, _level_number):
        return self.random_levels[_level_number-1]

    def loadLevel(self, _level_number):
        
        if(_level_number == 1):   #2.1
            self.level =    [[1,1,1,1,1,1,1,1,1,1],
                             [1,1,1,1,1,2,1,1,1,1],
                             [1,1,0,0,0,0,1,1,1,1],
                             [1,3,0,0,0,0,1,1,1,1],
                             [1,1,0,0,0,0,1,1,1,1],
                             [1,0,0,0,0,0,1,1,1,1],
                             [1,0,0,0,0,0,1,1,1,1],
                             [1,1,0,0,0,0,1,1,1,1],
                             [1,2,0,0,0,4,1,1,1,1],
                             [1,1,1,1,1,1,1,1,1,1]]

        elif(_level_number == 2): #2.2
            self.level =    [[1,1,1,1,1,1,1,1,1,1],
                             [1,0,0,0,2,1,0,0,1,1],
                             [1,0,0,0,1,0,0,0,2,1],
                             [1,0,0,0,0,0,0,0,0,1],
                             [1,0,0,0,0,0,0,0,0,1],
                             [1,0,0,0,0,0,1,1,1,1],
                             [1,3,0,0,0,0,1,1,1,1],
                             [1,1,1,0,0,0,1,1,1,1],
                             [1,1,1,0,0,4,0,0,0,1],
                             [1,1,1,1,1,1,1,1,1,1]]
            
       
        elif(_level_number == 3): #5.5
            self.level =    [[1,1,1,1,1,1,1,1,1,1],
                             [1,1,0,0,0,0,0,0,0,1],
                             [1,0,0,0,0,0,0,0,0,1],
                             [1,0,4,1,0,0,0,0,1,1],
                             [1,2,0,0,0,0,0,0,1,1],
                             [1,0,0,0,0,0,0,0,0,1],
                             [1,1,0,0,0,0,0,0,0,1],
                             [1,0,0,0,2,2,1,1,0,1],
                             [1,0,0,3,0,0,0,0,0,1],
                             [1,1,1,1,1,1,1,1,1,1]] 

        elif(_level_number == 4): #5.6
            self.level =    [[1,1,1,1,1,1,1,1,1,1],
                             [1,0,0,3,1,0,0,0,0,1],
                             [1,0,2,0,0,0,0,0,1,1],
                             [1,0,0,0,0,0,2,0,0,1],
                             [1,0,0,0,1,4,0,0,0,1],
                             [1,0,2,0,0,0,0,0,1,1],
                             [1,0,0,0,0,0,2,0,0,1],
                             [1,0,0,0,1,0,0,0,0,1],
                             [1,0,2,0,0,0,0,0,1,1],
                             [1,1,1,1,1,1,1,1,1,1]] 

        elif(_level_number == 5): #8.10
            self.level =    [[1,1,1,1,1,1,1,1,1,1],
                             [1,0,2,0,2,2,0,0,0,1],
                             [1,0,0,0,2,2,0,2,0,1],
                             [1,0,1,0,0,0,0,0,0,1],
                             [1,0,2,0,0,0,0,2,1,1],
                             [1,0,2,0,0,0,0,2,1,1],
                             [1,0,2,0,1,0,0,0,0,1],
                             [1,4,2,0,2,1,0,0,3,1],
                             [1,0,0,0,2,1,0,0,0,1],
                             [1,1,1,1,1,1,1,1,1,1]]

        for ly in range(0, len(self.getLevelArray()), 1):
            for lx in range(0, len(self.getLevelArray()[0]), 1):
                if(self.getLevelArray()[ly][lx] == 3):
                    self.x = lx
                    self.y = ly

    def getLevelArray(self):
        return self.level

    def getBallX(self):
        return self.x

    def getBallY(self):
        return self.y

    def setBallX(self, _int):
        self.x = _int

    def setBallY(self, _int):
        self.y = _int

            
