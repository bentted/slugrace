from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')

class SlugraceScreenManager(ScreenManager):
    pass


class SlugraceApp(App):
    def build(self):
        return SlugraceScreenManager()
if __name__=='__main__':
    SlugraceApp().run()