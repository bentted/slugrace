from kivy.config import Config 
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class GameOverScreen(BoxLayout):
    pass
class GameOverApp(App):
    def build(self):
        return GameOverScreen()
    
if __name__ == '__main__':
    GameOverApp().run()