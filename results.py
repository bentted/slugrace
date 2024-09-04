from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '0')

class ResultsScreen(BoxLayout):
    pass
class ResultsApp(App):
    def build(self):
        return ResultsScreen()
if __name__=='__main__':
    ResultsApp().run()