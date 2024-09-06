# File name: race.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import NumericProperty, StringProperty
from kivy.lang import Builder

# Besides Screen we have to import ScreenManager.
from kivy.uix.screenmanager import Screen, ScreenManager


# Load the Bets and Results kv files.
Builder.load_file('bets.kv')
Builder.load_file('results.kv')

# Here's the screen manager class.
class RaceScreenManager(ScreenManager):
    pass

class SlugStats(BoxLayout):
    name = StringProperty('')
    wins = NumericProperty(0)
    win_percent = NumericProperty(0)

class PlayerStats(BoxLayout):
    name = StringProperty('')
    money = NumericProperty(0)

class SlugInfo(BoxLayout):
    y_position = NumericProperty(0)
    name = StringProperty('')
    wins = NumericProperty(0)

class RaceScreen(Screen):
    pass

class RaceApp(App):
    def build(self):
        return RaceScreen()

