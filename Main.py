#TP6
#Par Milan Mallak

from turtledemo.nim import SCREENWIDTH

import arcade
from pyglet.event import EVENT_HANDLE_STATE

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
WINDOW_TITLE = "Drawing"

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, fullscreen=True)

        self.background = arcade.Sprite("Assets/background.png", scale=4)
        self.button = arcade.Sprite("Assets/button.png")

    def setup(self):

        self.background.position = (960, 540)
        self.button.position = (1742, 52)

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.background, pixelated=True)
        arcade.draw_sprite(self.button, pixelated=True)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> EVENT_HANDLE_STATE:
        pass




def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()