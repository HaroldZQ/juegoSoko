import pygame

#button class
class Button():
	#METODO CONSTRUCTOR 
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#Obtener la posición del mouse
		pos = pygame.mouse.get_pos()

		#verifique las condiciones de paso del mouse y de realizar el clic
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#Dibujar botón en pantalla
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action