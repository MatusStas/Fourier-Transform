import pygame
import math

(WIDTH, HEIGHT) = (1024,512)
running = True
FPS = 60

BackgroundColor = (0,0,0)
ArrOfCircles = []

def COS(angle):
    return math.cos(math.radians(angle))


def SIN(angle):
    return math.sin(math.radians(angle))

def update():
    for c in range(1,len(ArrOfCircles),1):
        ArrOfCircles[c].x_start = ArrOfCircles[c-1].x_end
        ArrOfCircles[c].y_start = ArrOfCircles[c-1].y_end


class Circle:
    def __init__(self,x_start,y_start,radius,angle,offset,x_end,y_end,color_line):
        self.x_start = x_start
        self.y_start = y_start
        self.radius = radius
        self.angle = angle
        self.offset = offset
        self.x_end = x_end
        self.y_end = y_end
        self.color_line = color_line

    def DrawCirle(self,x_start,y_start,radius):
        pygame.draw.circle(window,(255,255,255),(int(x_start),int(y_start)),radius,2)

    def DrawLine(self,x_start,y_start,x_end,y_end):
        pygame.draw.line(window, (128,128,128), (x_start,y_start),(x_end,y_end),1)

    def update(self):
        self.angle += self.offset
        self.x_end = self.radius*COS(self.angle)+self.x_start
        self.y_end = self.y_start - self.radius*SIN(self.angle)

class Wave:
    def __init__(self):
        self.x = ArrOfCircles[-1].x_end+100
        self.y = ArrOfCircles[-1].y_end
        self.X = ArrOfCircles[-2].x_end+100
        self.Y = ArrOfCircles[-2].y_end
        self.arr = [[self.x,self.y],[self.X,self.Y]]

    def DrawWave(self):
        self.y = ArrOfCircles[-1].y_end
        self.Y = ArrOfCircles[-2].y_end
        self.arr.append([self.x,self.y])
        self.arr.append([self.X,self.Y])

        for i in range(1,len(self.arr),1):
            pygame.draw.line(window,(255,255,255),(self.arr[i]),(self.arr[i-1]),2)

        for j in self.arr:
            j[0] += 1

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

ArrOfCircles.append(Circle(WIDTH//3, HEIGHT//2, 128, 88, 1, 128 *COS(88)+WIDTH//2,HEIGHT//2-128
                           *SIN(88), (128, 128, 128)))

#amount = int(input("NUMBER OF WAVES: "))
amount = 32
mod = 1
inc = 3
for rot in range(3,amount*2,2):
    if mod%2 == 1:
        ArrOfCircles.append(Circle(ArrOfCircles[-1].x_end, ArrOfCircles[-1].y_end, ArrOfCircles[0].radius // rot, 270-inc*rot, rot,ArrOfCircles[-1].radius // rot * COS(270-inc*rot) + ArrOfCircles[-1].x_end,ArrOfCircles[-1].y_end - ArrOfCircles[-1].radius //rot * SIN(270-inc*rot), (128, 128, 128)))
    else:
        ArrOfCircles.append(Circle(ArrOfCircles[-1].x_end, ArrOfCircles[-1].y_end, ArrOfCircles[0].radius // rot, 90 - inc * rot, rot,ArrOfCircles[-1].radius // rot * COS(270 - inc * rot) + ArrOfCircles[-1].x_end,ArrOfCircles[-1].y_end - ArrOfCircles[-1].radius // rot * SIN(90 - inc * rot), (128, 128, 128)))

    mod += 1
    inc += 1

w = Wave()
while running:
    pygame.time.delay(int(1000/FPS))

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                running = False
                break

    pygame.display.update()
    window.fill(BackgroundColor)
    for c in ArrOfCircles:
        c.DrawCirle(c.x_start,c.y_start,c.radius)
        c.DrawLine(c.x_start,c.y_start,c.x_end,c.y_end)
        c.update()

    pygame.draw.line(window,(128,128,128),(ArrOfCircles[-1].x_end,ArrOfCircles[-1].y_end),(w.x,w.y))
    w.DrawWave()
    update()