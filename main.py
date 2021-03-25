"""
-------------------------------------------------------------------------------
Name:   main.py
Purpose:  PyGame assignment based on an article that was found on Flipboard in order to raise awareness about computers and technology.
 
Author: Wang.K
 
Created: 03/03/2021
------------------------------------------------------------------------------
"""
 
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0,   255)
ORANGE    = (   0,   0,   0)
YELLOW    = (   0,   0,   0)
PURPLE    = (   0,   0,   0)
LIGHTGREEN    = (   0,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
screen_width = 1200
screen_height = 750
size = (1150, 700)
screen = pygame.display.set_mode(size)

#Names the window at the top 
pygame.display.set_caption("Kevin's Computer Kiosk")

 
#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Loads all the images that is displayed to the user.
background_image = pygame.image.load("background.jpg").convert()

pc_image = pygame.image.load("pc.png").convert()
pc_image.set_colorkey(BLACK)

software_image = pygame.image.load("software.png").convert()
software_image.set_colorkey(BLACK)

scene = 0

#Sets the posltiion and the velocity for the animated lock

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  

    # --- Game logic should go here
    
    #Animates the moving image
    

    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    
    #Displays the images onto the screen
    screen.blit(background_image, [0, 0])
    
    #Defines the mouse position and clicks
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  
    # --- Drawing button code should go here 
    if scene == 0:  
      pygame.draw.rect(screen, GREEN, (100,535,175,50) )
      pygame.draw.rect(screen, RED, (900,535,175,50) )
      pygame.draw.rect(screen, BLUE, (500,535,175,50) )

      if 100+175 > mouse[0] > 100 and 535+50 > mouse[1] > 535:
        if click[0] == 1:
          scene = 1
        
      elif 900+175 > mouse[0] > 900 and 535+50 > mouse[1] > 535:
        if click[0] == 1:
          scene = 2

      elif 500+175 > mouse[0] > 500 and 535+50 > mouse[1] > 535:
        if click[0] == 1:
          scene = 3

    # Logic and drawings for scene 1    
    if scene == 1:

      # Drawing code
      pygame.draw.rect(screen, BLUE, (20,20,170,35) )
      pygame.draw.rect(screen, WHITE, (20,235,120,20) )
      pygame.draw.rect(screen, WHITE, (12,280,120,20) )
      pygame.draw.rect(screen, WHITE, (40,500,120,20) )
      pygame.draw.rect(screen, WHITE, (300,135,120,20) )
      pygame.draw.rect(screen, WHITE, (530,250,120,20) )
      pygame.draw.rect(screen, WHITE, (530,440,120,20) )
      
      screen.blit(pc_image, [0, 0])

      # Logic
      if 20+170 > mouse[0] > 20 and 20+35 > mouse[1] > 20:
        if click[0] == 1:
          scene = 0
      
      if 20+120 > mouse[0] > 20 and 235+20 > mouse[1] > 235:
        if click[0] == 1:
          print("motherboard")

      if 12+120 > mouse[0] > 12 and 280+20 > mouse[1] > 280:
        if click[0] == 1:
          print("GPU")

      if 40+120 > mouse[0] > 40 and 500+20 > mouse[1] > 500:
        if click[0] == 1:
          print("Power Supply")

      if 300+120 > mouse[0] > 300 and 135+20 > mouse[1] > 135:
        if click[0] == 1:
          print("CPU")
        
      if 530+120 > mouse[0] > 530 and 250+20 > mouse[1] > 250:
        if click[0] == 1:
          print("RAM")

      if 530+440 > mouse[0] > 530 and 440+20 > mouse[1] > 440:
        if click[0] == 1:
          print("Storage")
        
    
    # Logic and drawings for scene 2 
    if scene == 2:

      # Drawing code
      pygame.draw.rect(screen, BLUE, (20,20,170,35) )
      pygame.draw.rect(screen, WHITE, (295,427,155,30) )
      pygame.draw.rect(screen, WHITE, (295,290,155,30) )
      pygame.draw.rect(screen, WHITE, (295,570,155,30) )
      pygame.draw.rect(screen, WHITE, (295,155,155,30) )
      screen.blit(software_image, [0, 0])

      
      # Logic
      if 20+170 > mouse[0] > 20 and 170+35 > mouse[1] > 35:
        if click[0] == 1:
          scene = 0
      

    # Logic and drawings for scene 3 
    if scene == 3:

      # Drawing code
      pygame.draw.rect(screen, BLUE, (20,20,170,35) )
      
      # Logic
      if 20+170 > mouse[0] > 20 and 170+35 > mouse[1] > 35:
        if click[0] == 1:
          scene = 0

      
      
      
    # --- Go ahead and update the screen with what we've drawn.
    
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    pygame.display.flip()
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()