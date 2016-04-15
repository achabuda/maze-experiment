 #!/usr/bin/env python

import pygame
from pygame.locals import *

import numpy as np

class Arrow(object):
    def __init__(self, levels):
        self.levels = levels

    def find_point_x(self, x, y, level_x):
        a, b = np.polyfit(x, y, 1)
        return (level_x, level_x*a+b)

    def find_point_y(self, x, y, level_y):
        a, b = np.polyfit(x, y, 1)
        return ((level_y-b)/a, level_y)

    def init_shape(self, position):
        pass

    def get_level_points(self, level):
        pass

    def get_shape_level_points(self):
        pass


class RightArrow(Arrow):
    def __init__(self, levels=[45,90]):
        super(RightArrow, self).__init__(levels)
        
    def init_shape(self, position):
        point1 = (position[0]+  0, position[1]-27)
        point2 = (position[0]+  0, position[1]+27)
        point3 = (position[0]+ 45, position[1]+27)
        point4 = (position[0]+ 45, position[1]+68)
        point5 = (position[0]+120, position[1]+ 0)
        point6 = (position[0]+ 45, position[1]-68)
        point7 = (position[0]+ 45, position[1]-27)
        self.points = (point1, point2, point3, point4, point5, point6, point7)

    def get_shape_level_points(self):
        line1_1 = self.find_point_x([self.points[3][0], self.points[4][0]],
                                    [self.points[3][1], self.points[4][1]],
                                    self.points[1][0]+self.levels[0])
        line1_2 = self.find_point_x([self.points[4][0], self.points[5][0]],
                                    [self.points[4][1], self.points[5][1]],
                                    self.points[1][0]+self.levels[0])
        line2_1 = self.find_point_x([self.points[3][0], self.points[4][0]],
                                    [self.points[3][1], self.points[4][1]],
                                    self.points[1][0]+self.levels[1])
        line2_2 = self.find_point_x([self.points[4][0], self.points[5][0]],
                                    [self.points[4][1], self.points[5][1]],
                                    self.points[1][0]+self.levels[1])
        return (line1_1, line1_2), (line2_1, line2_2)

    def get_level_points(self, level):
        if level <= self.levels[0]:
            points = (self.points[0], 
                      self.points[1], 
                      (self.points[1][0]+level, self.points[2][1]), 
                      (self.points[1][0]+level, self.points[6][1]))
            return 'yellow', points
        elif level<120:
            points = (self.points[0], 
                      self.points[1], 
                      self.points[2], 
                      self.points[3], 
                      self.find_point_x([self.points[3][0], self.points[4][0]],
                                        [self.points[3][1], self.points[4][1]],
                                        self.points[0][0]+level),
                      self.find_point_x([self.points[4][0], self.points[5][0]],
                                        [self.points[4][1], self.points[5][1]],
                                        self.points[0][0]+level),
                      self.points[5], 
                      self.points[6])
            if level < self.levels[1]:
                return 'green', points
            else:
                return 'red', points
        else:
            return 'red', self.points

class LeftArrow(Arrow):
    def __init__(self, levels=[45,90]):
        super(LeftArrow, self).__init__(levels)

    def init_shape(self, position):
        point1 = (position[0]-  0, position[1]-27)
        point2 = (position[0]-  0, position[1]+27)
        point3 = (position[0]- 45, position[1]+27)
        point4 = (position[0]- 45, position[1]+68)
        point5 = (position[0]-120, position[1]+ 0)
        point6 = (position[0]- 45, position[1]-68)
        point7 = (position[0]- 45, position[1]-27)
        self.points = (point1, point2, point3, point4, point5, point6, point7)  

    def get_shape_level_points(self):
        line1_1 = self.find_point_x([self.points[3][0], self.points[4][0]],
                                    [self.points[3][1], self.points[4][1]],
                                    self.points[1][0]-self.levels[0])
        line1_2 = self.find_point_x([self.points[4][0], self.points[5][0]],
                                   [self.points[4][1], self.points[5][1]],
                                   self.points[1][0]-self.levels[0])
        line2_1 = self.find_point_x([self.points[3][0], self.points[4][0]],
                                   [self.points[3][1], self.points[4][1]],
                                   self.points[1][0]-self.levels[1])
        line2_2 = self.find_point_x([self.points[4][0], self.points[5][0]],
                                   [self.points[4][1], self.points[5][1]],
                                   self.points[1][0]-self.levels[1])
        return (line1_1, line1_2), (line2_1, line2_2)

    def get_level_points(self, level):
        if level <= self.levels[0]:
            points = (self.points[0], 
                      self.points[1], 
                      (self.points[1][0]-level, self.points[2][1]), 
                      (self.points[1][0]-level, self.points[6][1]))
            return 'yellow', points
        elif level<120:
            points = (self.points[0], 
                      self.points[1], 
                      self.points[2], 
                      self.points[3], 
                      self.find_point_x([self.points[3][0], self.points[4][0]],
                                        [self.points[3][1], self.points[4][1]],
                                        self.points[1][0]-level),
                      self.find_point_x([self.points[4][0], self.points[5][0]],
                                        [self.points[4][1], self.points[5][1]],
                                        self.points[1][0]-level),
                      self.points[5], 
                      self.points[6])
            if level < self.levels[1]:
                return 'green', points
            else:
                return 'red', points
        else:
            return 'red', self.points
        
class TopArrow(Arrow):
    def __init__(self, levels=[45,90]):
        super(TopArrow, self).__init__(levels)

    def init_shape(self, position):
        point1 = (position[0]-27, position[1]- 0)
        point2 = (position[0]+27, position[1]- 0)
        point3 = (position[0]+27, position[1]- 45)
        point4 = (position[0]+68, position[1]- 45)
        point5 = (position[0]+ 0, position[1]-120)
        point6 = (position[0]-68, position[1]- 45)
        point7 = (position[0]-27, position[1]- 45)
        self.points = (point1, point2, point3, point4, point5, point6, point7)  

    def get_shape_level_points(self):
        line1_1 = self.find_point_x([self.points[0][0], self.points[1][0]],
                                    [self.points[0][1]-self.levels[0],self.points[1][1]-self.levels[0]],
                                    self.points[0][0])
        line1_2 = self.find_point_x([self.points[0][0], self.points[1][0]],
                                    [self.points[0][1]-self.levels[0], self.points[1][1]-self.levels[0]],
                                    self.points[1][0])
        line2_1 = self.find_point_y([self.points[5][0], self.points[4][0]],
                                    [self.points[5][1], self.points[4][1]],
                                    self.points[0][1]-self.levels[1])
        line2_2 = self.find_point_y([self.points[4][0], self.points[3][0]],
                                    [self.points[4][1], self.points[3][1]],
                                    self.points[0][1]-self.levels[1])
        return (line1_1, line1_2), (line2_1, line2_2)

    def get_level_points(self, level):
        if level <= self.levels[0]:
            points = (self.points[0], 
                      self.points[1], 
                      (self.points[1][0], self.points[1][1]-level),
                      (self.points[0][0], self.points[0][1]-level))

            return 'yellow', points
        elif level<120:
            points = (self.points[0], 
                      self.points[1], 
                      self.points[2], 
                      self.points[3], 
                      self.find_point_y([self.points[4][0], self.points[3][0]],
                                        [self.points[4][1], self.points[3][1]],
                                         self.points[0][1]-level),
                      self.find_point_y([self.points[5][0], self.points[4][0]],
                                        [self.points[5][1], self.points[4][1]],
                                        self.points[0][1]-level),
                      self.points[5], 
                      self.points[6])
            if level < self.levels[1]:
                return 'green', points
            else:
                return 'red', points
        else:
            return 'red', self.points

class DownArrow(Arrow):
    def __init__(self, levels=[45,90]):
        super(DownArrow, self).__init__(levels)

    def init_shape(self, position):
        point1 = (position[0]-27, position[1]+ 0)
        point2 = (position[0]+27, position[1]+ 0)
        point3 = (position[0]+27, position[1]+ 45)
        point4 = (position[0]+68, position[1]+ 45)
        point5 = (position[0]+ 0, position[1]+120)
        point6 = (position[0]-68, position[1]+ 45)
        point7 = (position[0]-27, position[1]+ 45)
        self.points = (point1, point2, point3, point4, point5, point6, point7)

    def get_shape_level_points(self):
        line1_1 = self.find_point_x([self.points[0][0], self.points[1][0]],
                                    [self.points[0][1]+self.levels[0],self.points[1][1]+self.levels[0]],
                                    self.points[0][0])
        line1_2 = self.find_point_x([self.points[0][0], self.points[1][0]],
                                    [self.points[0][1]+self.levels[0], self.points[1][1]+self.levels[0]],
                                    self.points[1][0])
        line2_1 = self.find_point_y([self.points[5][0], self.points[4][0]],
                                    [self.points[5][1], self.points[4][1]],
                                    self.points[0][1]+self.levels[1])
        line2_2 = self.find_point_y([self.points[4][0], self.points[3][0]],
                                    [self.points[4][1], self.points[3][1]],
                                    self.points[0][1]+self.levels[1])
        return (line1_1, line1_2), (line2_1, line2_2)

    def get_level_points(self, level):
        if level <= self.levels[0]:
            points = (self.points[0], 
                      self.points[1], 
                      (self.points[1][0], self.points[1][0]+level),
                      (self.points[0][0], self.points[0][0]+level))

            return 'yellow', points
        elif level<120:
            points = (self.points[0], 
                      self.points[1], 
                      self.points[2], 
                      self.points[3], 
                      self.find_point_y([self.points[4][0], self.points[3][0]],
                                        [self.points[4][1], self.points[3][1]],
                                         self.points[0][1]+level),
                      self.find_point_y([self.points[5][0], self.points[4][0]],
                                        [self.points[5][1], self.points[4][1]],
                                        self.points[0][1]+level),
                      self.points[5], 
                      self.points[6])
            if level < self.levels[1]:
                return 'green', points
            else:
                return 'red', points
        else:
            return 'red', self.points


class DrawArrow(object):
    colors = {'black'  : (  0,   0,   0),
              'white'  : (255, 255, 255),
              'yellow' : (255, 255,   0),
              'green'  : (  0, 255,   0),
              'red'    : (255,   0,   0)}

    def __init__(self, window, type_):
        self.window = window
        if type_ == 'right':
            self.arrow = RightArrow()
        elif type_ == 'left':
            self.arrow = LeftArrow()
        elif type_ == 'top':
            self.arrow = TopArrow()
        elif type_ == 'down':
            self.arrow = DownArrow()
    def init_position(self, position):
        self.arrow.init_shape(position)

    def draw_black_shape_arrow(self):
        line1, line2 = self.arrow.get_shape_level_points()
        pygame.draw.line(self.window, self.colors['black'], line1[0], line1[1], 2)
        pygame.draw.line(self.window, self.colors['black'], line2[0], line2[1], 2)
        pygame.draw.polygon(self.window, self.colors['black'], self.arrow.points, 3)

    def draw_white_fill_arrow(self):
        pygame.draw.polygon(self.window, self.colors['white'], self.arrow.points)


    def init_draw_arrow(self):
        self.draw_white_fill_arrow()
        self.draw_black_shape_arrow()
        self.display()

    def draw_level(self, level):
        color, points = self.arrow.get_level_points(level)
        pygame.draw.polygon(self.window, self.colors[color], points)
        self.draw_black_shape_arrow()
        self.display()

    def display(self):
        pygame.display.flip()



