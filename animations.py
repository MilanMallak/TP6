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

    def __init__(self, type):
        super().__init__()

        self.animation_update_time = 1.0 / Animation.AnimationSpeed
        self.time_since_last_swap = 0.0

        self.type = type
        if self.type == AnimationType.STARTUP:
            self.textures = [
                arcade.load_texture("assets/startup.png"),
                arcade.load_texture("assets/windows95.png"),
            ]
        elif self.type == AnimationType.ROCK:
            self.textures = [
                arcade.load_texture("assets/"),
                arcade.load_texture("assets/"),
            ]
        elif self.type == AnimationType.PAPER:
            self.textures = [
                arcade.load_texture("assets/"),
                arcade.load_texture("assets/"),
            ]
        elif self.type == AnimationType.SCISSORS:
            self.textures = [
                arcade.load_texture("assets/"),
                arcade.load_texture("assets/"),
            ]

        self.scale = self.AnimationScale
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def on_update(self, delta_time: float = 1 / 60):
        # Update the animation.
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0
