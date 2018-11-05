# this file was created by Maxim Koretsky

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((480,600))
        pg.display.set_caption("jumpy")
        self.clock = pg.time.Clock()
        self.running = True
        # init pygame and create...
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()
        # create new player object
    def run(self):
        self.playing = True
        while self.player:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        # game loop
    def update(self):
        self.all_sprites.update()

        # update things
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
            self.running = False

        # listening for events
    def draw(self):
        self.screen.fill(REDDISH)
        self.all_sprites.draw(self.screen)
        # Double buffer
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()