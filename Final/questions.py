from settings import *
import random

#pool of questions
class Question():
	def _init_(Q):
		Q.text = ""
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

	def Text(A, displayed_text, screen, pos, size, colour, centered = False):
		font = pygame.font.SysFont(START_FONT, size)
		text = font.render(displayed_text, False, colour)
		text_size = text.get_size()
		if centered:
			pos[0]= pos[0]-text_size[0]//2
			pos[1]= pos[1]-text_size[1]//2
		screen.blit(text, pos)


	def Q1(Q):
		Q.text = "Solve the addition"
		Q.X = random.randrange(100, 300)
		Q.Y = random.randrange(100, 300)
		Q.Total = Q.X + Q.Y
		Q.selection = "0"
		Q.fake1 = Q.X - Q.Y
		Q.fake2 = Q.X + Q.X
		Q.fake3 = Q.Y + Q.Y
