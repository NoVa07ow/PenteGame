class Square:
    dark_color = 1
    empty = 0
    light_color = -1

    bg_color = (242, 215, 167)
    clickColor = (255, 255, 0)
    lslategrey = (119, 136, 153)
    lightStoneColor = (255, 255, 255)
    darkStoneColor = (36, 12, 10)

    def __init__(self, xLoc, yLoc, side, r, c):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.side = side
        self.myState = Square.empty
        self.clicked = False
        self.myRow = r
        self.myCol = c

    def ClickMe(self,pos):
        self.xPos = pos[0]
        self.yPos = pos[1]
        if self.xLoc < self.xPos < (self.xLoc + self.side) and self.yLoc < self.yPos (self.yLoc + self.side):
            return True
        else:
            return False

    def getDrawParams(self):
        return(self.xLoc, self.yLoc, self.side, self.side)
    def getState(self):
        return self.myState
    def getStoneColor(self):
        if self.myState == self.dark_color:
            return self.darkStoneColor
        else:
            return self.lightStoneColor
    def setState(self, newState):
        self.myState = newState
    def getBGColor(self):
        return self.bg_color
    def getLineColor(self):
        return self.lslategrey
    def resetXLoc(self, newXLoc):
        self.xLoc = newXLoc
    def resetYLoc(self, newYLoc):
        self.yLoc = newYLoc
    def resetSideW(self, newW):
        self.side = newW
    def getRow(self):
        return self.myRow
    def getCol(self):
        return self.myCol