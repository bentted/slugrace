
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

class TestApp(App):
    def build(self):
        return FloatLayout()
    
if __name__ == '__main__':
    TestApp().run()