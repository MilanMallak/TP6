#TP6
#Par Milan Mallak
import time
from turtledemo.nim import SCREENWIDTH

import animations as anims

import arcade

import game_state

from pyglet.event import EVENT_HANDLE_STATE

import random

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


        self.rss = False
        self.pss = False
        self.sss = False

        self.itemchosen = False
        self.player_choice = int
        self.games_won = 0
        self.games_lost = 0


        self.invisible_sprites = arcade.SpriteList()

        self.RPSicon = arcade.Sprite("Assets/game.png", scale=4)
        self.RPSicon.visible = False
        self.ingameFS = arcade.Sprite(scale=4)
        self.ingameFS.visible = False

        self.invisible_sprites.append(self.RPSicon)
        self.invisible_sprites.append(self.ingameFS)


        self.prioritized_invisible_sprites = arcade.SpriteList() #drawn on top

        self.r_bg = arcade.Sprite("Assets/reading_bg.png", scale=4)
        self.r_bg.visible = False
        self.p_fs = arcade.Sprite("Assets/postit_FS.png", scale=4)
        self.p_fs.visible = False
        self.ok = arcade.create_text_sprite("Ok →", arcade.color.WHITE, font_size=50)
        self.ok.visible = False

        self.prioritized_invisible_sprites.append(self.r_bg)
        self.prioritized_invisible_sprites.append(self.p_fs)
        self.prioritized_invisible_sprites.append(self.ok)


        self.background = arcade.Sprite(scale=4)
        self.button = arcade.Sprite("Assets/button.png")
        self.postit = arcade.Sprite("Assets/postit_s.png", scale=4)
        self.scrn = anims.Animation(anims.AnimationType.STARTUP)
        self.rock = anims.Animation(anims.AnimationType.ROCK)
        self.paper = anims.Animation(anims.AnimationType.PAPER)
        self.scissors = anims.Animation(anims.AnimationType.SCISSORS)

        self.comp_r = arcade.Sprite(scale=3)
        self.comp_r.texture = self.rock.texture
        self.comp_r.color = (15, 15, 15)
        self.comp_r.visible = False
        self.comp_p = arcade.Sprite(scale=3)
        self.comp_p.texture = self.paper.texture
        self.comp_p.color = (15, 15, 15)
        self.comp_p.visible = False
        self.comp_s = arcade.Sprite(scale=3)
        self.comp_s.texture = self.scissors.texture
        self.comp_s.color = (15, 15, 15)
        self.comp_s.visible = False
        self.ok2 = arcade.create_text_sprite("Ok →", arcade.color.WHITE, font_size=40)
        self.ok2.visible = False

        self.invisible_sprites.append(self.comp_r)
        self.invisible_sprites.append(self.comp_p)
        self.invisible_sprites.append(self.comp_s)
        self.invisible_sprites.append(self.ok2)

        self.instructions_visible = False
        self.instructions = arcade.Text("Click on the item you intend to use\n"
                                        "The computer will then randomly select one\n"
                                        "\n"
                                        "Press Esc at any time to quit", 300, 900, arcade.color.WHITE, font_size=15, multiline=True, width=800)

        self.outcome = arcade.Text("", 1400, 900, arcade.color.WHITE, font_size=50)
        self.points_visible = False
        self.points = arcade.Text(f"", 1300, 350, arcade.color.WHITE, font_size=40)


        self.state = game_state.GameState.NOT_STARTED

    def setup(self):

        self.r_bg.alpha = 175

        self.rock.alpha = 0
        self.paper.alpha = 0
        self.scissors.alpha = 0


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
        self.postit.position = (460, 216)
        self.r_bg.position = (960, 540)
        self.p_fs.position = (960, 540)
        self.ok.position = (800, 160)
        self.ok2.position = (1400, 850)
        self.scrn.position = (960, 616)
        self.ingameFS.position = (960, 616)
        self.rock.position = (1152, 370)
        self.paper.position = (960, 370)
        self.scissors.position = (768, 370)
        self.comp_r.position = (960, 896)
        self.comp_p.position = (960, 896)
        self.comp_s.position = (960, 896)
        self.RPSicon.position = (1200, 800)

        self.rock_target_x = self.rock.center_x
        self.rock_target_y = self.rock.center_y

        self.paper_target_x = self.paper.center_x
        self.paper_target_y = self.paper.center_y

        self.scissors_target_x = self.scissors.center_x
        self.scissors_target_y = self.scissors.center_y

    def on_draw(self):
        self.clear()

        with self.camera.activate():
            arcade.draw_sprite(self.scrn, pixelated=True)

            self.invisible_sprites.draw(pixelated=True)

            arcade.draw_sprite(self.background, pixelated=True)
            arcade.draw_sprite(self.button, pixelated=True)
            arcade.draw_sprite(self.postit, pixelated=True)
            arcade.draw_sprite(self.rock, pixelated=True)
            arcade.draw_sprite(self.paper, pixelated=True)
            arcade.draw_sprite(self.scissors, pixelated=True)

            if self.instructions_visible:
                self.instructions.draw()
            self.outcome.draw()
            if self.points_visible:
                self.points.draw()

            self.prioritized_invisible_sprites.draw(pixelated=True)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol == arcade.key.ESCAPE:
            self.target_background_alpha = 255
            self.target_zoom = 1.0
            self.target_position_center_x = 960
            self.target_position_center_y = 540
            self.ingameFS.visible = False
            self.outcome.text = ("")
            self.ok2.visible = False
            self.points_visible = False
            self.comp_r.visible = False
            self.comp_p.visible = False
            self.comp_s.visible = False
            self.instructions_visible = False
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

        elif self.postit.collides_with_point((world_x, world_y)):
            self.r_bg.visible = True
            self.p_fs.visible = True
            self.ok.visible = True

        elif self.ok.collides_with_point((world_x, world_y)):
            self.r_bg.visible = False
            self.p_fs.visible = False
            self.ok.visible = False

        elif self.RPSicon.collides_with_point((world_x, world_y)) and self.state == game_state.GameState.NOT_OPENED:
            anims.Animation.icon_visibility = False #Hide the game icons
            self.ingameFS.visible = True
            self.points_visible = True

            self.target_position_center_x = self.scrn.center_x
            self.target_position_center_y = self.scrn.center_y
            self.target_zoom = 1.4 # 1.9 for wide screen
            self.target_background_alpha = 0

            self.state = game_state.GameState.ROUND_ACTIVE

            self.instructions_visible = True

        elif self.rock.collides_with_point((world_x, world_y)) and self.state == game_state.GameState.ROUND_ACTIVE and self.itemchosen == False:
            self.rock_target_x = 960
            self.rock_target_y = 670
            self.itemchosen = True
            self.player_choice = 0
        elif self.paper.collides_with_point((world_x, world_y)) and self.state == game_state.GameState.ROUND_ACTIVE and self.itemchosen == False:
            self.paper_target_x = 960
            self.paper_target_y = 670
            self.itemchosen = True
            self.player_choice = 1
        elif self.scissors.collides_with_point((world_x, world_y)) and self.state == game_state.GameState.ROUND_ACTIVE and self.itemchosen == False:
            self.scissors_target_x = 960
            self.scissors_target_y = 670
            self.itemchosen = True
            self.player_choice = 2

        elif self.ok2.collides_with_point((world_x, world_y)) and self.state == game_state.GameState.ROUND_DONE:
            self.outcome.text = ("")
            self.ok2.visible = False
            self.comp_r.visible = False
            self.comp_p.visible = False
            self.comp_s.visible = False
            self.rock_target_x = 1152
            self.rock_target_y = 370
            self.paper_target_x = 960
            self.paper_target_y = 370
            self.scissors_target_x = 768
            self.scissors_target_y = 370
            self.itemchosen = False
            self.state = game_state.GameState.ROUND_ACTIVE


    def on_mouse_motion(self, x, y, dx, dy):
        world_x, world_y, _ = self.camera.unproject((x, y))

        if self.rock.collides_with_point((world_x, world_y)):
            self.rock.playing = True
            self.rss = False #rock should stop
        else:
            self.rss = True
        if self.paper.collides_with_point((world_x, world_y)):
            self.paper.playing = True
            self.pss = False
        else:
            self.pss = True
        if self.scissors.collides_with_point((world_x, world_y)):
            self.scissors.playing = True
            self.sss = False
        else:
            self.sss = True


    def on_update(self, delta_time: float) -> bool | None:
        self.scrn.on_update(delta_time)
        self.rock.on_update(delta_time)
        self.paper.on_update(delta_time)
        self.scissors.on_update(delta_time)

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
            self.background_alpha = self.target_background_alpha  # instant fade-in
        elif self.background_alpha > self.target_background_alpha:
            self.background_alpha -= self.fade_speed * delta_time  # gradual fade-out

        self.background.alpha = int(self.background_alpha)
        self.postit.alpha = int(self.background_alpha)

        self.attack_alpha = 250 - self.background_alpha # L'opposé
        self.rock.alpha = self.attack_alpha
        self.paper.alpha = self.attack_alpha
        self.scissors.alpha = self.attack_alpha

        #movement de sprite
        for sprite, tx, ty in [
            (self.rock, self.rock_target_x, self.rock_target_y),
            (self.paper, self.paper_target_x, self.paper_target_y),
            (self.scissors, self.scissors_target_x, self.scissors_target_y),
        ]:
            sprite.center_x += (tx - sprite.center_x) * 5 * delta_time
            sprite.center_y += (ty - sprite.center_y) * 5 * delta_time

        #gérer les animations
        if self.rss == True and self.rock.current_texture == 0 :
            self.rock.playing = False
        if self.pss == True and self.paper.current_texture == 0 :
            self.paper.playing = False
        if self.sss == True and self.scissors.current_texture == 0 :
            self.scissors.playing = False

        self.points.text = (f"You {self.games_won} - Comp {self.games_lost}")

        #roche papier sciseaux
        if self.itemchosen == True and self.state == game_state.GameState.ROUND_ACTIVE:
            self.state = game_state.GameState.ROUND_DONE
            comp_choice = random.randint(0, 2) # 0:r 1:p 2:s
            if comp_choice == 0:
                self.comp_r.visible = True
                if comp_choice == self.player_choice :
                    self.outcome.text = ("It's a tie!")
                elif self.player_choice == 1 :
                    self.outcome.text = ("You win!")
                    self.games_won += 1
                else:
                    self.outcome.text = ("You lose")
                    self.games_lost += 1
            elif comp_choice == 1:
                self.comp_p.visible = True
                if comp_choice == self.player_choice :
                    self.outcome.text = ("It's a tie!")
                elif self.player_choice == 2 :
                    self.outcome.text = ("You win!")
                    self.games_won += 1
                else:
                    self.outcome.text = ("You lose")
                    self.games_lost += 1
            else:
                self.comp_s.visible = True
                if comp_choice == self.player_choice :
                    self.outcome.text = ("It's a tie!")
                elif self.player_choice == 0 :
                    self.outcome.text = ("You win!")
                    self.games_won += 1
                else:
                    self.outcome.text = ("You lose")
                    self.games_lost += 1
            self.ok2.visible = True


def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()
