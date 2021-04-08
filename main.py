"""
-------------------------------------------------------------------------------
Name:   main.py
Purpose:  A program that acts as a "computer kiosk" and allows the user to click on buttons to learn new things about computers. (CPT)
 
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

home_image = pygame.image.load("HomePage.png").convert()
home_image.set_colorkey(BLACK)

cpu_image = pygame.image.load("cpu.png").convert()
cpu_image.set_colorkey(BLACK)

gpu_image = pygame.image.load("gpu.png").convert()
gpu_image.set_colorkey(BLACK)

ram_image = pygame.image.load("ram.png").convert()
ram_image.set_colorkey(BLACK)

mobo_image = pygame.image.load("motherboard.png").convert()
mobo_image.set_colorkey(BLACK)

storage_image = pygame.image.load("storage.png").convert()
storage_image.set_colorkey(BLACK)

psu_image = pygame.image.load("psu.png").convert()
psu_image.set_colorkey(BLACK)

os_image = pygame.image.load("os.png").convert()
os_image.set_colorkey(BLACK)

multimedia_image = pygame.image.load("multimedia.png").convert()
multimedia_image.set_colorkey(BLACK)

browser_image = pygame.image.load("browser.png").convert()
browser_image.set_colorkey(BLACK)

productivity_image = pygame.image.load("productivity.png").convert()
productivity_image.set_colorkey(BLACK)

scene = 0

#Sets the posltiion and the velocity for the animated lock

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  

    # --- Game logic should go here
    
    #Displays the images onto the screen
    screen.blit(background_image, [0, 0])
    
  
    
    #Defines the mouse position and clicks
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  
    # --- Drawing button code should go here 
    if scene == 0:  

      pygame.draw.rect(screen, GREEN, (100,535,175,50) )
      pygame.draw.rect(screen, RED, (900,535,175,50) )
    
      screen.blit(home_image, [0, 0])
  
      if 100+175 > mouse[0] > 100 and 535+50 > mouse[1] > 535:
        if click[0] == 1:
          scene = 1
        
      elif 900+175 > mouse[0] > 900 and 535+50 > mouse[1] > 535:
        if click[0] == 1:
          scene = 2

      

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
          screen.blit(mobo_image, [0, 0])
          

      if 12+120 > mouse[0] > 12 and 280+20 > mouse[1] > 280:
        if click[0] == 1:
          screen.blit(gpu_image, [0, 0])
          

      if 40+120 > mouse[0] > 40 and 500+20 > mouse[1] > 500:
        if click[0] == 1:
          screen.blit(psu_image, [0, 0])
          

      if 300+120 > mouse[0] > 300 and 135+20 > mouse[1] > 135:
        if click[0] == 1:
          screen.blit(cpu_image, [0, 0])
          
        
      if 530+120 > mouse[0] > 530 and 250+20 > mouse[1] > 250:
        if click[0] == 1:
          screen.blit(ram_image, [0, 0])
          

      if 530+440 > mouse[0] > 530 and 440+20 > mouse[1] > 440:
        if click[0] == 1:
          screen.blit(storage_image, [0, 0])       
    
    # Logic and drawings for scene 2 
    if scene == 2:

      # Drawing code
      pygame.draw.rect(screen, BLUE, (20,20,170,35) )
      #Operating System
      pygame.draw.rect(screen, WHITE, (295,155,155,30) )
      #multimedia
      pygame.draw.rect(screen, WHITE, (295,290,155,30) )
      #web browser
      pygame.draw.rect(screen, WHITE, (295,427,155,30) )
      #productivity
      pygame.draw.rect(screen, WHITE, (295,570,155,30) )
      
      screen.blit(software_image, [0, 0])

      # Logic
      if 20+170 > mouse[0] > 20 and 170+35 > mouse[1] > 35:
        if click[0] == 1:
          scene = 0

      if 295+155 > mouse[0] > 295 and 155+30 > mouse[1] > 155:
        if click[0] == 1:
          screen.blit(os_image, [0, 0])
          

      if 295+155 > mouse[0] > 295 and 290+30 > mouse[1] > 290:
        if click[0] == 1:
          screen.blit(multimedia_image, [0, 0])
          

      if 295+155 > mouse[0] > 295 and 427+30 > mouse[1] > 427:
        if click[0] == 1:
          screen.blit(browser_image, [0, 0])
          

      if 295+155 > mouse[0] > 295 and 570+30 > mouse[1] > 570:
        if click[0] == 1:
          screen.blit(productivity_image, [0, 0])
      
    # --- Go ahead and update the screen with what we've drawn.
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    pygame.display.flip()
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()