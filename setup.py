
class penteSetup:
    def __init__(self, sWidth, sHeight):
        self.updateBoard(sWidth, sHeight)
    def getBoardSize(self):
        return(self.boardSizeWH)
    def getBoardParams(self) -> object:
        return(self.boardStartXY[0], self.boardStartXY[0], self.boardSizeWH, self.boardSizeWH)
    def getScoreBParams(self):
        return(self.scoreWinXY[0], self.scoreWinXY[1], self.scoreWinWH[0], self.scoreWinWH[1])
        #return (10, 10, 150, 500)
    def getFinalW(self):
        return int(self.finalWidth)
    def getFinalH(self):
        return int(self.finalHeight)
    def getSquareSize(self):
        return int(self.boardSizeWH/19)
    def isLandscape(self):
        return self.landscape
    def isPortrait(self):
        return not self.landscape
    def updateBoard(self, newW, newH):
        self.sWidth = newW
        self.sHeight = newH

        self.mValue = 0.05
        self.spaceVal = min(self.sHeight, self.sWidth) * self.mValue

        if self.sWidth > self.sHeight:
            self.landscape = True


            self.boardStartXY = (self.spaceVal, self.spaceVal)
            self.boardSizeWH = self.sHeight - (self.spaceVal * 2)
            self.boardSizeWH = int(self.boardSizeWH/19) * 19

            self.scoreWinXY = (self.spaceVal + self.boardSizeWH + self.spaceVal, self.spaceVal)
            self.scoreWinWH = (self.boardSizeWH * (7 / 16), self.boardSizeWH)



            self.finalWidth = self.spaceVal + self.boardSizeWH + self.spaceVal + self.scoreWinWH[0] + self.spaceVal
            self.finalHeight = self.sHeight
        else:
            self.landscape = False

            self.boardStartXY = (self.spaceVal, self.spaceVal)
            self.boardSizeWH = self.sWidth - (self.spaceVal * 2)
            self.boardSizeWH = int(self.boardSizeWH / 19) * 19

            self.scoreWinXY = (self.spaceVal, self.spaceVal + self.boardSizeWH + self.spaceVal)
            self.scoreWinWH = (self.boardSizeWH, self.boardSizeWH * (7 / 16))

            self.finalHeight = self.spaceVal + self.boardSizeWH + self.spaceVal + self.scoreWinWH[1] + self.spaceVal
            self.finalWidth = self.sWidth
