from math import sin, cos, pi

widthScreen, heightScreen = 1080, 720
fps = 30
lengthOfBlock = 25

class Barrier:
    def __init__(self, *listOfDots):
        self.dots = listOfDots

    def __repr__(self):
        return f'Barrier( {self.dots} )'

    def itemise(self):
        dots = self.dots
        if len(dots) == 2:
            d1, d2 = dots[0], dots[1]
            length = math.sqrt((d2[0]-d1[0])**2 + (d2[1]-d1[1])**2)
            if length > lengthOfBlock * 1.5:
                #  print('Breaking Barrier into pieces:')
                out = []
                blocks = round(length / lengthOfBlock)
                xCh = (d2[0] - d1[0]) / blocks
                yCh = (d2[1] - d1[1]) / blocks
                x, y = d1[0], d1[1]
                for i in range(blocks):
                    #  print(f'\tBarrier(({x},{y}), ({x+xCh},{y+yCh}))')
                    out.append(Barrier((x, y), (x+xCh, y+yCh)))
                    x = x + xCh
                    y = y + yCh
                return out
            else:
                return [self]
        elif len(dots) > 2:
            out = []
            for n in range(len(dots)-1):
                #  print(f'Making Barrier({dots[n]}, {dots[n+1]})')
                out.extend([*Barrier(dots[n], dots[n+1]).itemise()])
                print()
            return out



class Tank:
    def __init__(self, x, y, direction, gun, size, diff, forwardSpeed, backwardSpeed, rotSpeed, color=(255, 40, 40)):
        self.x, self.y = x, y
        self.direction = direction
        self.size = size
        self.color = color
        self.prop = diff
        self.speed = forwardSpeed
        self.backwardSpeed = backwardSpeed
        self.rotSpeed = rotSpeed
        self.gun = gun

    def draw(self, display):
        x, y = self.x, self.y
        direction = self.direction
        prop = self.prop
        size = self.size
        points = ((x + cos(direction + pi/4 * (1-prop)) * size,  y + sin(direction + pi/4 * (1-prop)) * size),
                  (x + cos(direction + pi/4 * (3+prop)) * size,  y + sin(direction + pi/4 * (3+prop)) * size),
                  (x + cos(direction + pi/4 * (5-prop)) * size,  y + sin(direction + pi/4 * (5-prop)) * size),
                  (x + cos(direction + pi/4 * (7+prop)) * size,  y + sin(direction + pi/4 * (7+prop)) * size))

        pygame.draw.polygon(display, self.color, points, size // 4)

    def moveForward(self):
        self.x = self.x + cos(self.direction) * self.speed
        self.y = self.y + sin(self.direction) * self.speed

    def moveBackward(self):
        self.x = self.x - cos(self.direction) * self.backwardSpeed
        self.y = self.y - sin(self.direction) * self.backwardSpeed

    def rotRight(self):
        self.direction = self.direction + self.rotSpeed

    def rotLeft(self):
        self.direction = self.direction - self.rotSpeed


class Gun:
    def __init__(self, relTurn, rotSpeed, bulletSpeed, bulletsLimit, reloadingTime, color=(127, 20, 20)):
        self.relTurn = relTurn
        self.rotSpeed = rotSpeed
        self.bulletSpeed = bulletSpeed
        self.bulletsLimit = bulletsLimit
        self.bullets = 0
        self.reloadingTime = reloadingTime
        self.reloading = 0
        self.color = color

    def draw(self, display, receiver):
        direction = receiver.direction + self.relTurn
        p1 = (receiver.x + cos(direction), receiver.y + sin(direction))
        p2 = (receiver.x + cos(direction) * receiver.size * 1.2, receiver.y + sin(direction) * receiver.size * 1.2)

        pygame.draw.line(display, self.color, p1, p2, receiver.size // 6)
        pygame.draw.circle(display, self.color, (receiver.x, receiver.y), receiver.size / 3, receiver.size // 6)

    def rotRight(self):
        self.relTurn = self.relTurn + self.rotSpeed

    def rotLeft(self):
        self.relTurn = self.relTurn - self.rotSpeed

    def reload(self):
        self.reloading -= 1
        if self.bullets < self.bulletsLimit and self.reloading < 0:
            self.bullets += 1
            self.reloading = self.reloadingTime

    def shoot(self, receiver):
        if self.bullets > 0 and self.reloading < self.reloadingTime - 3:
            self.bullets = self.bullets - 1
            self.reloading = self.reloadingTime
            direction = receiver.direction + self.relTurn
            x, y = receiver.x + cos(direction) * receiver.size, receiver.y + sin(direction) * receiver.size
            return Bullet(x, y, direction, self.bulletSpeed, 1)
        return None


class Bullet:
    def __init__(self, x, y, direction, speed, force, color=(20, 20, 20)):
        self.x, self.y = x, y
        self.direction = direction
        self.speed = speed
        self.force = force
        self.color = color

    def fly(self):
        self.x = self.x + cos(self.direction) * self.speed
        self.y = self.y + sin(self.direction) * self.speed
        return self

    def inFrame(self):
        return (0 < self.x < widthScreen) and (0 < self.y < heightScreen)

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), 3, 4)



basicGun = Gun(0, 0.05, 5, 3, 10)
ourTank = Tank(widthScreen // 3, heightScreen // 2, 0, basicGun, 50, 0.2, 3, 2, 0.03)


pygame.init()
ourDisplay = pygame.display.set_mode((widthScreen, heightScreen))
pygame.display.set_caption('Tnks')
clock = pygame.time.Clock()


tracked = (pygame.K_SPACE, pygame.K_UP, pygame.K_DOWN,
           pygame.K_LEFT, pygame.K_RIGHT,
           pygame.K_a, pygame.K_d)
keyboard = {key: False for key in tracked}

bullets = []

closed = False
while not closed:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in tracked:
            keyboard[event.key] = True
        elif event.type == pygame.KEYUP and event.key in tracked:
            keyboard[event.key] = False
        elif event.type == pygame.QUIT:
            closed = True

    if keyboard[pygame.K_UP]:
        ourTank.moveForward()
    if keyboard[pygame.K_DOWN]:
        ourTank.moveBackward()
    if keyboard[pygame.K_LEFT]:
        ourTank.rotLeft()
    if keyboard[pygame.K_RIGHT]:
        ourTank.rotRight()
    if keyboard[pygame.K_a]:
        ourTank.gun.rotLeft()
    if keyboard[pygame.K_d]:
        ourTank.gun.rotRight()
    if keyboard[pygame.K_SPACE]:
        shoot = ourTank.gun.shoot(ourTank)
        if shoot:
            bullets.append(shoot)

    bullets = [bullet.fly() for bullet in bullets if bullet.inFrame()]
    ourTank.gun.reload()

    ourDisplay.fill((240, 240, 240))
    ourTank.draw(ourDisplay)
    ourTank.gun.draw(ourDisplay, ourTank)
    for bullet in bullets:
        bullet.draw(ourDisplay)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
