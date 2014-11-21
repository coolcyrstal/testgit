import pygame
from pygame.locals import *
from gamelib import SimpleGame
 
class SquashGame(SimpleGame):
    pass
 
def main():
    game = SquashGame('SquashGame')
    game.run()
 
if __name__ == '__main__':
    main()

def init(self):
	super(SquashGame, self).init()