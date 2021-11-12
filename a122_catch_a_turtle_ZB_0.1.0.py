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
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
colors = ['purple', 'blue', 'lightblue', 'yellow', 'white', 'yellow', 'green', 'pink']
sizes = [3, 2.5, 2, 1.5, 1.2, 1, 0.75, 0.5]
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
  change_color()
  change_size()
  shortie.color('lightgreen')
  score_writer.clear()
  update_score()
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
def change_color():
  shortie.color(rand.choice(colors))
  shortie.stamp()
def change_size():
  shortie.turtlesize(rand.choice(sizes))
# manages the leaderboard for top 5 scorers

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

def load_leaderboard(file_name, leader_names, leader_scores):

  leaderboard_file = open(file_name, "r")  # need to create the file ahead of time in same folder

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  for line in leaderboard_file:
    leader_name = ""
    leader_score = ""    
    index = 0

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")


    # TODO 2: add the leader name to the list

    
    # TODO 3: read the player score using a similar loop

    
    # TODO 4: add the player score to the list


  leaderboard_file.close()


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

  leader_index = 0
  # TODO 5: loop through all the scores in the existing leaderboard list
  '''
    while ():
    # TODO 6: check if this is the position to insert new score at
    if ():
      break
    else:
      leader_index = leader_index + 1
  '''
  # TODO 7: insert the new player and score at the appropriate position


  # TODO 8: keep both lists at 5 elements only (top 5 players)

  
  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
  leader_index = 0
  # TODO 9: loop through all the leaderboard elements and write them to the file
  '''
    while ():
    leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
    leader_index = leader_index + 1
  '''
  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-200,100)
  turtle_object.hideturtle()
  turtle_object.down()
  leader_index = 0

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while leader_index < len(leader_names):
    turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
    leader_index = leader_index + 1

  # Display message about player making/not making leaderboard based on high_scorer
  if (high_scorer):
    turtle_object.write("Congratulations! You made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry, you didn't make the leaderboard. Maybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # TODO 10: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
  '''
  if ():
    turtle_object.write("You earned a bronze medal!", font=font_setup)
    turtle_object.write("You earned a silver medal!", font=font_setup)
    turtle_object.write("You earned a gold medal!", font=font_setup)
  '''
  
#-----events----------------
wn = turtle.Screen()
wn.bgcolor('red')
wn.ontimer(countdown, counter_interval) 
shortie.onclick(shortie_clicked)
wn.mainloop()