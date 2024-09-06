
from kivy.config import Config 
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.lang import Builder
Builder.load_file('widgets.kv')
from kivy.uix.screenmanager import Screen


class GameoverScreen(Screen):
    pass
class GameoverApp(App):
    def build(self):
        return GameoverScreen()
    
if __name__ == '__main__':
    GameoverApp().run()