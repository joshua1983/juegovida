#
# Juego de la vida por Josue Barrios: josue.barrios at gmail punto com
#
import pygame, time, sys, numpy as np

pygame.init()

size = width, height = 600, 600

fondo = 25,25,25
screen = pygame.display.set_mode(size)
nxC, nyC = 50, 50
dimCW = width / nxC
dimCH = height / nyC
screen.fill(fondo)

# celdas 1= viva y 0 muerta
gameState = np.zeros((nxC, nyC))

#automata palo
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1


#Automata movil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

while 1:

    newGameState = np.copy(gameState)

    screen.fill(fondo)
    time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        #detectar si presiona el mouse
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    for y in range(0, nxC):
        for x in range(0, nyC):
            #calcular el numero de vecinos cercanos
            n_neigh  = gameState[(x-1) % nxC, (y-1) % nyC] + \
                       gameState[(x)   % nxC, (y-1) % nyC] + \
                       gameState[(x+1) % nxC, (y-1) % nyC] + \
                       gameState[(x-1) % nxC, (y)   % nyC] + \
                       gameState[(x+1) % nxC, (y)   % nyC] + \
                       gameState[(x-1) % nxC, (y+1) % nyC] + \
                       gameState[(x)   % nxC, (y+1) % nyC] + \
                       gameState[(x+1) % nxC, (y+1) % nyC]

            # regla 1: una celula muerta con 3 vecinas vivas, "revive"
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # regla 2: una celula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # rejilla
            poly = [((x) * dimCW, y * dimCH), ((x+1) * dimCW, y *dimCH), ((x+1) * dimCW, (y+1) *dimCH), ((x) * dimCW, (y+1) *dimCH)]

            #Dibujar la celda para cada par de x, y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)


    gameState = np.copy(newGameState)

    pygame.display.flip()