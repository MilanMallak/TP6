import arcade
from enum import Enum

class AnimationType(Enum):
    STARTUP = 0
    ROCK = 1,
    PAPER = 2,
    SCISSORS = 3

class Animation(arcade.Sprite):
    AnimationScale = 4
    AnimationSpeed = 2.0

    icon_visibility = False

    def __init__(self, type):
        super().__init__()

        self.playing = False
        self.type = type

        SPEEDS = {
            AnimationType.STARTUP: 2.0,
            AnimationType.ROCK: 2.0,
            AnimationType.PAPER: 3.0,
            AnimationType.SCISSORS: 6.0
        }
        speed = SPEEDS[self.type]
        self.animation_update_time = 1.0 / speed

        self.time_since_last_swap = 0.0

        if self.type == AnimationType.STARTUP:
            self.time_since_last_swap = -1.0
            self.textures = [
                arcade.load_texture("assets/startup.png"),
                arcade.load_texture("assets/windows95.png"),
                arcade.load_texture("assets/desktop.png")
            ]
        elif self.type == AnimationType.ROCK:
            self.textures = [
                arcade.load_texture("assets/R0.png"),
                arcade.load_texture("assets/R1.png"),
                arcade.load_texture("assets/R2.png"),
            ]
        elif self.type == AnimationType.PAPER:
            self.textures = [
                arcade.load_texture("assets/P0.png"),
                arcade.load_texture("assets/P1.png"),
                arcade.load_texture("assets/P2.png"),
                arcade.load_texture("assets/P1.png"),
            ]
        elif self.type == AnimationType.SCISSORS:
            self.textures = [
                arcade.load_texture("assets/S0.png"),
                arcade.load_texture("assets/S1.png"),
                arcade.load_texture("assets/S2.png"),
                arcade.load_texture("assets/S1.png"),
            ]

        self.scale = self.AnimationScale
        self.current_texture = 0
        self.set_texture(self.current_texture)
        print(self.animation_update_time)

    def on_update(self, delta_time: float = 1 / 60):
        if self.playing == True :

            # Update the animation.
            if self.type == AnimationType.STARTUP :

                self.time_since_last_swap += delta_time
                if self.time_since_last_swap > self.animation_update_time:
                    if self.current_texture == 1 :
                        self.current_texture = 2
                        Animation.icon_visibility = True
                    elif self.current_texture == 0 :
                        self.current_texture = 1

                    self.set_texture(self.current_texture)
                    self.time_since_last_swap = -1.0

            else :
                self.time_since_last_swap += delta_time
                if self.time_since_last_swap > self.animation_update_time:
                    self.current_texture = (self.current_texture+1)%len(self.textures)
                    self.set_texture(self.current_texture)
                    self.time_since_last_swap = 0.0
