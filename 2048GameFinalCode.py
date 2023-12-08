from tkinter import Frame, Label, CENTER
import GameLogic
import GameUIconstants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid() 
        self.master.title("2048")
        self.master.bind("<key>", self.keyDown) 
        # Key bindingd
        self.commands = {c.KEY_UP: GameLogic.upMove,c.KEY_DOWN: GameLogic.downMove, 
                        c.KEY_LEFT: GameLogic.leftMove, c.KEY_RIGHT: GameLogic.rightMove}
        self.gridCells = []
        self.initGrid()
        self.initMatrix() # intialize the matrix
        self.updateGridCells() # update the UI as [er the data re ceived]
        
        self.mainLoop()
    
    def initGrid(self):
        background = Frame(self, bg = c.backgroundColorGame, width = c.size, height = c.size)
        background.grid()
        for i in range(c.gridLen):
            gridRow = []
            for j in range(c.gridLen):
                cell = Frame(background, bg = c.BackgroundColorCell, width = c.size/ c.gridLen, 
                             height = c.size/ c.gridLen)
                cell.grid(row = i, column = j, padx = c.gridPadding, pady = c.gridPadding)
                t = Label(master=cell, text="", bg = c.BackgroundColorCell,
                          justify = CENTER,font = c.FONT, width =5, height = 2)
                t.grid()
                gridRow.append(t)
            self.gridCells.append(gridRow)
    
    def initMatrix(self):
        self.matrix = GameLogic.startGame()
        GameLogic.addNew2(self.matrix)
        GameLogic.addNew2(self.matrix)
    
    def updateGridCells(self):
        for i in range(c.gridLen):
            for j in range(c.gridLen):
                newNumber = self.matrix[i][j]
                if newNumber == 0:
                    self.gridCells[i][j].configure(text = "", bg = c.BackgroundColorCell)
                else:
                    self.gridCells[i][j].configure(text = str(newNumber), 
                    bg = c.BACKGROUND_COLOR_DICT[newNumber], fg = c.CELL_COLOR_DICT[newNumber])
        self.update_idletasks()
    
    def keyDown(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                GameLogic.addNew2(self.matrix)
                self.updateGridCells()
                changed = False
                if GameLogic.getCurrentState(self.matrix) == "WON":
                    self.gridCells[1][1].configure(text = "You", bg = c.BackgroundColorCell)
                    self.gridCells[1][2].configure(text = "Won!", bg = c.BackgroundColorCell)
                if GameLogic.getCurrentState(self.matrix) == "LOST":
                    self.gridCells[1][1].configure(text = "You", bg = c.BackgroundColorCell)
                    self.gridCells[1][2].configure(text = "Lose!", bg = c.BackgroundColorCell)
                    
gamegrid = Game2048()