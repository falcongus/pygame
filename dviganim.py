"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random
import os

SPRITE_SCALING = 1
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "KILL OR DIE"

COIN_SCALE = 1
COIN_COUNT = 500

VIEWPORT_MARGIN=40


MOVEMENT_SPEED = 5
LEVELx=1000
LEVELy=1000
class Mish(arcade.Sprite):
    mish_textures=[]
    def __init__(self,x,y,w,h):
        super().__init__("sword.png")

        self.center_x=x
        self.center_y=y
        self.angle=45





class heroy(arcade.Sprite):
    hero_textures=[]
    def __init__(self, texture_list):
        super().__init__("ichigoanim/ichigo_stand0.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list
        self.plbegintexture = 0
        self.plendtexture = 0
        self.k=self.center_x
        self.lpose = ""
        self.p=0
        self.pl=1
        self.hp=100
    def update(self):
        if self.hp<=0:
            self.kill()
        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        if self.lpose=="rs":
            self.plbegintexture=0
            self.plendtexture=3
        if self.lpose=="ls":
            self.plbegintexture=4
            self.plendtexture=7
        if self.lpose=="rw":
            self.plbegintexture=8
            self.plendtexture=15

        if self.lpose=="lw":
            self.plbegintexture=16
            self.plendtexture=23

        self.p+=1
        if self.lpose=="rs" or self.lpose=="ls":
            if self.p>=5:
                self.current_texture += 1
                if self.current_texture < len(self.textures):
                    if self.current_texture>=self.plbegintexture and self.current_texture<=self.plendtexture:
                        self.set_texture(self.current_texture)

                    else:
                        self.current_texture=self.plbegintexture
                else:
                    self.current_texture=0
                if self.current_texture >= self.plendtexture:
                    self.current_texture = self.plbegintexture
                self.p=0
        if self.lpose=="rw" or self.lpose=="lw" and self.pl==0 :
            if self.center_x-self.k<=-20 or self.center_x-self.k>=20:
                self.current_texture += 1
                if self.current_texture < len(self.textures):
                    if self.current_texture >= self.plbegintexture and self.current_texture <= self.plendtexture:
                        self.set_texture(self.current_texture)

                    else:
                        self.current_texture = self.plbegintexture
                else:
                    self.current_texture = 0
                if self.current_texture >= self.plendtexture:
                    self.current_texture = self.plbegintexture

                self.k=self.center_x

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)
        self.set_mouse_visible(False)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = None
        self.coin_list = None


        # Set up the player
        self.money = 0
        self.player = None
        self.player_stand=None
        self.wall_list=None
        self.physics_engine=None
        self.view_bottom=0
        self.view_left=0
        self.atak=False
        self.GRAVITY=-5
        self.last_move="right"
        self.movespeed=MOVEMENT_SPEED
        self.onground=False

        self.isjump=False
        self.xx=10
        self.yy=20
        self.player_texture_list=[]

        self.last_x=0
        self.last_y=0

        self.mish = Mish(50, 50,11,30)
        self.level=[
        "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-      -----------                                      --      -----------                                      --      -----------                                      --      -----------                                           -----------                                      --      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                   -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                      -------          --                                      -------           --                                      -------           --                                      -------                                             -------          --                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------     -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                      --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                         -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                         -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------       -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-           --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                          -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-      -----------                                      --      -----------                                       --     -----------                                      --      -----------                                           -----------                                      --      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                   -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                      -------           --                                     -------           --                                      -------           --                                      -------                                             -------          --                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------     -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                      --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                         -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                         -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------       -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-           --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                          -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-      -----------                                      --      -----------                                      --      -----------                                      --      -----------                                           -----------                                      --      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                   -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                      -------           --                                     -------           --                                      -------           --                                      -------                                             -------          --                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------     -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                      --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                         -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                 --                      -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------       -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-           --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                          -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    ]


    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.l=0
        self.LEVELw=50000
        self.LEVELh=2750
        # Set up the player
        self.money = 0
        self.player = arcade.AnimatedWalkingSprite()




        character_scale = 0.85


        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand0.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand1.png",
                                                                    scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand2.png",
                                                                    scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand3.png",
                                                                    scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand0.png",
                                                                   scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand1.png",
                                                                   scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand2.png",
                                                                   scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand3.png",
                                                                   scale=character_scale, mirrored=True))


        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg0.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg1.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg2.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg3.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg4.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg5.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg6.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg7.png",
                                                                   scale=character_scale))


        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg0.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg1.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg2.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg3.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg4.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg5.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg6.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg7.png",
                                                                  scale=character_scale,mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak0.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak1.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak2.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak3.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak4.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak5.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak6.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak0.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak1.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak2.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak3.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak4.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak5.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak6.png",
                                                            scale=character_scale, mirrored=True))

        #self.monster_list.append(self.monster)

        self.hero = heroy(self.player_texture_list)
        self.hero.center_x = 200
        self.hero.center_y = 500


        # -- Set up several columns of walls
        x=0
        y=0
        for row in self.level:
            for col in row:
                if col == "-":
                # Randomly skip a box so the player can find a way through
                #if random.randrange(5) > 0:
                    wall = arcade.Sprite("LazyList/tanks_crateWood.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y

                    self.wall_list.append(wall)
                x+=50
            y+=50
            x=0




        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coin.png", COIN_SCALE)

            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(10000)
                coin.center_y = random.randrange(2750)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)








        self.physics_engine=arcade.PhysicsEngineSimple(self.hero,self.coin_list)
        #self.physics_engine1=arcade.PhysicsEngineSimple(self.monster,self.wall_list)
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.wall_list.draw()
        self.hero.draw()
        self.mish.draw()
        #self.monster.draw()




        # Put the text on the screen.
        output = f"Gold: {self.money}"
        output1=f"HP: {self.hero.hp}"
        arcade.draw_text(output, self.xx,self.yy, arcade.color.WHITE, 14)
        arcade.draw_text(output1,self.xx,self.yy+570,arcade.color.ALABAMA_CRIMSON,20)
    def on_mouse_motion(self, x, y,dx,dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.mish.center_x = x
        self.mish.center_y = y
    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
       # if key == arcade.key.UP:
        #   self.hero.change_y = self.movespeed
        #elif key == arcade.key.DOWN:
        #    self.player.change_y = -self.movespeed
        if key == arcade.key.A:
            self.hero.change_x = -self.movespeed
            self.last_move="left"
            self.hero.lpose="lw"
            self.hero.pl=0
        elif key == arcade.key.D:
            self.hero.change_x = self.movespeed
            self.last_move="right"
            self.hero.lpose="rw"
            self.hero.pl=0
        elif key== arcade.key.P:
            self.atak=True
        elif key== arcade.key.LSHIFT and self.hero.center_x<self.LEVELw-1000 and self.hero.center_y<self.LEVELh-250 and self.hero.center_y>50 and self.hero.center_x>500:
            self.movespeed=25
        elif key==arcade.key.SPACE:
            if self.onground==True:
                self.isjump=True
                self.jumpcount=7


    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.hero.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.hero.change_x = 0
            self.hero.pl=1
            if self.last_move=="left":
                self.hero.lpose="ls"
            else:
                self.hero.lpose="rs"
            self.l=0
        elif key==arcade.key.P:
            self.atak=False
        elif key==arcade.key.LSHIFT or not(self.hero.center_x<self.LEVELw-1000 and self.hero.center_y<self.LEVELh-250 and self.hero.center_y>250 and self.hero.center_x>500 ):
            self.movespeed=5

    def update(self, delta_time):
        """ Movement and game logic """
        changed=False
        self.l+=1
        self.onground=False

        self.last_x=self.hero.center_x
        self.last_y=self.hero.center_y
        self.physics_engine.update()

        self.coin_list.update()
        self.coin_list.update_animation()

        #self.player_list.update()
        #self.player_list.update_animation()
        if self.hero.center_x==self.last_x and self.hero.center_y==self.last_y and self.l==10:
            if self.last_move=="left":
                self.hero.lpose="ls"
            else:
                self.hero.lpose="rs"
            self.l=0
        self.hero.update()
        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.hero , self.coin_list)
        for wall in self.wall_list:
            if (self.hero.center_x+10+100>wall.center_x and self.hero.center_x+10+100<wall.center_x+50) and ((self.hero.center_y+70>wall.center_y and self.hero.center_y+70<wall.center_y+50) or (self.hero.center_y>wall.center_y and self.hero.center_y<wall.center_y+50)):
                self.hero.set_position(wall.center_x-100,self.hero.center_y)
            if (self.hero.center_x-20>wall.center_x and self.hero.center_x-20<wall.center_x+50) and ((self.hero.center_y+70>wall.center_y and self.hero.center_y+70<wall.center_y+50) or (self.hero.center_y>wall.center_y and self.hero.center_y<wall.center_y+50)):
                self.hero.set_position(wall.center_x+70,self.hero.center_y)
            if ((self.hero.center_x+100>wall.center_x and self.hero.center_x+100<wall.center_x+50) or (self.hero.center_x>wall.center_x and self.hero.center_x<wall.center_x+50)) and  (self.hero.center_y-20>wall.center_y and self.hero.center_y-20<wall.center_y+50):
                self.hero.set_position(self.hero.center_x,wall.center_y+70)
                self.onground= True
            if ((self.hero.center_x+100>wall.center_x and self.hero.center_x+100<wall.center_x+50) or (self.hero.center_x>wall.center_x and self.hero.center_x<wall.center_x+50)) and  (self.hero.center_y+10+70>wall.center_y and self.hero.center_y+10+70<wall.center_y+50):
                self.hero.set_position(self.hero.center_x,wall.center_y-80)
                self.onground=True
        self.hero.center_y+=self.GRAVITY


        if self.isjump:
            if self.jumpcount>=-7:
                if self.jumpcount<0:
                    self.hero.center_y-=(self.jumpcount**2)/2
                else:
                    self.hero.center_y+=(self.jumpcount**2)/2
                self.jumpcount-=0.1
            else:
                self.isjump=False
                self.jumpcount=7
            for wall in self.wall_list:
                if ((self.hero.center_x + 10 + 100 > wall.center_x and self.hero.center_x + 10 + 100 < wall.center_x + 50) and (self.hero.center_y + 70 > wall.center_y and self.hero.center_y + 70 < wall.center_y + 50) or (self.hero.center_y > wall.center_y and self.hero.center_y < wall.center_y + 50)):
                    self.hero.set_position(wall.center_x - 100, self.hero.center_y)
                if (self.hero.center_x - 20 > wall.center_x and self.hero.center_x - 20 < wall.center_x + 50) and ((self.hero.center_y + 70 > wall.center_y and self.hero.center_y + 70 < wall.center_y + 50) or (self.hero.center_y > wall.center_y and self.hero.center_y < wall.center_y + 50)):
                    self.hero.set_position(wall.center_x + 70, self.hero.center_y)
                if ((self.hero.center_x + 100 > wall.center_x and self.hero.center_x + 100 < wall.center_x + 50) or (self.hero.center_x > wall.center_x and self.hero.center_x < wall.center_x + 50)) and (self.hero.center_y - 20 > wall.center_y and self.hero.center_y - 20 < wall.center_y + 50):
                    self.hero.set_position(self.hero.center_x, wall.center_y + 70)
                    self.onground = True
                    self.isjump=False
                if ((self.hero.center_x + 100 > wall.center_x and self.hero.center_x + 100 < wall.center_x + 50) or (self.hero.center_x > wall.center_x and self.hero.center_x < wall.center_x + 50)) and (self.hero.center_y + 10 + 70 > wall.center_y and self.hero.center_y + 10 + 70 < wall.center_y + 50):
                    self.hero.set_position(self.hero.center_x, wall.center_y - 80)
                    self.onground = True
                    self.jumpcount=0
                    self.isjump=False




        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.money += 1

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.hero.left < left_bndry:
            self.view_left -= left_bndry - self.hero.left
            self.xx=self.view_left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.hero.right > right_bndry:
            self.view_left += self.hero.right - right_bndry
            self.xx=self.view_left
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.hero.top > top_bndry:
            self.view_bottom += self.hero.top - top_bndry
            self.yy=self.view_bottom
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.hero.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.hero.bottom
            self.yy=self.view_bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()