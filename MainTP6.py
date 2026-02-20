#TP6
#Par Milan Mallak

from turtledemo.nim import SCREENWIDTH

import arcade

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800
WINDOW_TITLE = "Drawing"

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        self.clear()



def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()