import pygame
import cv2
import time
cap  =cv2.VideoCapture(0)
pygame.init()
size = (1280,720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ronny")

endGame = False
while (not endGame) and cap.isOpened():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame = True
    img = cap.read()[1]
    start = time.clock()
    cv2.imwrite("img.jpg",img)
    pyimg = pygame.image.load("img.jpg")
    print(1.0/(time.clock() - start))
    screen.blit(pyimg,(0,0))
    pos = pygame.mouse.get_pos()
    pygame.display.update()

pygame.quit()
quit()
exit()
