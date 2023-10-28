import sys
import pygame
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
pygame.init()
x=800
y=600
size=(800,600)
screen=pygame.display.set_mode(size)
io=screen
#rectangle size......
rect_x=400
rect_y=580

#intial moving spped
rect_change_x=0
rect_change_y=0

#ball size..
ball_x=50
ball_y=50

#speed of the ball
ball_speed_x=5
ball_speed_y=5

score=0
k=0
def drawrect(screen,x,y):
    if x<=0:
        x=0
    if x>=699:
        x=699
    pygame.draw.rect(screen,red,[x,y,100,20])

#main loop
done=False
clock=pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
        elif event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                rect_change_x=-6
            elif event.key==pygame.K_RIGHT:
                rect_change_x=6
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                rect_change_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                rect_change_y=0
    screen.fill(black)
    rect_x+=rect_change_x
    rect_y+=rect_change_y

    ball_x+=ball_speed_x
    ball_y+=ball_speed_y


    if ball_x<0:
        ball_x=0
        ball_speed_x=ball_speed_x * -1
    elif ball_x>785:
        ball_x=785
        ball_speed_x=ball_speed_x * -1
    elif ball_y<0:
        ball_y=0
        ball_speed_y=ball_speed_y * -1
    elif ball_x>rect_x and ball_x<rect_x+100 and ball_y==565:
        ball_speed_y=ball_speed_y * -1
        score=score+1
    elif ball_y>600:
        ball_speed_y=ball_speed_y * -1
        score-=1
        k+=1

    elif score <0:
        score = 0
        print("Your Score is :", score)
    elif k==1:
        print("Your Score is :", score)
        pygame.quit()
        sys.exit()


    #pygame.draw.rect(screen,white,[ball_x,ball_y,15,15])
    pygame.draw.circle(screen, white, (ball_x,ball_y), 10)

    #draw ball
    #drawrect((screen,rect_x,rect_y))
    pygame.draw.rect(screen, red, (rect_x,rect_y,120,100))



    #scores

    pygame.display.flip()
    clock.tick(60)

print("Your Score is :", score)
