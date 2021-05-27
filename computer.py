class CMG:
    D_STONE = 1
    L_STONE = -1
    EMPTY = 0
    def __init__(self):
        self.myColor = self.D_STONE
        print("computer move generator here")


    def getNextMove(self, b, lastMove):
        pass
    def genRandomMove(self, b):
        randRow = randint(0, 18)