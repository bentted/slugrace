# File name: bets.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen

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

