 #!/usr/bin/env python

import pygame
pygame.mixer.init()
import os, pygame.mixer
pygame.font.init
import random
import numpy as np
from conf_level import LEVELS, LEVELS_GROUP

class Level:
    def __init__(self, current_level=1):
        self.x = 0
        self.y = 0
        self.current_level = current_level
        self.random_levels = []
        for i in range(1, len(LEVELS_GROUP.keys())+1):
            a = LEVELS_GROUP[str(i)]
            random.shuffle(a)
            self.random_levels.append(a)
        self.random_levels = sum(self.random_levels, [])
        self.loadLevel(self.current_level)
        self.maze_number = len(LEVELS.keys())

    def get_level_number(self, _level_number):
        return self.random_levels[_level_number-1]
   

    def loadLevel(self, _level_number):
        if _level_number <=388:
            self.level_number = self.random_levels[_level_number-1]
            self.level = LEVELS[str(self.level_number)]
            for ly in range(0, len(self.getLevelArray()), 1):
                for lx in range(0, len(self.getLevelArray()[0]), 1):
                    if(self.getLevelArray()[ly][lx] == 3):
                        self.x = lx
                        self.y = ly

    def getAllLevels(self):
        return self.levels_number

    def getLevelGroup(self):
        for i in LEVELS_GROUP.keys():
            if self.level_number in LEVELS_GROUP[i]:
                return i

    def getAllMaze(self):
        return self.maze_number

    def getLevelNumber(self):
        return self.level_number

    def getLevelType(self):
        return self.type_maze

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

            
