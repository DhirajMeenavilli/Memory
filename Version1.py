import pygame
import random

image1 = pygame.image.load('image1.bmp')
image2 = pygame.image.load('image2.bmp')
image3 = pygame.image.load('image3.bmp')
image4 = pygame.image.load('image4.bmp')
image5 = pygame.image.load('image5.bmp')
image6 = pygame.image.load('image6.bmp')
image7 = pygame.image.load('image7.bmp')
image8 = pygame.image.load('image8.bmp')

pos = {1: (0,0),
       2: (100,0),
       3: (200,0),
       4: (300,0),
       5: (0,100),
       6: (100,100),
       7: (200,100),
       8: (300,100),
       9: (0,200),
       10: (100,200),
       11: (200,200),
       12: (300,200),
       13: (0,300),
       14: (100,300),
       15: (200,300),
       16: (300,300)}

choice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
random.shuffle(choice)

# User-defined functions
def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Memory')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        self.tile1 = Tile(pos[choice[0]][0], pos[choice[0]][1], image1)
        self.tile2 = Tile(pos[choice[1]][0], pos[choice[1]][1], image2)
        self.tile3 = Tile(pos[choice[2]][0], pos[choice[2]][1], image3)
        self.tile4 = Tile(pos[choice[3]][0], pos[choice[3]][1], image4)
        self.tile5 = Tile(pos[choice[4]][0], pos[choice[4]][1], image5)
        self.tile6 = Tile(pos[choice[5]][0], pos[choice[5]][1], image6)
        self.tile7 = Tile(pos[choice[6]][0], pos[choice[6]][1], image7)
        self.tile8 = Tile(pos[choice[7]][0], pos[choice[7]][1], image8)
        self.tile9 = Tile(pos[choice[8]][0], pos[choice[8]][1], image1)
        self.tile10 = Tile(pos[choice[9]][0], pos[choice[9]][1], image2)
        self.tile11 = Tile(pos[choice[10]][0], pos[choice[10]][1], image3)
        self.tile12 = Tile(pos[choice[11]][0], pos[choice[11]][1], image4)
        self.tile13 = Tile(pos[choice[12]][0], pos[choice[12]][1], image5)
        self.tile14 = Tile(pos[choice[13]][0], pos[choice[13]][1], image6)
        self.tile15 = Tile(pos[choice[14]][0], pos[choice[14]][1], image7)
        self.tile16 = Tile(pos[choice[15]][0], pos[choice[15]][1], image8)
        self.max_frames = 150
        self.frame_counter = 0

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS)  # run at most with FPS Frames Per Second

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first

        name1,pos1 = self.tile1.draw()
        self.surface.blit(name1,pos1)

        name2,pos2 = self.tile2.draw()
        self.surface.blit(name2,pos2)

        name3,pos3 = self.tile3.draw()
        self.surface.blit(name3,pos3)

        name4,pos4 = self.tile4.draw()
        self.surface.blit(name4,pos4)

        name5,pos5 = self.tile5.draw()
        self.surface.blit(name5,pos5)

        name6,pos6 = self.tile6.draw()
        self.surface.blit(name6,pos6)

        name7,pos7 = self.tile7.draw()
        self.surface.blit(name7,pos7)

        name8,pos8 = self.tile8.draw()
        self.surface.blit(name8,pos8)

        name9,pos9 = self.tile9.draw()
        self.surface.blit(name9,pos9)

        name10,pos10 = self.tile10.draw()
        self.surface.blit(name10,pos10)

        name11,pos11 = self.tile11.draw()
        self.surface.blit(name11,pos11)

        name12,pos12 = self.tile12.draw()
        self.surface.blit(name12,pos12)

        name13,pos13 = self.tile13.draw()
        self.surface.blit(name13,pos13)

        name14,pos14 = self.tile14.draw()
        self.surface.blit(name14,pos14)

        name15,pos15 = self.tile15.draw()
        self.surface.blit(name15,pos15)

        name16,pos16 = self.tile16.draw()
        self.surface.blit(name16,pos16)

        #self.surface.blit(image1,(100,100))
        pygame.display.update()  # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        if self.frame_counter > self.max_frames:
            self.continue_game = False

class Tile():
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name
    def draw(self):
        return self.name,(self.x,self.y)

main()
