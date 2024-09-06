# File name: bets.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
Builder.load_file('widgets.kv')

class Bet(BoxLayout):
    player_name = StringProperty('')
    bet_amount = NumericProperty(0)
    max_bet_amount = NumericProperty(0)
    player_group = StringProperty('')

class BetsScreen(Screen):
    pass

class BetsApp(App):
    def build(self):
        return BetsScreen()

if __name__ == '__main__':
    BetsApp().run()