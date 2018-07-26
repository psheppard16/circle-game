from tkinter import *
from Screens.screen import Screen
class SummaryScreen(Screen):
    def __init__(self, window):
        super().__init__(window, "summaryScreen")
        self.startsCollected = StringVar()
        self.starLabel = Label(self.window.root, text="Stars collected: " + str(self.window.gameEngine.player.starsCollected), bg="#%02x%02x%02x" % (0, 165, 0), font="Helvetica 50 bold")
        self.starLabel.pack(in_=self.f, pady=25)
        self.highScoreLabel = Label(self.window.root, text="High score: " + str(self.window.save.highScore), bg="#%02x%02x%02x" % (0, 165, 0), font="Helvetica 50 bold")
        self.highScoreLabel.pack(in_=self.f, pady=25)
        self.newHighScoreLabel = Label(self.window.root, text="New high score!", bg="#%02x%02x%02x" % (0, 165, 0), font="Helvetica 50 bold")
        self.accept = Button(self.window.root, text="Continue", command=self.accept, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.f, pady=25)

    def setUp(self):
        self.starLabel.config(text="Stars collected: " + str(self.window.gameEngine.player.starsCollected))
        self.highScoreLabel.config(text="High score: " + str(self.window.save.highScore))
        if self.window.gameEngine.newHighScore:
            self.newHighScoreLabel.pack(in_=self.f, pady=25)
        else:
            self.newHighScoreLabel.pack_forget()
        self.f.pack(side=LEFT)

    def accept(self):
        self.window.rMenu = "mainMenu"