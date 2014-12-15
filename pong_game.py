# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 1000
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 90
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
#ball_vel=[1,-3]
ball_pos=[WIDTH/2,HEIGHT/2]
paddle1_pos=0
paddle2_pos=0
paddle1_vel=0
paddle2_vel=0
PAD_VEL=60
score1=0
score2=0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction=="left":
       ball_vel=[-random.randrange(6,10),-1]
    if direction=="right":
       ball_vel=[random.randrange(2,4),-1]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball("left")
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,WIDTH,PAD_WIDTH
    global PAD_VEL,paddle1_vel,paddle2_vel,PAD_HEIGHT
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]=ball_pos[0]+ball_vel[0]
    ball_pos[1]=ball_pos[1]+ball_vel[1]
    
    if ball_pos[0]<=(BALL_RADIUS+PAD_WIDTH):
       ball_vel[0]= - ball_vel[0]
       print "Left gutter"
       print "x   y"
       print ball_pos[0],ball_pos[1]
       print paddle1_pos 
       if (ball_pos[1]>=paddle1_pos) and (ball_pos[1]<=(paddle1_pos+PAD_HEIGHT)) :
            print 'won'
       else:
            print 'left paddle player out'
            score2+=1
    elif ball_pos[0]>=WIDTH-(BALL_RADIUS+PAD_WIDTH):
       ball_vel[0]= - ball_vel[0]
       print "Right gutter"
       print "x    y"
       print ball_pos[0],ball_pos[1]
       print paddle2_pos 
       if (ball_pos[1]>=paddle2_pos) and (ball_pos[1]<=(paddle2_pos+PAD_HEIGHT)):
            print 'won'
       else:
            print 'right paddle player out' 
            score1+=1
      
    if(ball_pos[1])<=BALL_RADIUS:
       ball_vel[1]=-ball_vel[1]
    if(ball_pos[1])>=(HEIGHT-BALL_RADIUS):
       ball_vel[1]=-ball_vel[1]
                    
            
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"red","white")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos=paddle1_vel
    paddle2_pos=paddle2_vel
    #print paddle1_pos
    #print paddle2_pos

    # draw paddles
   
    canvas.draw_polygon([(0,paddle1_pos),(0,(paddle1_pos+PAD_HEIGHT))],16,"red")
    canvas.draw_polygon([(WIDTH,paddle2_pos),(WIDTH,paddle2_pos+PAD_HEIGHT)],16,"red")
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text("PLAYER1",(300,20),24,"ORANGE")
    canvas.draw_text("PLAYER2",(650,20),24,"ORANGE")
    canvas.draw_text(str(score1),(300,70),30,"yellow")
    canvas.draw_text(str(score2),(680,70),30,"yellow")  
def keydown(key):
    global paddle1_vel, paddle2_vel,paddle1_pos,PAD_VEL,PAD_HEIGHT
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=PAD_VEL
        if paddle1_vel>=(HEIGHT-PAD_HEIGHT):
            paddle1_vel=HEIGHT-PAD_HEIGHT
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=PAD_VEL
        if paddle2_vel>=(HEIGHT-PAD_HEIGHT):
            paddle2_vel=HEIGHT-PAD_HEIGHT
def restart():
    global score1,score2,ball_pos,paddle1_pos
    global paddle2_pos,paddle1_vel,paddle2_vel
    score1=0
    score2=0
    ball_pos=[WIDTH/2,HEIGHT/2]
    paddle1_pos=0
    paddle2_pos=0
    paddle1_vel=0
    paddle2_vel=0
    
  
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=PAD_VEL
        if paddle1_vel<0:
            paddle1_vel=0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=PAD_VEL
        if paddle2_vel<0:
            paddle2_vel=0
        
           
        


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",restart)

# start frame
new_game()
frame.start()
