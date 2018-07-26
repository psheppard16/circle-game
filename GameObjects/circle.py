__author__ = 'psheppard16'
import random
import math
from GameObjects.mobile import Mobile
class Circle(Mobile):
    def __init__(self, window, x, y, xVel, yVel, mass):
        super().__init__(window, x, y, xVel, yVel)
        self.mass = mass
        self.window = window
        self.startRadius = math.sqrt(self.mass / math.pi)
        self.radius = self.startRadius
        self.radiusOsc = 1.0
        self.grow = True
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (0, 255, 255), (128, 0, 255), (255, 0, 255)]
        self.color = random.choice(self.colors)
        self.alive = True

    def run(self):
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

    def isTouching(self, x, y, radius):
        if self.distanceToSelf(x, y) < self.radius + radius:
            return True
        else:
            return False