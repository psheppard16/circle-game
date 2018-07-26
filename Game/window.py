__author__ = 'psheppard16'
import tkinter
import pickle
from Screens.instructions import Instructions
from Screens.startScreen import StartScreen
from Screens.saveScreen import SaveScreen
from Screens.summaryScreen import SummaryScreen
from Screens.options import Options
from Screens.mainMenu import MainMenu
from Game.frameRate import FrameRate
from Game.gameEngine import GameEngine
from SaveFiles.saveFile import SaveFile
from Display.drawingEngine import DrawingEngine
class Window:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.cMenu = "null"
        self.rMenu = "startScreen"

        self.root = tkinter.Tk()
        self.root.title("Red Siege")
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.root.bind_all('<KeyPress>', self.kp)
        self.root.bind_all('<KeyRelease>', self.kr)

        self.saveNumber = 0
        self.saveSelected = False
        self.save = SaveFile()

        #self.saveCharacter(1) # resets the saves
        #self.saveCharacter(2)
        #self.saveCharacter(3)

        self.screenList = [] #when a class that extends Screen is created it automatically adds itself to screenList
        self.frameRate = FrameRate(self)
        self.startScreen = StartScreen(self)
        self.instructions = Instructions(self)
        self.gameEngine = GameEngine(self)
        self.drawingEngine = DrawingEngine(self)
        self.saveScreen = SaveScreen(self)
        self.summarySreen = SummaryScreen(self)
        self.mainMenu = MainMenu(self)
        self.options = Options(self)

        self.root.after(1, self.loop)
        self.root.mainloop()

    def loop(self):
        while True:
            self.root.focus_force()
            if self.frameRate.getTime() > self.frameRate.nextTick:
                self.frameRate.tickStartTime = self.frameRate.getTime()

                self.updateFrameSizes()
                self.switchScreen()

                if self.cMenu == "gameEngine":
                    self.gameEngine.runGame()
                    self.drawingEngine.render(self.gameEngine.player, self.gameEngine.circleList, self.gameEngine.starList)
                else:
                    self.root.update()
                self.frameRate.update()

    def switchScreen(self):
        if self.cMenu != self.rMenu:
            if self.saveSelected:
                    self.saveCharacter(self.saveNumber)

            self.clearWindow()
            for screen in self.screenList:
                if self.rMenu == screen.name:
                    screen.setUp()
                    self.cMenu = self.rMenu
            if self.rMenu == "gameEngine":
                self.gameEngine = GameEngine(self)
            self.cMenu = self.rMenu

    def clearWindow(self):
        for screen in self.screenList:
            screen.hide()
        self.drawingEngine.hide()

    def updateFrameSizes(self):
        if str(self.width) + 'x' + str(self.height) != self.save.resolution:
            self.root.geometry(self.save.resolution)
            split = self.save.resolution.replace("x", " ").split()
            self.width = int(split[0])
            self.height = int(split[1])
            for screen in self.screenList:
                screen.update()

    def loadChar(self, number):
        try:
            if number == 1:
                with open('SaveFiles/saveFile1', 'rb') as input:
                    self.save = pickle.load(input)
            elif number == 2:
                with open('SaveFiles/saveFile2', 'rb') as input:
                    self.save = pickle.load(input)
            elif number == 3:
                with open('SaveFiles/saveFile3', 'rb') as input:
                    self.save = pickle.load(input)
        except EOFError:
            return {}

    def saveCharacter(self, number):
        if number == 1:
            with open('SaveFiles/saveFile1', 'wb') as output:
                pickle.dump(self.save, output, pickle.HIGHEST_PROTOCOL)
        elif number == 2:
            with open('SaveFiles/saveFile2', 'wb') as output:
                pickle.dump(self.save, output, pickle.HIGHEST_PROTOCOL)
        elif number == 3:
            with open('SaveFiles/saveFile3', 'wb') as output:
                pickle.dump(self.save, output, pickle.HIGHEST_PROTOCOL)

    def kp(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.kp(event)

    def kr(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.kr(event)