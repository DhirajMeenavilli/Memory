import pygame
import random

image0 = pygame.image.load('image0.bmp')
image1 = pygame.image.load('image1.bmp')
image2 = pygame.image.load('image2.bmp')
image3 = pygame.image.load('image3.bmp')
image4 = pygame.image.load('image4.bmp')
image5 = pygame.image.load('image5.bmp')
image6 = pygame.image.load('image6.bmp')
image7 = pygame.image.load('image7.bmp')
image8 = pygame.image.load('image8.bmp')

image = [image1,image2,image3,image4,image5,image6,image7,image8]

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

#for i in range(16):
    #Tile(pos[i][0],pos[i][1],image0)


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
        self.score = 0
        self.randoms = []
        self.images = []
        for i in range(16):
            self.randoms.append(Tile(pos[i+1][0],pos[i+1][1],image0))
            self.images.append(Tile(pos[choice[i]][0],pos[choice[i]][1],image[i%8]))
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

        pressed = pygame.mouse.get_pressed()
        popped = []
        clicked = 0
        if pressed[0] == 1:
            clicked += 1
            for i in range(len(self.randoms)):
                if pygame.mouse.get_pos()[0] > self.randoms[i].x and pygame.mouse.get_pos()[0] < self.randoms[i].x + 100:
                    if pygame.mouse.get_pos()[1] > self.randoms[i].y and pygame.mouse.get_pos()[1] < self.randoms[i].y + 100:
                        popped.append(i)

        self.score += len(popped)

        for i in range(len(popped)):
            self.randoms.pop(popped[i])

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color)  # clear the display surface first
        for i in range(len(self.images)):
            nameI,posI = self.images[i].draw()
            self.surface.blit(nameI,posI)
        for i in range(len(self.randoms)):
            nameR,posR = self.randoms[i].draw()
            self.surface.blit(nameR,posR)

        font = pygame.font.SysFont("arial", 25, True)
        text = font.render('Score:' + str(self.score), 1, (245, 56, 78))
        self.surface.blit(text, (400, 0))

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
