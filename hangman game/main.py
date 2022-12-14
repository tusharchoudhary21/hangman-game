
import pygame
import math
import random


#setting up dispaly window
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

#button variables 
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP)*13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + (( RADIUS * 2 + GAP)*(i % 13))
    y = starty + ((i//13)*( GAP + RADIUS * 2))
    letters.append([x,y,chr(A+i), True])

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 32)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)


#load images
images = []
for i in range(7):
    image = pygame.image.load("hangman"+ str(i)+ ".png")
    images.append(image)

#game varibles
#hangman_status = 0
words = ["DEVELOPER", "IDE", "PYTHON", "PYGAME", "CODE", "PROJECT", "SOFTWARE", "VSCODE","XCODE"]
word = random.choice(words)
guessed = []

#colors 
WHITE = (255,255,255)
BLACK = (0,0,0)


def draw(): 
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    text.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))


    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y),RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150,100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1500) 
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000) 

def main():
    #setting up game loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    
    global hangman_status 
    hangman_status = 0
    guessed.clear()
    letters.clear()
    startx = round((WIDTH - (RADIUS * 2 + GAP)*13)/2)
    starty = 400
    A = 65
    for i in range(26):
        x = startx + GAP * 2 + (( RADIUS * 2 + GAP)*(i % 13))
        y = starty + ((i//13)*( GAP + RADIUS * 2))
        letters.append([x,y,chr(A+i), True])
    
    

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 

                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    for letter in letters:
                        x, y, ltr, visible = letter
                        if visible:
                            dis = math.sqrt((x-m_x)**2+(y-m_y)**2)
                            if dis < RADIUS:
                                letter[3] = False
                                guessed.append(ltr)
                                if ltr not in word:
                                    hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won: 
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("You LOST!")
            break

flag = True
while flag:
    # ask for do you want to play
    win.fill(WHITE)
    text = WORD_FONT.render("Do you want to play", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 - 100))
    #pygame.display.update()

    # creating yes button
    pygame.draw.circle(win, BLACK, (340,250),RADIUS, 3)
    text = LETTER_FONT.render("Y", 1, BLACK)
    win.blit(text, (370 - text.get_width()/2 - 30, 250 - text.get_height()/2))
    #pygame.display.update()

    # creating no button
    pygame.draw.circle(win, BLACK, (460,250),RADIUS, 3)
    text = LETTER_FONT.render("N", 1, BLACK)
    win.blit(text, (430 - text.get_width()/2 + 30, 250 - text.get_height()/2))
    pygame.display.update()
    #pygame.time.delay(5000)

    #checking the input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            if(math.sqrt((340-m_x)**2+(250-m_y)**2)<RADIUS):
                word = random.choice(words)
                main()
            if(math.sqrt((460-m_x)**2+(250-m_y)**2)<RADIUS):
                flag = False



    
pygame.quit()