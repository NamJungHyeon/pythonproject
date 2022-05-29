import time
import random
from tkinter import *
import turtle
from turtle import Turtle
a = Turtle()
b = Turtle()
a.hideturtle()
b.hideturtle()
a.shape("turtle")
b.shape("turtle")
a.penup()
b.penup()
a.left(90)
b.left(90)
a.goto(300, -280)
b.goto(300, -280)
a.color("green")
b.color("yellow")
a.showturtle()
b.showturtle()


class throwing():
   def __init__(self, name, count, i, computer):
      self.__name = name
      self.__count = count
      self.__i = i
      self.__computer = computer

   def name1(self):
      self.__name = input("플레이어의 이름은?:")

   def show(self):
      self.__count = 0
      self.__i = 0
      self.__l = []
      while self.__i < 4:
         self.__l.append(random.randint(0,1))
         self.__i += 1
      print(self.__l)
      for x in self.__l :
         if x == 1:
            self.__count = self.__count + 1
      if self.__count == 1:
         print("도!", self.__name, "의 말을 한칸 움직입니다.")
         if a.heading() == 225 or a.heading() == 315:
            if a.xcor() == 102.01 and a.ycor() == 122.01:
               a.forward(140)
               a.left(90)
            elif a.xcor() == -194.97 and a.ycor() == -174.97:
               a.forward(140)
               a.left(135)
            elif a.position() == (201.01, -174.97):
               a.goto(300,-280)
               a.reset()
               a.write("You win!")
            else:
               a.forward(140)
         else:
            if (a.xcor() == 300 and a.ycor() == 200) or (a.xcor() == -180 and a.ycor() == 320):
               a.forward(120)
               a.left(135)
            elif a.xcor() == -300 and a.ycor() == -160:
               a.forward(120)
               a.left(90)
            else:
               a.forward(120)



         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print(self.__name, "의 말이 컴퓨터의 말을 잡았습니다.")
            print("컴퓨터의 말이 시작점으로 돌아갑니다.")
            b.goto(300,-280)
            b.setheading(90)



      elif self.__count == 2:
         print("개!", self.__name, "의 말을 두칸 움직입니다.")
         if a.heading() == 225 or a.heading() == 315:
            if  a.xcor() == -194.97 and a.ycor() == -174.97:
               a.forward(140)
               a.left(135)
               a.forward(120)
            elif a.xcor() == 201.01 and a.ycor() == 221.01:
               a.forward(280)
               a.left(90)
            elif a.xcor() == -95.98 and a.ycor() == -75.98:
               a.forward(280)
               a.left(135)
            elif a.position() == (201.01, -174.97):
               a.goto(300,-280)
               a.reset()
               a.write("You win!")
            elif a.position() == (102.01, -75.98):
               a.goto(300,-280)
               a.reset()
               a.write("You win!")
            else:
               a.forward(280)
         else:
            if a.xcor() == 300 and a.ycor() == 200 :
               a.forward(120)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -180 and a.ycor() == 320:
               a.forward(120)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -300 and a.ycor() == -160:
               a.forward(120)
               a.left(90)
               a.forward(120)
            else:
               if (a.xcor() == 300 and a.ycor() == 80) or (a.xcor() == -60 and a.ycor() == 320):
                  a.forward(240)
                  a.left(135)
               elif a.xcor() == -300 and a.ycor() == -40:
                  a.forward(240)
                  a.left(90)
               else:
                  a.forward(240)

         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print(self.__name, "의 말이 컴퓨터의 말을 잡았습니다.")
            print("컴퓨터의 말이 시작점으로 돌아갑니다.")
            b.goto(300,-280)
            b.setheading(90)




      elif self.__count == 3:
         print("걸!", self.__name, "의 말을 세칸 움직입니다.")
         if a.heading() == 225 or a.heading() == 315:
            if a.xcor() == -95.98 and a.ycor() == -75.98:
               a.forward(280)
               a.left(135)
               a.forward(120)
            elif a.xcor() == -194.97 and a.ycor() == -174.97:
               a.forward(140)
               a.left(135)
               a.forward(240)
            elif a.xcor() == 300 and a.ycor() == 320 :
               a.forward(420)
               a.left(90)
            elif a.position() == (201.01, -174.97):
               a.goto(300,-280)
               a.reset()
               a.write("You win!")
            elif a.position() == (102.01, -75.98):
               a.goto(300,-280)
               a.reset()
               a.write("You win!")
            else:
               a.forward(420)
         else:
            if a.xcor() == 300 and a.ycor() == 80 :
               a.forward(240)
               a.left(90)
               a.forward(120)
            elif a.xcor() == 300 and a.ycor() == 200 :
               a.forward(120)
               a.left(90)
               a.forward(240)
            elif a.xcor() == -60 and a.ycor() == 320 :
               a.forward(240)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -180 and a.ycor() == 320 :
               a.forward(120)
               a.left(90)
               a.forward(240)
            elif a.xcor() == -300 and a.ycor() == -40:
               a.forward(240)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -300 and a.ycor() == -160:
               a.forward(120)
               a.left(90)
               a.forward(240)
            else:
               if (a.xcor() == 300 and a.ycor() == -40)or(a.xcor() == -60 and a.ycor() == 320):
                  a.forward(360)
                  a.left(135)

               elif a.xcor() == -300 and a.ycor() == 80:
                  a.forward(360)
                  a.left(90)
               else:
                  a.forward(360)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print(self.__name, "의 말이 컴퓨터의 말을 잡았습니다.")
            print("컴퓨터의 말이 시작점으로 돌아갑니다.")
            b.goto(300,-280)
            b.setheading(90)




      elif self.__count == 4:
         print("윷!", self.__name, "의 말을 네칸 움직입니다.")
         if a.heading() == 225 or a.heading() == 315:
            if a.xcor() == 3.02 and a.ycor() == 23.02:
               a.forward(420)
               a.left(135)
               a.forward(120)
            elif a.xcor() == -95.98 and a.ycor() == -75.98:
               a.forward(280)
               a.left(135)
               a.forward(240)
            elif a.xcor() == -194.97 and a.ycor() == -174.97:
               a.forward(140)
               a.left(135)
               a.forward(360)
            elif a.xcor() == 102.01 and a.ycor() == 122.01:
               a.forward(560)
               a.left(135)
            elif a.position() == (201.01, -174.97):
               a.reset()
               a.write("You win!")
            elif a.position() == (102.01, -75.98):
               a.reset()
               a.write("You win!")
            else:
               a.forward(560)
         else:
            if a.xcor() == 300 and a.ycor() == -40 :
               a.forward(360)
               a.left(90)
               a.forward(120)
            elif a.xcor() == 300 and a.ycor() == 80 :
               a.forward(240)
               a.left(90)
               a.forward(240)
            elif a.xcor() == 300 and a.ycor() == 200 :
               a.forward(120)
               a.left(90)
               a.forward(360)
            elif a.xcor() == 60 and a.ycor() == 320:
               a.forward(360)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -60 and a.ycor() == 320:
               a.forward(240)
               a.left(90)
               a.forward(240)
            elif a.xcor() == -180 and a.ycor() == 320:
               a.forward(120)
               a.left(90)
               a.forward(360)
            elif a.xcor() == -300 and a.ycor() == 80:
               a.forward(360)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -300 and a.ycor() == -40:
               a.forward(240)
               a.left(90)
               a.forward(240)
            elif a.xcor() == -300 and a.ycor() == -160:
               a.forward(120)
               a.left(90)
               a.forward(360)
            else:
               if (a.xcor() == 300 and a.ycor() == -160) or (a.xcor() == 180 and a.ycor() == 320):
                  a.forward(480)
                  a.left(135)
               elif a.xcor() == -300 and a.ycor() == 200:
                  a.forward(480)
                  a.left(90)
               else:
                  a.forward(480)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print(self.__name, "의 말이 컴퓨터의 말을 잡았습니다.")
            print("컴퓨터의 말이 시작점으로 돌아갑니다.")
            b.goto(300,-280)
            b.setheading(90)




      elif self.__count == 0:
         print("모!", self.__name, "의 말을 다섯칸 움직입니다.")
         if a.heading() == 225 or a.heading() == 315:
            if a.xcor() == 102.01 and a.ycor() == 122.01:
               a.forward(560)
               a.left(135)
               a.forward(120)
            elif a.xcor() == 3.02 and a.ycor() == 23.02:
               a.forward(420)
               a.left(135)
               a.forward(240)
            elif a.xcor() == -95.98 and a.ycor() == -75.98:
               a.forward(280)
               a.left(135)
               a.forward(360)
            elif a.xcor() == -194.97 and a.ycor() == -174.97:
               a.forward(140)
               a.left(135)
               a.forward(480)
            elif a.xcor() == 201.01 and a.ycor() == 221.01:
               a.forward(700)
               a.left(135)
            elif a.position() == (201.01, -174.97):
               a.reset()
               a.write("You win!")
            elif a.position() == (102.01, -75.98):
               a.reset()
               a.write("You win!")
            else:
               a.forward(700)
         else:
            if a.xcor() == 300 and a.ycor() == -160 :
               a.forward(480)
               a.left(90)
               a.forward(120)
            elif a.xcor() == 300 and a.ycor() == -40 :
               a.forward(360)
               a.left(90)
               a.forward(240)
            elif a.xcor() == 300 and a.ycor() == 80 :
               a.forward(240)
               a.left(90)
               a.forward(360)
            elif a.xcor() == 300 and a.ycor() == 200 :
               a.forward(120)
               a.left(90)
               a.forward(480)
            elif a.xcor() == 180 and a.ycor() == 320:
               a.forward(480)
               a.left(90)
               a.forward(120)
            elif a.xcor() == 60 and a.ycor() == 320:
               a.forward(360)
               a.left(90)
               a.forward(240)
            elif a.xcor() == -60 and a.ycor() == 320:
               a.forward(240)
               a.left(90)
               a.forward(360)
            elif a.xcor() == -180 and a.ycor() == 320:
               a.forward(120)
               a.left(90)
               a.forward(480)
            elif a.xcor() == -300 and a.ycor() == 200:
               a.forward(480)
               a.left(90)
               a.forward(120)
            elif a.xcor() == -300 and a.ycor() == 80:
               a.forward(360)
               a.left(90)
               a.forward(240)
            elif a.xcor() == -300 and a.ycor() == -40:
               a.forward(240)
               a.left(90)
               a.forward(360)
            elif a.xcor() == -300 and a.ycor() == -160:
               a.forward(120)
               a.left(90)
               a.forward(480)
            else:
               if (a.xcor() == 300 and a.ycor() == -280) or (a.xcor() == 300 and a.ycor() == 320):
                  a.forward(600)
                  a.left(135)
               elif a.xcor() == -300 and a.ycor() == 320:
                  a.forward(600)
                  a.left(90)
               else:
                  a.forward(600)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print(self.__name, "의 말이 컴퓨터의 말을 잡았습니다.")
            print("컴퓨터의 말이 시작점으로 돌아갑니다.")
            b.goto(300,-280)
            b.setheading(90)



      time.sleep(2)
      self.__count = 0
      self.__i = 0
      self.__l = []
      while self.__i < 4:
         self.__l.append(random.randint(0, 1))
         self.__i += 1
      print(self.__l)
      for x in self.__l:
         if x == 1:
            self.__count = self.__count + 1
      if self.__count == 1:
         print("도! 컴퓨터의 말을 한칸 움직입니다.")
         if b.heading() == 225 or b.heading() == 315:
            if b.xcor() == 102.01 and b.ycor() == 122.01:
               b.forward(140)
               b.left(90)
            elif b.xcor() == -194.97 and b.ycor() == -174.97:
               b.forward(140)
               b.left(135)
            elif b.position() == (201.01, -174.97):
               b.reset()
               b.write("You lose!")

            else:
               b.forward(140)
         else:
            if (b.xcor() == 300 and b.ycor() == 200) or (b.xcor() == -180 and b.ycor() == 320):
               b.forward(120)
               b.left(135)
            elif b.xcor() == -300 and b.ycor() == -160:
               b.forward(120)
               b.left(90)
            else:
               b.forward(120)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print("컴퓨터의 말이", self.__name, "의 말을 잡았습니다.")
            print(self.__name, "의 말이 시작점으로 돌아갑니다.")
            a.goto(300,-280)
            a.setheading(90)


      elif self.__count == 2:
         print("개! 컴퓨터의 말을 두칸 움직입니다.")
         if b.heading() == 225 or b.heading() == 315:
            if b.xcor() == -194.97 and b.ycor() == -174.97:
               b.forward(140)
               b.left(135)
               b.forward(120)
            elif b.xcor() == 201.01 and b.ycor() == 221.01:
               b.forward(280)
               b.left(90)
            elif b.xcor() == -95.98 and b.ycor() == -75.98:
               b.forward(280)
               b.left(135)
            elif b.position() == (201.01, -174.97):
               b.goto(300,-280)
               b.reset()
               b.write("You lose!")
            elif b.position() == (102.01, -75.98):
               b.goto(300,-280)
               b.reset()
               b.write("You lose!")


            else:
               b.forward(280)
         else:
            if b.xcor() == 300 and b.ycor() == 200 :
               b.forward(120)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -180 and b.ycor() == 320:
               b.forward(120)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -300 and b.ycor() == -160:
               b.forward(120)
               b.left(90)
               b.forward(120)
            else:
               if (b.xcor() == 300 and b.ycor() == 80) or (b.xcor() == -40 and b.ycor() == 320):
                  b.forward(240)
                  b.left(135)
               elif b.xcor() == -300 and b.ycor() == -40:
                  b.forward(240)
                  b.left(90)
               else:
                  b.forward(240)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print("컴퓨터의 말이", self.__name, "의 말을 잡았습니다.")
            print(self.__name, "의 말이 시작점으로 돌아갑니다.")
            a.goto(300,-280)
            a.setheading(90)



      elif self.__count == 3:
         print("걸! 컴퓨터의 말을 세칸 움직입니다.")
         if b.heading() == 225 or b.heading() == 315:
            if b.xcor() == -95.98 and b.ycor() == -75.98:
               b.forward(280)
               b.left(135)
               b.forward(120)
            elif b.xcor() == -194.97 and b.ycor() == -174.97:
               b.forward(140)
               b.left(135)
               b.forward(240)
            elif b.xcor() == 300 and b.ycor() == 320:
               b.forward(420)
               b.left(90)
            elif b.position() == (201.01, -174.97):
               b.goto(300,-280)
               b.reset()
               b.write("You lose!")
            elif b.position() == (102.01, -75.98):
               b.goto(300,-280)
               b.reset()
               b.write("You lose!")

            else:
               b.forward(420)
         else:
            if b.xcor() == 300 and b.ycor() == 80 :
               b.forward(240)
               b.left(90)
               b.forward(120)
            elif b.xcor() == 300 and b.ycor() == 200 :
               b.forward(120)
               b.left(90)
               b.forward(240)
            elif b.xcor() == -60 and b.ycor() == 320 :
               b.forward(240)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -180 and b.ycor() == 320 :
               b.forward(120)
               b.left(90)
               b.forward(240)
            elif b.xcor() == -300 and b.ycor() == -40:
               b.forward(240)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -300 and b.ycor() == -160:
               b.forward(120)
               b.left(90)
               b.forward(240)
            else:
               if (b.xcor() == 300 and b.ycor() == -40) or (b.xcor() == 60 and b.ycor() == 320):
                  b.forward(360)
                  b.left(135)
               elif b.xcor() == -300 and b.ycor() == 80:
                  b.forward(360)
                  b.left(90)
               else:
                  b.forward(360)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print("컴퓨터의 말이", self.__name, "의 말을 잡았습니다.")
            print(self.__name, "의 말이 시작점으로 돌아갑니다.")
            a.goto(300,-280)
            a.setheading(90)



      elif self.__count == 4:
         print("윷! 컴퓨터의 말을 네칸 움직입니다.")
         if b.heading() == 225 or b.heading() == 315:
            if b.xcor() == 3.02 and b.ycor() == 23.02:
               b.forward(420)
               b.left(135)
               b.forward(120)
            elif b.xcor() == -95.98 and b.ycor() == -75.98:
               b.forward(280)
               b.left(135)
               b.forward(240)
            elif b.xcor() == -194.97 and b.ycor() == -174.97:
               b.forward(140)
               b.left(135)
               b.forward(360)
            elif b.xcor() == 102.01 and b.ycor() == 122.01:
               b.forward(560)
               b.left(90)
            elif b.position() == (201.01, -174.97):
               b.reset()
               b.write("You lose!")
            elif b.position() == (102.01, -75.98):
               b.reset()
               b.write("You lose!")
            else:
               b.forward(560)
         else:
            if b.xcor() == 300 and b.ycor() == -40 :
               b.forward(360)
               b.left(90)
               b.forward(120)
            elif b.xcor() == 300 and b.ycor() == 80 :
               b.forward(240)
               b.left(90)
               b.forward(240)
            elif b.xcor() == 300 and b.ycor() == 200 :
               b.forward(120)
               b.left(90)
               b.forward(360)
            elif b.xcor() == 60 and b.ycor() == 320:
               b.forward(360)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -60 and b.ycor() == 320:
               b.forward(240)
               b.left(90)
               b.forward(240)
            elif b.xcor() == -180 and b.ycor() == 320:
               b.forward(120)
               b.left(90)
               b.forward(360)
            elif b.xcor() == -300 and b.ycor() == 80:
               b.forward(360)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -300 and b.ycor() == -40:
               b.forward(240)
               b.left(90)
               b.forward(240)
            elif b.xcor() == -300 and b.ycor() == -160:
               b.forward(120)
               b.left(90)
               b.forward(360)
            else:
               if (b.xcor() == 300 and b.ycor() == --160) or (b.xcor() == 180 and b.ycor() == 320):
                  b.forward(480)
                  b.left(135)
               elif b.xcor() == -300 and b.ycor() == 200:
                  b.forward(480)
                  b.left(90)
               else:
                  b.forward(480)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print("컴퓨터의 말이", self.__name, "의 말을 잡았습니다.")
            print(self.__name, "의 말이 시작점으로 돌아갑니다.")
            a.goto(300,-280)
            a.setheading(90)




      elif self.__count == 0:
         print("모! 컴퓨터의 말을 다섯칸 움직입니다.")
         if b.heading() == 225 or b.heading() == 315:
            if b.xcor() == 102.01 and b.ycor() == 122.01:
               b.forward(560)
               b.left(135)
               b.forward(120)
            elif b.xcor() == 3.02 and b.ycor() == 23.02:
               b.forward(420)
               b.left(135)
               b.forward(240)
            elif b.xcor() == -95.98 and b.ycor() == -75.98:
               b.forward(280)
               b.left(135)
               b.forward(360)
            elif b.xcor() == -194.97 and b.ycor() == -174.97:
               b.forward(140)
               b.left(135)
               b.forward(480)
            elif b.xcor() == 201.01 and b.ycor() == 221.01:
               b.forward(560)
               b.left(135)
            elif b.position() == (201.01, -174.97):
               b.reset()
               b.write("You lose!")
            elif b.position() == (102.01, -75.98):
               b.reset()
               b.write("You lose!")
            else:
               b.forward(700)
         else:
            if b.xcor() == 300 and b.ycor() == -160 :
               b.forward(480)
               b.left(90)
               b.forward(120)
            elif b.xcor() == 300 and b.ycor() == -40 :
               b.forward(360)
               b.left(90)
               b.forward(240)
            elif b.xcor() == 300 and b.ycor() == 80 :
               b.forward(240)
               b.left(90)
               b.forward(360)
            elif b.xcor() == 300 and b.ycor() == 200 :
               b.forward(120)
               b.left(90)
               b.forward(480)
            elif b.xcor() == 180 and b.ycor() == 320:
               b.forward(480)
               b.left(90)
               b.forward(120)
            elif b.xcor() == 60 and b.ycor() == 320:
               b.forward(360)
               b.left(90)
               b.forward(240)
            elif b.xcor() == -60 and b.ycor() == 320:
               b.forward(240)
               b.left(90)
               b.forward(360)
            elif b.xcor() == -180 and b.ycor() == 320:
               b.forward(120)
               b.left(90)
               b.forward(480)
            elif b.xcor() == -300 and b.ycor() == 200:
               b.forward(480)
               b.left(90)
               b.forward(120)
            elif b.xcor() == -300 and b.ycor() == 80:
               b.forward(360)
               b.left(90)
               b.forward(240)
            elif b.xcor() == -300 and b.ycor() == -40:
               b.forward(240)
               b.left(90)
               b.forward(360)
            elif b.xcor() == -300 and b.ycor() == -160:
               b.forward(120)
               b.left(90)
               b.forward(480)
            else:
               if (b.xcor() == 300 and b.ycor() == -280) or (b.xcor() == 300 and b.ycor() == 320):
                  b.forward(600)
                  b.left(135)
               elif b.xcor() == -300 and b.ycor() == -320:
                  b.forward(600)
                  b.left(90)
               else:
                  b.forward(600)


         if a.xcor() == b.xcor() and a.ycor() == b.ycor():
            print("컴퓨터의 말이", self.__name, "의 말을 잡았습니다.")
            print(self.__name, "의 말이 시작점으로 돌아갑니다.")
            a.goto(300,-280)
            a.setheading(90)




   def tnstj(self):
      self.__count = 0
      self.__i = 0
      self.__l = []
      while self.__i < 1:
         self.__l.append(random.randint(0, 1))
         self.__i += 1
      print(self.__l)
      for x in self.__l:
         if x == 1:
            self.__count = self.__count + 1
      if self.__count == 1:
         print("", self.__name, " 먼저 던지세요!")
      else:
         print("두번째 순서에요! 컴퓨터 먼저 시작합니다.")
         time.sleep(2)
         self.__count = 0
         self.__i = 0
         self.__l = []
         while self.__i < 4:
            self.__l.append(random.randint(0, 1))
            self.__i += 1
         print(self.__l)
         for x in self.__l:
            if x == 1:
               self.__count = self.__count + 1
         if self.__count == 1:
            print("도! 컴퓨터의 말을 한칸 움직입니다.")
            b.forward(120)
         elif self.__count == 2:
            print("개! 컴퓨터의 말을 두칸 움직입니다.")
            b.forward(240)
         elif self.__count == 3:
            print("걸! 컴퓨터의 말을 세칸 움직입니다.")
            b.forward(360)
         elif self.__count == 4:
            print("윷! 컴퓨터의 말을 네칸 움직입니다. ")
            b.forward(480)
         elif self.__count == 0:
            print("모! 컴퓨터의 말을 다섯칸 움직입니다. ")
            b.goto(300,320)
            b.left(135)




def main():
   class App(Frame):
      def __init__(self, master):
         super().__init__(master)
         self.pack()
         label = Label(self)
         label['text'] = "신나는 윷놀이"
         label.pack()
         Button(self, text="사용자 설정", command=self.c1).pack()
         Button(self, text="순서정하기", command=self.c3).pack()
         Button(self, text="던지기", command=self.c2).pack()
         Button(self, text="그만하기", command=self.quit).pack()

      import turtle
      from turtle import Turtle
      turtle.hideturtle()
      turtle.speed(500000)
      turtle.width(10)
      turtle.color("red")
      turtle.circle(40)

      turtle.penup()
      turtle.goto(300, 300)
      turtle.pendown()
      turtle.circle(40)
      turtle.penup()
      turtle.goto(-300, 300)
      turtle.pendown()
      turtle.circle(40)
      turtle.penup()
      turtle.goto(-300, -300)
      turtle.pendown()
      turtle.circle(40)
      turtle.penup()
      turtle.goto(300, -300)
      turtle.pendown()
      turtle.circle(40)
      turtle.penup()
      turtle.goto(300, -180)
      turtle.color("blue")
      turtle.width(5)
      turtle.pendown()
      turtle.circle(20)

      turtle.penup()
      turtle.goto(300, -60)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(300, 60)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(300, 180)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(180, 320)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(60, 320)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-60, 320)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-180, 320)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-300, 180)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-300, 60)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-300, -60)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-300, -180)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-180, -300)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-60, -300)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(60, -300)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(180, -300)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(180, -180)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(80, -80)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-100, 110)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-180, 200)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-180, -180)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(-90, -80)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(110, 110)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()
      turtle.goto(200, 200)
      turtle.pendown()
      turtle.circle(20)
      turtle.penup()

      def c1(self):
         throwing.name1(self)

      def c2(self):
         throwing.show(self)

      def c3(self):
         throwing.tnstj(self)

   window = Tk()
   window.title("윷놀이")
   window.geometry("200x140")
   App(window)
   window.mainloop()


print(main())




