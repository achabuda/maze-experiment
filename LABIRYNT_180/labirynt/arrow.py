 #!/usr/bin/env python
 
import os
import time

import pygame
from pygame.locals import *

import numpy as np

from arrows import DrawArrow


if __name__ == '__main__':
    pygame.init()
    okno = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Labirynt')
    arrow = DrawArrow(okno, (120, 120), 'top')
    arrow.init_draw_arrow()
    level=10
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    key_down=True
                    while pygame.event.get()==[]:
                        level+=1
                        print level
                        time.sleep(0.3)
                        arrow.draw_level(level)
            print 'level:', level
            
