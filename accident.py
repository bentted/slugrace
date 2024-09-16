#file name : accident.py 
from abc import ABC
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.clock import Clock

from random import choice


class Accident(ABC):
    intro = "BREAKING NEWS:"
    def __init__(self, name,
                 headlines,
                 sound,
                 position=0,
                 slug = None,
                 image = None,
                 game = None):
        self.name = name
        self.headlines = headlines
        self.sound = SoundLoader.load(sound)
        self.position = position
        self.slug = slug
        self.image = image
        self.game = game
        
    def happen(self, autoplay = True, loop=False):
        if loop:
            self.sopund.loop = True
        if autoplay:
            self.sound.play()
        headline = choice(self.headlines)
        label = Label(markup = True,
                      text = f'[b][color=ff3333]{self.slug.name} {headline}[/color][/b]',
                      text_size =(400, 100),
                      halign = 'left',
                      valign = 'center')
        popup_image = Image(source = self.slug.front_image, size_hint= (.2,1))
        content = BoxLayout()
        content.add_widget(popup_image)
        content.add_widget(label)
        popup = Popup(title = self.intro,
                      title_color = [.9, .2, 0, 1],
                      content = content,
                      size_hint = (None, None),
                      size = (600, 150),
                      pos_hint = {'center_x':.5,'top':.2},
                      background_color =[0, 0, 0, .2])
    
        popup.open()
    def reset(self):
        pass
class BrokenLegAccident(Accident):
    name = 'Broken Leg'
    headlines = [
        "just broke his leg and is grounded!",
        "broke his leg, which is practically all he consists of!",
        "suffered from an open fracture. All he can do now is watch the others win!",
        "broke his only leg and now looks pretty helpless!",
        "tripped over a root and broke his leg!"
        ]
    sound = 'assets/sounds/Accidents/Broken Leg.mp3'
    
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
        self.slug.run_animation.stop(self.slug)
        self.slug.eye_animation.cancel(self.slug) 
        self.slug.normal_image = self.slug.body.source
        self.slug.body.source = ('atlas://assets/accidents/accidents/nroken leg'
                                 + self.slug.name.lower())
        self.slug.body.x += 10
    def reset(self):
        self.slug.body.source = self.slug.normal_image
        self.slug.body.x -= 10
class OverheatAccident(Accident):
    name = 'Overheat'
    headlines = [
        "has been running faster than he should have.He burned of overheat!",
        "burned by friction. needs to cool down a bit before the next race!",
        "roasted on the track from overheat. he's been running way to fast!",
        "looks like he has been running faster than his body cooling system can handle!",
        "shouldn't have been speeding like that. Ovcerheating can be dangerous!"
        ]
    sound = 'assets/sounds/Accidents/Overheat.mp3'
    
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
        self.slug.run_animation.stop(self.slug)
        self.slug.eye_animation.cancel(self.slug)
        self.slug.normal_body_image = self.slug.body.source
        self.slug.normal_eye_image = self.slug.left_eye.source
        self.slug.body.source = 'atlas://assets/accidents/accidents/overheat body'
        self.slug.left_eye.source = 'atlas://assets/accidents/accidents/overheat eye'
    def reset(self):
        self.slug.body.source = self.slug.normal_body_image
        self.slug.left_eye_source = self.slug.normal_eye_image
        self.slug.right_eye_source = self.slug.normal_eye_image
        self.slug.eye_animation.start(self.slug)
class HeartAttackAccident(Accident):
    name = 'Heart Attack'
    headlines = [
        "Had a heart attack. Definitely needs a rest!",
        "Had a poor heart condition. hadn't he stopped now, it could have killed him!",
        "Beaten by cardiac infarction. he'd better go to hospital asap!",
        "Almost killed by heart attack. He had a really narrow escape!",
        "Beaten by his weak heart! he better get some rest!"
        ]
    sound = 'assets/sounds/Accidents/heart attack.mp3'
    image = 'atlas://assets/accidents/accidents/heart attack'

    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen(loop=True)
        self.slug.run_animation.stop(self.slug)
        self.heart - Image(source=self.image)
        self.heart.size_hint = .8,.8
        self.heart.x + 40
        self.heart.y + 3
        self.slug.add_widget(self.heart)
        self.heart_animation = (Animation(size_hint = (.6,.6,), 
                                duration = .2, t ='out_back') 
                                +Animation(size_hint=(.8,.8),
                                duration = .62, t='out_back'))
        self.heart_animation.repeat = True
        self.heart_animation.start(self.heart)
    def reset(self):
        self.sound.stop()
        self.heart_animation.cancel(self.heart)
        self.slug.remove_widget(self.heart)
class GrassAccident(Accident):
    name = 'Grass'
    headlines = [
        "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how important sleep is.Even if it's not the best time for that!"
        ]
    sound = 'assets/sounds/Accidents/Grass.mp3'
    image = 'atlas://assets/accidents/accidents/grass'

    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
        self.slug.run_animation.stop(self.slug)
        self.grass = Image(source= self.image)
        self.grass.x = self.slug.body.x + 90
        self.slug.add_widget(self.grass, index=-1)
        Clock.schedule_once(self.continue_race, 2)
    def continue_race(self, dt):
        self.slug.remove_widget(self.grass)
        self.sound.stop()
        self.slug.run(acceleration=10).start(self.slug)
        self.slug.run_animation.bind(on_progress=self.game.while_running)
        self.slug.run_animation.bind(on_complete=self.game.finish_race)
    def reset(self):
        pass
        
class AsleepAccident(Accident):
    name = 'Asleep'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Asleep.mp3'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass

class BlindAccident(Accident):
    name = 'Blind'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Blind.mp3'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
class PuddleAccident(Accident):
    name = 'Puddle'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Drown.mp3'
    image = 'atlas://assets/accidents/accidents/puddle'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
class ElectroshockAccident(Accident):
    name = 'Electroshock'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Electroshock.mp3'
    image = 'atlas://assets/accidents/accidents/electroshock'
    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
class TurningBackAccident(Accident):
    name = 'Turning Back'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Turning Back.mp3'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
class ShootingEyesAccident(Accident):
    name = 'Shooting Eyes'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Shooting Eyes.mp3'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
class RubberizedAccident(Accident):
    name = 'Rubberized'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Rubberizer.mp3'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
class DevouredAccident(Accident):
    name = 'Devoured'
    headlines = [
          "just fell asleep for a while after the long and wearisome running!",
        "having a nap. He again has chosen just the perfect time for that!",
        "sleeping instead of running. It's getting one of his bad habits!",
        "always takes a shoirt nape at this time of the day, no matter what he's doing!",
        "knows how importanr sleep is.Even if it's not the best time for that!"
        
        ]
    sound = 'assets/sounds/Accidents/Devoured.mp3'
    image = 'atlas://assets/accidents/accidents/slug monster'
    def __init__(self,**kwargs):
        super().__init__(name=self.name, headlines=self.headlines,
                         sound = self.sound, **kwargs)
    def happen(self):
        super().happen()
    def reset(self):
        pass
accident = Accident()
print(accident)
