# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand
import leaderboard as lb
#-----game configuration----
turtle_color = 'lightgreen'
turtle_size = 1
turtle_shape = 'square'
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("give me ur name rn. \n")
#-----initialize turtle-----
shortie = turtle.Turtle()
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(350,285)
shortie.shape(turtle_shape)
shortie.fillcolor(turtle_color)
shortie.shapesize(turtle_size)
counter =  turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-300, 285)
#-----game functions--------
def shortie_clicked(x, y):
  global timer_up
  if timer_up == False:
    change_position()
    score_writer.clear()
    update_score()
  else:
      shortie.hideturtle()
def change_position():
  new_xpos = rand.randint(-400,400)
  new_ypos = rand.randint(-300, 300)
  shortie.penup()
  shortie.hideturtle()
  shortie.goto(new_xpos, new_ypos)
  shortie.showturtle()
  shortie.pendown()
def update_score():
  global score
  score += 1
  score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global shortie

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, shortie, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, shortie, score)

#-----events----------------
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval) 
shortie.onclick(shortie_clicked)
wn.mainloop()