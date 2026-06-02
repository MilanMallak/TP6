#TP6
#Par Milan Mallak
import time
from turtledemo.nim import SCREENWIDTH

import animations as anims

import arcade

import game_state

from pyglet.event import EVENT_HANDLE_STATE

WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
WINDOW_TITLE = "Drawing"

class GameView(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, fullscreen=True)

        self.camera = arcade.Camera2D() #Camera for "zoom in"s
        self.camera.zoom = 1.0
        self.target_zoom = 1.0
        self.zoom_speed = 1.5
        self.target_position_center_x = 960
        self.target_position_center_y = 540

        self.background_alpha = 255  # For "fade out"s
        self.target_background_alpha = 255
        self.fade_speed = 100

        self.invisible_sprites = arcade.SpriteList()

        self.RPSicon = arcade.Sprite("Assets/game.png", scale=4)
        self.RPSicon.visible = False
        self.ingameFS = arcade.Sprite(scale=4)
        self.ingameFS.visible = False

        self.invisible_sprites.append(self.RPSicon)
        self.invisible_sprites.append(self.ingameFS)

        self.background = arcade.Sprite(scale=4)
        self.button = arcade.Sprite("Assets/button.png")
        self.scrn = anims.Animation(anims.AnimationType.STARTUP)

        self.state = game_state.GameState.NOT_STARTED

    def setup(self):

        bg1 = arcade.load_texture("Assets/background_1.png")
        bg2 = arcade.load_texture("Assets/background_2.png")
        self.background.textures.append(bg1)
        self.background.textures.append(bg2)
        self.background.set_texture(0)

        #different minigame screens
        RPSscrn = arcade.load_texture("Assets/RPSbg.png")
        #aucun autre minijeux pour l'instant
        self.ingameFS.textures.append(RPSscrn)
        self.ingameFS.set_texture(0)


        self.background.position = (960, 540)
        self.button.position = (1742, 52)
        self.scrn.position = (960, 616)
        self.ingameFS.position = (960, 616)
        self.RPSicon.position = (1200, 800)

    def on_draw(self):
        self.clear()

        with self.camera.activate():
            arcade.draw_sprite(self.scrn, pixelated=True)

            self.invisible_sprites.draw(pixelated=True)

            arcade.draw_sprite(self.background, pixelated=True)
            arcade.draw_sprite(self.button, pixelated=True)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol == arcade.key.ESCAPE:
            self.target_background_alpha = 255
            self.target_zoom = 1.0
            self.target_position_center_x = 960
            self.target_position_center_y = 540
            self.ingameFS.visible = False
            anims.Animation.icon_visibility = True
            self.state = game_state.GameState.NOT_OPENED

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> EVENT_HANDLE_STATE:

        world_x, world_y, _ = self.camera.unproject((x, y))

        if self.button.collides_with_point((world_x, world_y)):

            if game_state.GameState.NOT_STARTED == self.state:
                self.background.set_texture(1)

                self.state = game_state.GameState.NOT_OPENED
                self.scrn.playing = True
            else :
                arcade.close_window()

        elif self.RPSicon.collides_with_point((world_x, world_y)) and self.state == game_state.GameState.NOT_OPENED:
            anims.Animation.icon_visibility = False #Hide the game icons
            self.ingameFS.visible = True

            self.target_position_center_x = self.scrn.center_x
            self.target_position_center_y = self.scrn.center_y
            self.target_zoom = 1.8
            self.target_background_alpha = 0

            self.state = game_state.GameState.INTRUCTIONS


    def on_update(self, delta_time: float) -> bool | None:
        self.scrn.on_update(delta_time)

        #Make the game icons visible
        self.RPSicon.visible = anims.Animation.icon_visibility
        #There is only on game for now

        #camera position
        self.camera.position = (
            self.camera.position[0] + (self.target_position_center_x - self.camera.position[0]) * 5 * delta_time,
            self.camera.position[1] + (self.target_position_center_y - self.camera.position[1]) * 5 * delta_time,
        )

        #zoom
        if self.camera.zoom < self.target_zoom:
            self.camera.zoom += (self.target_zoom - self.camera.zoom) * 5 * delta_time
        elif self.camera.zoom > self.target_zoom:
            self.camera.zoom -= (self.target_zoom + self.camera.zoom) * 5 * delta_time

        #fade
        if self.background_alpha < self.target_background_alpha:
            self.background_alpha += self.fade_speed * delta_time
        elif self.background_alpha > self.target_background_alpha:
            self.background_alpha -= self.fade_speed * delta_time

        self.background.alpha = int(self.background_alpha)


def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()
