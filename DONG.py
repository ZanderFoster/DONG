import pygame
from sys import exit

# Initialize Pygame
pygame.init()

# Set up the display window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BIG DONG")

# Define the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set game status messages
font1 = pygame.font.SysFont('chalkduster.ttf', 72)
font2 = pygame.font.SysFont('chalkduster.ttf', 42)
imgP1Win = font1.render('Player 1 WINS!', True, GREEN)
imgP2Win = font1.render('Player 2 WINS!', True, GREEN)
imgReset = font2.render('Press ESC to quit or Enter to continue', True, RED)



# Circle class
class Circle:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = 10
        self.direction = 1, 0.5
        self.status = 0

    def update(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        # Check for collision with screen edges
        if self.x - self.radius < 0:
            if self.y + self.radius in range(player1_location[0], player1_location[1]) or self.y - self.radius in range(player1_location[0], player1_location[1]):
                self.direction = (-self.direction[0], self.direction[1])
                print("hit player1 ")
            else:
                print("miss player1 ")
                self.status = 1

        if self.x + self.radius > width:
            if self.y + self.radius in range(player2_location[0], player2_location[1]) or self.y - self.radius in range(player2_location[0], player2_location[1]):
                self.direction = (-self.direction[0], self.direction[1])
                print("hit player2 ")
            else:
                print("miss player2 ")
                self.status = 2

        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.direction = (self.direction[0], -self.direction[1])
        
    def getStatus(self):
        return self.status

    def reset(self):
        self.status = 0
        self.x = width // 2
        self.y = height // 2

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)



#class paddle
class Paddle:
    def __init__(self, side, color):
        self.color = color
        self.y = 0
        self.thickness = 4
        self.length = 100
        self.speed = 10
        if side == 'left':
            self.x = 0
        else:
            self.x = width - self.thickness

    def move(self, direction):
        if direction == 0:
            if self.y + self.length + self.speed > height:
                print("y+ limit reached")
            else:
                self.y = self.y + self.speed
        elif direction == 1:
            if self.y - self.speed < 0:
                print("y- limit reached")
            else:
                self.y = self.y - self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.thickness, self.length), 0)
    
    def getLocation(self):
        return self.y, self.y + self.length



def checkKeys():
    pressed_keys = pygame.key.get_pressed()
    if  pressed_keys[pygame.K_ESCAPE]:
        running = False
    
    # Update player1 input
    if pressed_keys[pygame.K_w]:
        print("P1: UP")
        player1.move(1)
    elif pressed_keys[pygame.K_s]:
        print("P1: DOWN")
        player1.move(0)

    # Update player2 input
    if pressed_keys[pygame.K_UP]:
        print("P2: UP")
        player2.move(1)
    elif pressed_keys[pygame.K_DOWN]:
        print("P2: DOWN")
        player2.move(0)             


# Create pong
pong = Circle(width // 2, height // 2, RED, 10)

# Create players
player1 = Paddle('left', GREEN)
player2 = Paddle('right', GREEN)



# Game loop Setup
running = True
clock = pygame.time.Clock()


# MAIN GAME LOOP
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pong.getStatus() == 0:
        # Update circles
        pong.update()

        # Update location of paddels
        player1_location = player1.getLocation()
        player2_location = player2.getLocation()

        # Update Inputs
        checkKeys()
            
        

        # Clear the screen
        screen.fill(BLACK)

        # Update Graphics
        pong.draw()
        player1.draw()
        player2.draw()
        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

    elif pong.status == 1:
        print("Player 2 WINS!!!")
    
        # Display win message
        screen.blit(imgP2Win, (width // 2 - (imgP2Win.get_width() // 2), height // 2 - imgP2Win.get_height()))
        screen.blit(imgReset, (width // 2 - (imgReset.get_width() // 2), height // 2 + imgP2Win.get_height()))
        pygame.display.flip()
        
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                pong.reset()
        

        clock.tick(60)
    elif pong.status == 2:
        print("Player 1 WINS!!!")
    
        # Display win message
        screen.blit(imgP1Win, (width // 2 - (imgP1Win.get_width() // 2), height // 2 - imgP1Win.get_height()))
        screen.blit(imgReset, (width // 2 - (imgReset.get_width() // 2), height // 2 + imgP1Win.get_height()))
        pygame.display.flip()
        
         
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                pong.reset()
        

        clock.tick(60)
    # Quit the game
pygame.quit()
