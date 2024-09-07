from kivy.uix.accordion import NumericProperty,BooleanProperty
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
    number_of_players = NumericProperty(2)
    players =[player1,player2]
    end_by_money = BooleanProperty(True)
    end_by_races = BooleanProperty(False)
    end_by_time = BooleanProperty(False)
    def on_number_of_players(self, instance, value):
        if self.number_of_players == 1:
            self.players =[self.player1]
        elif self.number_of_players == 2:
            self.players =[self.player1, self.player2]
        elif self.number_of_players == 3:
            self.players =[self.player1, self.player2, self.player3]
        elif self.number_of_players == 4:
            self.players =[self.player1, self.player2, self.player3, self.player4]
    def set_ending_condition(self, condition):
        if condition == 'money':
            self.end_by_money = True
            self.end_by_races = False
            self.end_by_time =False
        elif condition == 'races':
            self.end_by_money = False
            self.end_by_races = True
            self.end_by_time =False
        elif condition == 'time':
            self.end_by_money = False
            self.end_by_races = False
            self.end_by_time = True
        
class SlugraceApp(App):
    initial_money_min = 10
    initial_money_max = 5000
    max_name_length =10
    def build(self):
        return Game()

if __name__ == '__main__':
    # We need the Window class to change the background color.
    from kivy.core.window import Window

    # Now we can change the color to the same shade of yellow
    # as the screens.
    Window.clearcolor = (1, 1, .8, 1)

    SlugraceApp().run()
