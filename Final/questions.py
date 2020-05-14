from settings import *

#pool of questions
class Question():
	def _init_(Q):
		Q.Text()
		Q.Buttons()

	def Text(A, displayed_text, screen, pos, size, colour, centered = False):
		font = pygame.font.SysFont(START_FONT, size)
		text = font.render(displayed_text, False, colour)
		text_size = text.get_size()
		if centered:
			pos[0]= pos[0]-text_size[0]//2
			pos[1]= pos[1]-text_size[1]//2
		screen.blit(text, pos)
