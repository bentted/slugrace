
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '0')
class RaceScreen(BoxLayout):
    pass
class RaceApp(App):
    def build(self):
        return RaceScreen()

if __name__=='__main__':
    RaceApp().run()