 #!/usr/bin/env python

from labirynt.Screen_exp import Screen
import numpy as np

def main():
    file_ = np.load('./labirynt/wyniki.npy')
    Game = Screen(file_)
    Game.main()


if __name__ == "__main__":
    main()
