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

    def setup(self):
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        self.clear()

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