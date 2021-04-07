import turtle as trtl
import turtle
import random as rand
import pygame
from pygame import mixer
pygame.init()
k1 = turtle.Turtle()

#title
wn = trtl.Screen()
wn.title("Word-Skies by Breakout Room 6")
wn.setup(width=600, height=400)
sky = 'sky.gif'
cloud_image = 'cloud.gif'
wrong_cloud = 'wcloud.gif'
wn.addshape(cloud_image)
wn.addshape(wrong_cloud)
wn.bgpic(sky)
print("Welcome to word-skies! Make sure not to capitalize, unless the word is!")
trtl.hideturtle()
trtl.penup()

#various lists
circle_list = []
circle_words = []
words = ['apple','bruh','cat', 'let', 'song', 'without', 'could', 'why', 'into', 'food', 'head', 'away', 'soon', 'best', 'girl', 'she', 'miss', 'big', 'feet', 'she', 'us', 'letter', 'young', 'place', 'ask', 'such', 'he', 'a', 'it', 'side', 'fall', 'high', 'eye', 'let', 'men', 'only', 'its', 'change', 'was', 'hear', 'have', 'cut', 'hard', 'begin', 'old', 'saw', 'water', 'world', 'side', 'song', 'first', 'still', 'want', 'say', 'look', 'next', 'work', 'every', 'time', 'face', 'live', 'left', 'our', 'find', 'sometimes', 'four', 'long', 'every', 'once', 'carry', 'page', 'got', 'thought', 'young', 'big', 'must', 'at', 'leave', 'large', 'name', 'mother', 'have']


#score keeping setup
score = 0
a = 0
k1.hideturtle()
k1.penup()
k1.goto(-200,140)
k1.write("Your Score:", align="center",font=(("Arial"), 20, "bold"))
k2 = turtle.Turtle()
k2.hideturtle()
k2.penup()
k2.goto(-85,140)
k2.write(score, align="center", font=("Arial", 20, "bold"))

#creating turtles for clouds / choosing three words
for i in range(3):
  circle_list.append(trtl.Turtle())
  circle_words.append(rand.choice(words))

#main code
while True:

 #word circles
 def cloud(index):
   circle_list[index].penup()
   circle_list[index].shape(cloud_image)
   circle_list[index].showturtle()
   circle_list[index].goto(-200 + a, 60)
   wn.tracer(False)
   circle_list[index].sety(circle_list[index].ycor()-40)
   circle_list[index].color("black")
   circle_list[index].write(circle_words[index], align="center", font=("Arial", 35, "bold"))
   circle_list[index].sety(circle_list[index].ycor()+40)
   wn.tracer(True)
   wn.update()

 #Falling clouds
 def drop_circle(index):
    circle_list[index].clear()
    circle_list[index].sety(-500)
    circle_words[index] = rand.choice(words)
    wn.tracer(False)
    k2.clear()
    k2.goto(-85,140)
    k2.write(score, align="center", font=("Arial", 20, "bold"))
    wn.tracer(True)
    wn.update()
    
 #controlling and creating cloud positions
 a = 0
 for i in range(3):
   cloud(i)
   a = a + 200
   if (a == 600):
     a = 0

 for i in range(3):
   word = input("Type the Word: ")
   if word in circle_words:
     score = score + 1
     drop_circle(i) 
   else:
     print("Wrong word.")
     circle_list[i].shape(wrong_cloud)
     score = score - 1
     drop_circle(i)
