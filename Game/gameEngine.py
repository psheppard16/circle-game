from GameObjects.circle import Circle
from GameObjects.star import Star
from GameObjects.player import Player
import random
class GameEngine:
    def __init__(self, window):
        self.window = window
        self.player = Player(self.window, 1280 / 2, 720 / 2, 0, 0)
        self.circleList = []
        self.starList = []
        self.spawnCircles()
        self.timeLeft = 30
        self.scale = self.window.width / 1280
        self.newHighScore = False

    def runGame(self):
        self.timeLeft -= self.window.frameRate.TICK_SPEED
        self.player.run()
        self.runCircles()
        self.runStars()
        self.spawnStars()
        if self.timeLeft <= 0:
            if self.window.save.highScore < self.player.starsCollected:
                self.window.save.highScore = self.player.starsCollected
                self.newHighScore = True
            self.window.rMenu = "summaryScreen"

    def runCircles(self):
        for circle in self.circleList:
            circle.run()

    def runStars(self):
        for star in self.starList:
            star.run()
            star.aliveCheck(self.player.x, self.player.y)
            if star.alive == False:
                self.starList.remove(star)

    def spawnStars(self):
        randomNumber = random.randint(0, 100)
        if randomNumber > 25 + len(self.starList):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            xVel = 0
            yVel = 0
            radius = random.randint(10, 100)
            canSpawn = True
            for circle in self.circleList:
                if circle.isTouching(x, y, radius):
                    canSpawn = False
            if canSpawn:
                self.starList.append(Star(self.window, x, y, xVel, yVel, radius))

    def spawnCircles(self):
        numberOfBlobs = 10
        if self.window.save == "easy":
            numberOfBlobs = 10
        elif self.window.save == "medium":
            numberOfBlobs = 20
        elif self.window.save == "hard":
            numberOfBlobs = 30
        for i in range(numberOfBlobs):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            xVel = 0
            yVel = 0
            mass = random.randint(100, 1000)
            self.circleList.append(Circle(self.window, x, y, xVel, yVel, mass))

    def kp(self, event):
        pass

    def kr(self, event):
        pass




