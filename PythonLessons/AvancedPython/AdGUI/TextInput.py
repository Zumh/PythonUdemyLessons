# This example is goint to change using mouse click

# It great for gaming

import os
import sys
import random

import pygame as pg

CAPTION = "Click to Change My Color"
SCREEN_SIZE = (500, 500)

class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface() #Get reference to the display
        self.clock = pg.time.Clock() #Create a clock to restrict framerate
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed() # All keys currently held
        self.color = pg.Color("black")

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type ==pg.MOUSEBUTTONDOWN:
                self.color = [random.randint(0,255) for _ in range(3)]
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys = pg.key.get_pressed()

    def main_loop(self):

        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            pg.display.update()
            self.clock.tick(self.fps)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1' #create the window (optional)
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    App().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
