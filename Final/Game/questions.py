from settings import *
import random

#pool of questions
class Question():
	def _init_(Q):
		Q.text = ""
		Q.symbol = ""
		Q.X = 0
		Q.Y = 0
		Q.fake1 = 0
		Q.fake2 = 0
		Q.fake3 = 0
		Q.Total = 0
		Q.Text()
		Q.Buttons()
		Q.Q1()
		Q.selection = "0"
		Q.randomQuestion()
		Q.ran = 0
	


	def randomQuestion(Q):
		Q.ran = random.randrange(0, 2)

		if (Q.ran == 0):
			Q.Q1()
		elif(Q.ran == 1):
			Q.Q2()


	def Q2(Q):
		Q.ran = 1
		Q.text = "Solve the substraction"
		Q.symbol = "-"
		Q.X = random.randrange(0, 1000)
		Q.Y = random.randrange(0, 1000)
		if (Q.X - Q.Y < 0):
			Q.Q2()

		Q.Total = Q.X - Q.Y
		Q.selection = "0"
		Q.fake1 = Q.X + Q.Y
		Q.fake2 = Q.X - Q.Y + random.randrange(1,50)
		Q.fake3 = Q.X - Q.Y - random.randrange(1,50)




	def Q1(Q):
		
		Q.ran = 0
		Q.text = "Solve the addition"
		Q.symbol = "+"
		Q.X = random.randrange(0, 1000)
		Q.Y = random.randrange(0, 1000)
		Q.Total = Q.X + Q.Y
		Q.selection = "0"
		Q.fake1 = Q.X - Q.Y
		Q.fake2 = Q.X + Q.X
		Q.fake3 = Q.Y + Q.Y

