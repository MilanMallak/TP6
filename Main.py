#TP6
#Par Milan Mallak
import time
from turtledemo.nim import SCREENWIDTH

import animations

import arcade
from game_state import GameState

from pyglet.event import EVENT_HANDLE_STATE

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
WINDOW_TITLE = "Drawing"

computer_active = False

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, fullscreen=True)

        self.background = arcade.Sprite(scale=4)
        self.button = arcade.Sprite("Assets/button.png")
        self.scrn = animations.Animation(animations.AnimationType.STARTUP)

    def setup(self):

        bg1 = arcade.load_texture("Assets/background_1.png")
        bg2 = arcade.load_texture("Assets/background_2.png")
        self.background.textures.append(bg1)
        self.background.textures.append(bg2)
        self.background.set_texture(0)

        #startup = arcade.load_texture("Assets/startup.png")
        #w95 = arcade.load_texture("Assets/windows95.png")
        #self.scrn.textures.append(startup)
        #self.scrn.textures.append(w95)
        #self.scrn.set_texture(0)

        self.background.position = (960, 540)
        self.button.position = (1742, 52)
        self.scrn.position = (960, 616)

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.scrn, pixelated=True)
        arcade.draw_sprite(self.background, pixelated=True)
        arcade.draw_sprite(self.button, pixelated=True)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if self.button.collides_with_point((x, y)):
            global computer_active

            if computer_active == False :
                self.background.set_texture(1)
                #self.scrn.set_texture(1)

                computer_active = True
            else :
                arcade.close_window()



def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()