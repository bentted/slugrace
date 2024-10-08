# File name: main.py

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675')
Config.set('graphics', 'resizable', '0')

# Let's get rid of the window border.
Config.set('graphics', 'borderless', '1')

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from player import Player
from kivy.properties import (NumericProperty, BooleanProperty,
                             StringProperty,  ObjectProperty)
from datetime import timedelta
from random import choice, randint
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from accident import *

Builder.load_file('settings.kv')
Builder.load_file('race.kv')
Builder.load_file('gameover.kv')
Builder.load_file('widgets.kv')
Builder.load_file('slug.kv')
Builder.load_file('instructions.kv')

# We have to load the Splash screen.
Builder.load_file('splash.kv')

class Game(ScreenManager):
    # the players
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

    number_of_players = NumericProperty(2)
    players = [player1, player2]
    potential_players = [player1, player2, player3, player4]

    # ending conditions
    end_by_money = BooleanProperty(True)
    end_by_races = BooleanProperty(False)
    end_by_time = BooleanProperty(False)

    # races
    number_of_races = NumericProperty(0)
    races_finished = NumericProperty(0)
    races_to_go = NumericProperty(0)
    race_number = NumericProperty(1)
    race_winner = ObjectProperty(None, allownone=True)
    finish_line = 850

    # time
    time_set_delta = timedelta()  # duration
    time_set = StringProperty('') # string representation of duration

    time_elapsed_delta = timedelta()   # duration
    time_elapsed = StringProperty('')  # string representation of duration

    time_remaining_delta = timedelta()   # duration
    time_remaining = StringProperty('')  # string representation of duration

    # game over
    winners = []
    game_over_reason = StringProperty('')
    winner_text = StringProperty('')
    game_is_over = BooleanProperty(False)

    # Sound
    sound_on = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        game_sounds = 'assets/sounds/Game/'
        slug_sounds = 'assets/Sounds/Slugs Winning/'

        # game
        self.background_music = SoundLoader.load(game_sounds + 'Background Music.mp3')
        self.slugs_running_sound = SoundLoader.load(game_sounds + 'Slugs Running.mp3')
        self.gameover_sound = SoundLoader.load(game_sounds + 'Game Over.mp3')
        self.go_sound = SoundLoader.load(game_sounds + 'Go.mp3')

        # slugs
        self.speedster.win_sound = SoundLoader.load(slug_sounds + 'Speedster Win.mp3')
        self.trusty.win_sound = SoundLoader.load(slug_sounds + 'Trusty Win.mp3')
        self.iffy.win_sound = SoundLoader.load(slug_sounds + 'Iffy Win.mp3')
        self.slowpoke.win_sound = SoundLoader.load(slug_sounds + 'Slowpoke Win.mp3')

        # default volumes
        self.slugs_running_sound.volume = .2
        self.go_sound.volume = .1
        self.gameover_sound.volume = .1

        # sounds
        self.sounds = [self.background_music,
                       self.slugs_running_sound,
                       self.gameover_sound,
                       self.go_sound,
                       self.speedster.win_sound,
                       self.trusty.win_sound,
                       self.iffy.win_sound,
                       self.slowpoke.win_sound]

        # background music
        self.background_music.volume = .1
        self.background_music.loop = True
        self.background_music.play()

        # accidents
        self.acc_broken_leg = BrokenLegAccident()
        self.acc_overheat = OverheatAccident()
        self.acc_heart_attack = HeartAttackAccident()
        self.acc_grass = GrassAccident()
        self.acc_asleep = AsleepAccident()
        self.acc_blind = BlindAccident()
        self.acc_puddle = PuddleAccident()
        self.acc_electroshock = ElectroshockAccident()
        self.acc_turning_back = TurningBackAccident()
        self.acc_shooting_eyes = ShootingEyesAccident()
        self.acc_rubberized = RubberizedAccident()
        self.acc_devoured = DevouredAccident()

        self.accidents = [self.acc_broken_leg,
                          self.acc_overheat,
                          self.acc_heart_attack,
                          self.acc_grass,
                          self.acc_asleep,
                          self.acc_blind,
                          self.acc_puddle,
                          self.acc_electroshock,
                          self.acc_turning_back,
                          self.acc_shooting_eyes,
                          self.acc_rubberized,
                          self.acc_devoured]

        self.accident = None

    # callback methods
    def on_number_of_players(self, instance, value):
        if self.number_of_players == 1:
            self.players = [self.player1]
        elif self.number_of_players == 2:
            self.players = [self.player1, self.player2]
        elif self.number_of_players == 3:
            self.players = [self.player1, self.player2, self.player3]
        elif self.number_of_players == 4:
            self.players = [self.player1, self.player2, self.player3, self.player4]

    def set_ending_condition(self, condition):
        if condition == 'money':
            self.end_by_money = True
            self.end_by_races = False
            self.end_by_time = False
        elif condition == 'races':
            self.end_by_money = False
            self.end_by_races = True
            self.end_by_time = False
        elif condition == 'time':
            self.end_by_money = False
            self.end_by_races = False
            self.end_by_time = True

    def start_game(self):
        if self.end_by_time:
            self.time_event = Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        # Add one second to elapsed time.
        self.time_elapsed_delta += timedelta(seconds=1)
        self.time_elapsed = str(self.time_elapsed_delta)

        # Subtract one second from remaining time.
        self.time_remaining_delta -= timedelta(seconds=1)
        self.time_remaining = str(self.time_remaining_delta)

        # Unschedule the update_time method if the time has elepased.
        if self.time_remaining_delta.seconds == 0:
            self.time_event.cancel()

            self.gameover()

    def go(self, screen_manager):
        self.go_sound.play()
        self.slugs_running_sound.loop = True
        self.slugs_running_sound.play()

        for slug in self.slugs:
            anim = slug.run()
            anim.bind(on_progress=self.while_running)
            anim.bind(on_complete=self.finish_race)
            anim.start(slug)

        self.race_manager = screen_manager

        # Accident
        self.accident_expected = (randint(0, 3) == 0
                                  if self.race_number > 5
                                  else False)
        if self.accident_expected:
            self.accident = choice(self.accidents)
            self.accident.position = randint(290, 500)
            self.accident.slug = choice(self.slugs)
            if self.accident.slug == self.trusty:
                self.accident.slug = choice(self.slugs)
            self.accident.game = self

    def while_running(self, animation, slug, progression):
        if slug.shooting:
            slug.front = slug.right + slug.translation_left.x + slug.left_eye.width
        elif slug.rubberized:
            slug.front = slug.x + (slug.body.width + slug.left_eye.width) * slug.x_scale
        else:
            slug.front = slug.right

        if slug.front > self.finish_line:
            if not self.race_winner:
                self.race_winner = slug
                slug.win_sound.play()

                for player in self.players:
                    player.update(self.race_winner)

                for slug in self.slugs:
                    slug.update(self.race_winner, self.race_number)

                self.remove_bankrupt_players()
                self.gameover_check()

        # Accident
        if self.accident_expected and slug == self.accident.slug:
            if self.accident.position < slug.x < self.accident.position + 10:
                self.accident.happen()
                self.accident_expected = False

    def finish_race(self, animation, slug):
        slug.finished = True
        if (self.speedster.finished
            and self.trusty.finished
            and self.iffy.finished
            and self.slowpoke.finished):
            self.race_manager.current = 'resultsscreen'
            self.race_manager.transition.direction = 'left'
            self.slugs_running_sound.stop()

    def remove_bankrupt_players(self):
        self.players = [player for player in self.players if not player.bankrupt]

    def gameover_check(self):
        if (len(self.players) == 0
            or (len(self.players) == 1 and self.number_of_players > 1)
            or (self.end_by_races and self.race_number == self.number_of_races)
            or (self.end_by_time and self.time_remaining_delta.seconds == 0)):
            self.gameover()

    def gameover(self, manual=False):
        self.winners = []

        # all players go bankrupt
        if len(self.players) == 0:

            # 1-player mode
            if self.number_of_players == 1:
                self.game_over_reason = 'You just went bankrupt.'
                self.winner_text = 'There are no winners in 1-player mode.'

            # multi-player mode
            else:
                self.game_over_reason = 'All players are bankrupt.'
                self.winner_text = 'There is no winner!'

        # one player left in multi-player mode
        elif len(self.players) == 1 and self.number_of_players > 1:
            self.winners.append(self.players[0])
            self.game_over_reason = "There's only one player with any money left."
            winner = self.winners[0]
            self.winner_text = (f'The winner is {winner.name}, ' +
                                f'having started at ${winner.initial_money}, ' +
                                f'winning at ${winner.money}.')

        # after a given number of races, after the game time has elapsed
        # or if the game was ended manually
        elif ((self.end_by_races and self.race_number == self.number_of_races)
              or (self.end_by_time and self.time_remaining_delta.seconds == 0)
              or manual):

            if manual:
                self.game_over_reason = 'You ended the game manually.'
            elif self.end_by_races:
                self.game_over_reason = 'The number of races you set has been reached.'
            else:
                self.game_over_reason = 'The game time you set is up.'

            if self.number_of_players == 1:
                you = self.players[0]
                self.winner_text = (f"You were playing in 1-player mode." +
                                    f"\nYou started at ${you.initial_money} " +
                                    f"and you're ending at ${you.money}.")

            else:
                max_money = (max(*self.players, key=lambda player: player.money)).money
                self.winners = [player for player in self.players
                                if player.money == max_money]

                # one winner
                if len(self.winners) == 1:
                    winner = self.winners[0]
                    self.winner_text = (f'The winner is {winner.name}, ' +
                                       f'having started at ${winner.initial_money}, ' +
                                       f'winning at ${winner.money}.')

                # joint winners
                else:
                    self.winner_text = "There's a tie. The joint winners are:\n\n"
                    for winner in self.winners:
                        self.winner_text += (f'{winner.name}, ' +
                                            f'having started at ${winner.initial_money}, ' +
                                            f'winning at ${winner.money}.\n')

        self.game_is_over = True
        delay = 0 if manual else 4
        self.gameover_event = Clock.schedule_once(self.gameover_screen, delay)

    def gameover_screen(self, dt):
        self.background_music.stop()

        for sound in self.sounds:
            if sound != self.gameover_sound:
                sound.unload()

        self.gameover_sound.play()
        self.current = 'gameoverscreen'
        self.gameover_event.cancel()

    def reset_race(self):
        self.race_number += 1
        self.races_finished += 1
        self.races_to_go -= 1

        for player in self.players:
            player.reset()

        self.race_winner = None

        for slug in self.slugs:
            slug.reset()

        self.reset_accidents()

    def reset_players(self):
        for player in self.potential_players:
            player.reset(gameover = True)

    def mute_unmute(self, instance, value):
        if value == 'down':
            self.sound_on = False
            for sound in self.sounds:
                sound.default_volume = sound.volume
                sound.volume = 0
        else:
            self.sound_on = True
            for sound in self.sounds:
                sound.volume = sound.default_volume

    def reset_accidents(self):
        if self.accident:
            self.accident.reset()
            self.accident = None

class SlugraceApp(App):
    # General Settings
    initial_money_min = 10
    initial_money_max = 5000
    max_name_length = 10

    def restart(self):
        self.root.clear_widgets()
        self.game = Game()
        self.game.opacity = 0
        self.root.add_widget(self.game)
        self.show_event = Clock.schedule_interval(self.show, .01)

    def show(self, dt):
        self.game.opacity += .01
        if self.game.opacity >= 1:
            self.game.opacity = 1
            self.show_event.cancel()

    def build(self):
        self.root = FloatLayout()
        self.root.add_widget(Game())
        return self.root

    def quit(self):
        confirm_popup = Popup(title='Confirmation Required',
                              title_color=[1, 0, 0, 1],
                              size_hint=(None, None),
                              size=(400, 200),
                              pos_hint={'center_x': .5, 'center_y:': .5},
                              background_color=[1, 0, 0, .3],
                              auto_dismiss=False)

        content = BoxLayout(orientation='vertical')

        confirm_label = Label(text='Are you sure you want to quit?')

        cancel_button = Button(text='No, I was wrong. Cancel.')
        cancel_button.bind(on_press=lambda x: confirm_popup.dismiss())

        confirm_button=Button(text="Yes, I’m sure. Quit.")
        confirm_button.bind(on_press=lambda x: self.stop())

        buttons = BoxLayout()
        buttons.add_widget(cancel_button)
        buttons.add_widget(confirm_button)

        content.add_widget(confirm_label)
        content.add_widget(buttons)

        confirm_popup.content = content
        confirm_popup.open()

if __name__ == '__main__':
    from kivy.core.window import Window
    Window.clearcolor = (1, 1, .8, 1)
    SlugraceApp().run()