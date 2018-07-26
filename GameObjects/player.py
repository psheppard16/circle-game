__author__ = 'psheppard16'
import math
from GameObjects.mobile import Mobile
class Player(Mobile):
    def __init__(self, window, x, y, xVel, yVel):
        super().__init__(window, x, y, xVel, yVel)
        self.window = window
        self.radius = 75
        self.starsCollected = 0

    def run(self):
        self.move()
        mouseX = (self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()) / self.window.gameEngine.scale
        mouseY = (self.window.height - self.window.root.winfo_pointery() + self.window.root.winfo_rooty()) / self.window.gameEngine.scale
        xComponent = mouseX - self.x
        yComponent = mouseY - self.y
        hypotenuse = math.sqrt(xComponent ** 2 + yComponent ** 2)
        if hypotenuse >= 10:
            xAcc = 500 * xComponent / hypotenuse
            yAcc = 500 * yComponent / hypotenuse
            self.changePosition(xAcc, yAcc)

        for circle in self.window.gameEngine.circleList:
                if circle.isTouching(self.x, self.y, self.radius):
                    xComponent = self.x - circle.x
                    yComponent = self.y - circle.y
                    angle = math.atan2(yComponent, xComponent)
                    hypotenuse = self.distanceToSelf(circle.x, circle.y)
                    distanceToMove = self.radius + circle.radius - hypotenuse
                    distanceX = distanceToMove * math.cos(angle)
                    distanceY = distanceToMove * math.sin(angle)
                    self.x += distanceX
                    self.y += distanceY

