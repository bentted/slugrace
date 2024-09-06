# File name: main.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')
Builder.load_file('widgets.kv')
Builder.load_file('slug.kv')

from player import Player

class Game(ScreenManager):
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

class SlugraceApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    # We need the Window class to change the background color.
    from kivy.core.window import Window

    # Now we can change the color to the same shade of yellow
    # as the screens.
    Window.clearcolor = (1, 1, .8, 1)

    SlugraceApp().run()
