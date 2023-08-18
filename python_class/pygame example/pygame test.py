import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
RED = (255, 0 ,0)

size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

offs = 30 # 격자 크기
thick = 3 # 선굵기

def drawGrid(m, n):
    '''
    :param m: 격자무늬 행 개수
    :param n: 격자무늬 열 개수
    '''
    x = 0 
    y = 0
    for j in range(1, m+2):
        pygame.draw.line(screen, RED, (x,y), (x + n*offs, y), thick)
        y = j * offs
        print(y)
    x = 0
    y = 0
    for i in range(1, n+2):
        pygame.draw.line(screen, RED, (x,y), (x, y + m*offs), thick)
        x = i * offs

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        drawGrid(3, 4)
        '''where = screen, color = (0, 0, 255), rect = (x, y, width, height)
        pygame.draw.rect(screen, (0, 0, 255), (0, 0, 200, 100), 1)
        '''

        '''
        # where = screen, color = (0, 0,255), 중심좌표(x,y) = (100, 200), radius(반지름) = 30
        pygame.draw.circle(screen, (0,0,255), (100, 200), 30, 1)
        pygame.draw.circle(screen, (0,0,255), (160, 200), 30, 2)
        pygame.draw.circle(screen, (0,0,255), (220, 200), 30, 3)

        pygame.draw.line(screen, (255, 0, 0), (0, 0), (200,0))
        pygame.draw.line(screen, (255,0,0),(0,20),(200,20), 3)
        pygame.draw.line(screen, (255, 0, 0), (0, 40), (200, 40), 6)
        '''
        '''
        num_of_lines = 3
        gap = 20
        #가로선
        for y_idx in range(num_of_lines + 1):
            y_pos = y_idx * gap
            pygame.draw.line(screen, (255,0,0),(0, y_pos), (gap*num_of_lines, y_pos), 3)
        for x_idx in range(num_of_lines+1):
            x_pos = x_idx * gap
            pygame.draw.line(screen, (255,0,0), (x_pos, 0), (x_pos, gap*num_of_lines), 3)
        '''
        '''
        pygame.draw.rect(screen, (0, 0, 0), (40, 40, 120, 240), 1)
        pygame.draw.line(screen, (0,0,0),(100,280),(100,380), 1)
        pygame.draw.circle(screen, (255,0,0),(100,100), 30)
        pygame.draw.circle(screen, (255,255,0),(100,160), 30)
        pygame.draw.circle(screen, (0,255,0),(100,220), 30)
        pygame.display.update()
        '''

        pygame.display.update()
runGame()
pygame.quit()