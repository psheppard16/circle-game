__author__ = 'psheppard16'
import math
from GameObjects.mobile import Mobile
class Star(Mobile):
    def __init__(self, window, x, y, xVel, yVel, radius):
        super().__init__(window, x, y, xVel, yVel)
        self.window = window
        self.startRadius = radius / 2
        self.radius = self.startRadius
        self.radiusOsc = 1.0
        self.grow = True
        self.alive = True
        self.angle = 0
        self.cannotDespawn = 0
        self.pointList = []
        self.largeRadius = True
        for angle in range(0, 360, 36):
            if self.largeRadius:
                self.largeRadius = False
                x = self.radius * math.sin(math.radians(angle - self.angle)) * self.window.gameEngine.scale
                y = self.radius * math.cos(math.radians(angle - self.angle)) * self.window.gameEngine.scale
            else:
                self.largeRadius = True
                x = self.radius * math.sin(math.radians(angle - self.angle)) / 2 * self.window.gameEngine.scale
                y = self.radius * math.cos(math.radians(angle - self.angle)) / 2 * self.window.gameEngine.scale
            self.pointList.append((x, y))

    def run(self):
        #rotate star
        if self.angle < 360 + 360 * self.window.frameRate.TICK_SPEED:
            self.angle += 180 * self.window.frameRate.TICK_SPEED
        else:
            self.angle = 0

        #size oscillation
        if self.grow:
            self.radiusOsc += 3.0 * self.window.frameRate.TICK_SPEED
        else:
            self.radiusOsc -= 3.0 * self.window.frameRate.TICK_SPEED
        if self.radiusOsc > 1.25 and self.grow:
            self.radiusOsc = 1.25
            self.grow = False
        if self.radiusOsc < .75 and not self.grow:
            self.radiusOsc = .75
            self.grow = True
        self.radius = self.startRadius * self.radiusOsc * 2

        #update outline
        self.pointList.clear()
        for angle in range(0, 360, 36):
            if self.largeRadius:
                self.largeRadius = False
                x = self.radius * math.sin(math.radians(angle - self.angle)) * self.window.gameEngine.scale
                y = self.radius * math.cos(math.radians(angle - self.angle)) * self.window.gameEngine.scale
            else:
                self.largeRadius = True
                x = self.radius * math.sin(math.radians(angle - self.angle)) / 2 * self.window.gameEngine.scale
                y = self.radius * math.cos(math.radians(angle - self.angle)) / 2 * self.window.gameEngine.scale
            self.pointList.append((x, y))

    def aliveCheck(self, x, y):
        if self.distance(x, y, self.x, self.y) < self.radius + self.window.gameEngine.player.radius:
            self.alive = False
            self.window.gameEngine.player.starsCollected += 1

    def distance(self, x1, y1, x2, y2):
        xD = x1 - x2
        yD = y1 - y2
        return math.sqrt(xD ** 2 + yD ** 2)