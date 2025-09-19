import pygame
import pygame.freetype

from time import sleep

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

crossSCORE = 0
circleSCORE = 0

while True:
	pygame.init()
	Font = pygame.freetype.Font("freesansbold.ttf", 50)

	Turn = "CROSS"
	Win = False

	rowX = 0
	rowY = 0

	#Lager en liste for alle rutene
	SquaresA, SquaresB, SquaresC = ["Vacant","Vacant","Vacant"], ["Vacant","Vacant","Vacant"], ["Vacant","Vacant","Vacant"]

	def ClaimSquare(X, Y): #Funksjon for å kreve en rute
		global Turn
		global SquaresA
		global SquaresB
		global SquaresC
		SwitchSquares = False

		X -= 1
	
		if Y == 1 and SquaresA[X] == "Vacant":
			SquaresA[X] = Turn
			SwitchSquares = True

		elif Y == 2 and SquaresB[X] == "Vacant":
			SquaresB[X] = Turn
			SwitchSquares = True

		elif Y == 3 and SquaresC[X] == "Vacant":
			SquaresC[X] = Turn
			SwitchSquares = True

		if SwitchSquares:
			if Turn == "CROSS":
				Turn = "CIRCLE"
			
			else:
				Turn = "CROSS"

	def PlayerWon(Winner):
		global SquaresA, SquaresB, SquaresC
		global Win

		global crossSCORE
		global circleSCORE

		if not Winner == "Vacant":
			print(Winner, "WON THE MATCH")
			sleep(1)
			Win = True

			if Winner == "CROSS":
				crossSCORE += 1

			elif Winner == "CIRCLE":
				circleSCORE += 1

			print("Cross:", crossSCORE, "Circle:", circleSCORE)

	def FindWinner():
		global Turn
		global SquaresA
		global SquaresB
		global SquaresC


		if SquaresA[0] == SquaresA[1] == SquaresA[2]:
			PlayerWon(SquaresA[0])

		if SquaresB[0] == SquaresB[1] == SquaresB[2]:
			PlayerWon(SquaresB[0])

		if SquaresC[0] == SquaresC[1] == SquaresC[2]:
			PlayerWon(SquaresC[0])

		if SquaresA[0] == SquaresB[0] == SquaresC[0]:
			PlayerWon(SquaresA[0])

		if SquaresA[1] == SquaresB[1] == SquaresC[1]:
			PlayerWon(SquaresA[1])

		if SquaresA[2] == SquaresB[2] == SquaresC[2]:
			PlayerWon(SquaresA[2])

		if SquaresA[0] == SquaresB[1] == SquaresC[2]:
			PlayerWon(SquaresA[0])
		
		if SquaresA[2] == SquaresB[1] == SquaresC[0]:
			PlayerWon(SquaresA[2])

		if SquaresA.count("Vacant") == 0 and SquaresB.count("Vacant") == 0 and SquaresC.count("Vacant") == 0:
			PlayerWon("ITS A TIE SO NO ONE")


	while running:
		for event in pygame.event.get():
			if event == pygame.QUIT:
				running = False

		if Win:
			break

		screen.fill("black")
		FindWinner()

		#TIC TAC TOES
		pygame.draw.rect(screen, "grey", pygame.Rect(440, 160, 400, 400))
		pygame.draw.line(screen, "black", pygame.Vector2(440, 293), pygame.Vector2(840, 293), 3)
		pygame.draw.line(screen, "black", pygame.Vector2(440, 426), pygame.Vector2(840, 426), 3)
		pygame.draw.line(screen, "black", pygame.Vector2(573, 160), pygame.Vector2(573, 560), 3)
		pygame.draw.line(screen, "black", pygame.Vector2(706, 160), pygame.Vector2(706, 560), 3)

		Font.render_to(screen, (50, 250), "Cross: " + str(crossSCORE), "white")
		Font.render_to(screen, (50, 320), "Circle: " + str(circleSCORE), "white")

		lmb, rrb, rmb = pygame.mouse.get_pressed(num_buttons=3)

		if lmb:
			MousePosX, MousePosY = pygame.mouse.get_pos()

			if MousePosX > 440 and MousePosX < 573:
				rowX = 1

			elif MousePosX > 573 and MousePosX < 706:
				rowX = 2

			elif MousePosX > 706 and MousePosX < 840:
				rowX = 3

			else:
				rowX = 0

			if MousePosY > 160 and MousePosY < 293:
				rowY = 1

			elif MousePosY > 293 and MousePosY < 426:
				rowY = 2

			elif MousePosY > 426 and MousePosY < 560:
				rowY = 3

			else:
				rowY = 0

			ClaimSquare(rowX, rowY)

		for i in range(3):
			if SquaresA[i] == "CROSS":
				pygame.draw.line(screen, "red", pygame.Vector2(((i+1)*133)+307, 160), pygame.Vector2(((i+2)*133)+307, (2*133)+27),5)
				pygame.draw.line(screen, "red", pygame.Vector2(((i+2)*133)+307, 160), pygame.Vector2(((i+1)*133)+307, (2*133)+27),5)
			
			elif SquaresA[i] == "CIRCLE":
				pygame.draw.circle(screen, "blue", pygame.Vector2(((i+1)*133)+373, 226), 65, 5)

			if SquaresB[i] == "CROSS":
				pygame.draw.line(screen, "red", pygame.Vector2(((i+1)*133)+307, 293), pygame.Vector2(((i+2)*133)+307, 426),5)
				pygame.draw.line(screen, "red", pygame.Vector2(((i+2)*133)+307, 293), pygame.Vector2(((i+1)*133)+307, 426),5)

			elif SquaresB[i] == "CIRCLE":
				pygame.draw.circle(screen, "blue", pygame.Vector2(((i+1)*133)+373, 359), 65, 5)

			if SquaresC[i] == "CROSS":
				pygame.draw.line(screen, "red", pygame.Vector2(((i+1)*133)+307, 426), pygame.Vector2(((i+2)*133)+307, 559),5)
				pygame.draw.line(screen, "red", pygame.Vector2(((i+2)*133)+307, 426), pygame.Vector2(((i+1)*133)+307, 559),5)

			elif SquaresC[i] == "CIRCLE":
				pygame.draw.circle(screen, "blue", pygame.Vector2(((i+1)*133)+373, 492), 65, 5)

		pygame.display.flip()

		clock.tick(60)