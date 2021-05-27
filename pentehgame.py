import pygame
import tkinter as tk
import square as sq
import setup as setup


D_SQUARE_TURN = 1
L_SQUARE_TURN = -1
current_turn = 0
n_squares = 19
square_empty = 0

DScaptures = 0
LScaputers = 0

BG_BLUE = (66, 218, 245)
BOARD_AREA_COLOR = (242, 215, 167)
BOARD_BORDER = (255, 0, 0)
SCORE_B_COLOR = (255, 255, 255)
SCORE_B_BORDER = (0, 0, 255)
red = (255, 0, 0)

root = tk.Tk()
S_WIDTH = root.winfo_screenwidth()
S_HEIGHT = root.winfo_screenheight() - 60
print("The screen width and height is:", S_WIDTH, S_HEIGHT)

setup = setup.penteSetup(S_WIDTH, S_HEIGHT)
print(setup)

pygame.init()
screen = pygame.display.set_mode((setup.getFinalW(), setup.getFinalH()),pygame.RESIZABLE)
pygame.display.set_caption("lets play pente")

d_image = pygame.image.load('images/dark_stone_image250.png')
l_image = pygame.image.load('images/light_stone_image250.png')

cur_dImage = d_image
cur_lImage = l_image
gameOn = True



def GameAreas():
    pygame.draw.rect(screen,BOARD_AREA_COLOR, setup.getBoardParams())
    pygame.draw.rect(screen, BOARD_BORDER, setup.getBoardParams(), 2)

    pygame.draw.rect(screen, SCORE_B_COLOR, setup.getScoreBParams())
    pygame.draw.rect(screen, SCORE_B_BORDER, setup.getScoreBParams(), 2)

def drawSquares(s, screen):
    squareParams = s.getDrawParams()
    squareX = squareParams[0]
    squareY = squareParams[1]
    squareW = squareParams[2]
    squareH = squareParams[3]
    squareColor = s.getBGColor()
    squareLC =  s.getLineColor()

    if s.getRow() == 0 and s.getCol() == 0:
        print("In drawSquares -- x y for first square is ", squareX, squareY)

    pygame.draw.rect(screen, squareColor, squareParams)

    pygame.draw.line(screen, squareLC, (squareX + squareW/2, squareY), (squareX + squareW/2, squareY + squareH), 1)
    pygame.draw.line(screen, squareLC, (squareX, squareY + squareH / 2), (squareX + squareW, squareY + squareH / 2), 1)

    if s.getState() != square_empty:
        if s.getState() == D_SQUARE_TURN:
            dImage4Square = cur_dImage
            screen.blit(dImage4Square, (squareX,squareY))
        else:
            limage4Square = cur_lImage
            screen.blit(limage4Square, (squareX, squareY))
def makeBoard():
    global cur_dImage, cur_lImage
    b = []
    firstX, firstY, firstW, firstH = setup.getBoardParams()

    print("In makeBoard, firstX, firstY are: ", firstX, firstY)
    newSW = setup.getSquareSize()
    cur_dImage = pygame.transform.scale(d_image, (newSW, newSW))
    cur_lImage = pygame.transform.scale(l_image, (newSW, newSW))
    squareWidth = int(firstW / 19)

    for row in range(19):
        newR = []
        for col in range(19):
            newSq = sq.Square(firstX + (col * squareWidth), firstY + (row * squareWidth), squareWidth, row,  col)
            if row == 0 and col == 0:
                dp = newSq.getDrawParams()
                print("newSq xy are ", dp[0], dp[1])
            newR.append(newSq)
        b.append(newR)

    return b

def drawBoard(b, s):
    for row in range(19):
        for col in range(19):
            drawSquares(b[row][col], s)


def clickCheck(pos, b):
    squareClicked = None
    for row in range(19):
        for col in range(19):
            if b[row][col].didClickMe(pos) == True:
                squareClicked = b[row][col]
    return squareClicked

def resetSquares(b):
    global cur_dImage, cur_lImage
    firstX, firstY, firstX, firstH = setup.getBoardParams()
    newSquares = setup.getSquareSize()
    cur_dImage = pygame.transform.scale(d_image, (newSquares, newSquares))
    cur_lImage = pygame.transform.scale(l_image, (newSquares, newSquares))
    for row in range(19):
        for col in range(19):
            b[row][col].resetXLoc(firstX + (col * newSquares))
            b[row][col].resetYLoc(firstY + (row * newSquares))
            b[row][col].resetSideW(newSquares)
def captureCheck(s, b, curT):
    global DScaptures, LScaputers
    curRow = s.getRow()
    curCol = s.getCol()
    LEFT_D = UP_D = -1
    RIGHT_D = DOWN_D = 1
    for vDir in range(UP_D, DOWN_D + 1):
        if not ((vDir > 0 and curRow > 15) or (vDir < 0 and curRow < 3)):
            for hDir in range(LEFT_D, RIGHT_D + 1):
              if not ((hDir > 0 and curCol > 15) or (hDir < 0 and curCol < 3)):
                  if b[curRow + (1 * vDir)][curCol + (1 * hDir)].getState() == (curT * -1):
                      if b[curRow + (2 * vDir)][curCol + (2 * hDir)].getState() == (curT * -2):
                          if b[curRow + (3 * vDir)][curCol + (3 * hDir)].getState() == (curT * -3):
                                b[curRow + (1 * vDir)][curCol + (1 * hDir)].getState(SQUARE_EMPTY)
                                b[curRow + (2 * vDir)][curCol + (2 * hDir)].getState(SQUARE_EMPTY)

                                if curT == D_SQUARE_TURN:
                                    DScaptures += 1
                                else:
                                    LScaputers += 1
    print(f"DSCaptures: {DScaptures}")
    print(f"LSCaptures: {LScaptures}")


def startGame(b):
    global current_turn, DScaptures, LScaputers
    DScaptures = 0
    LScaputers = 0
    b[int(n_squares/2)][int(n_squares/2)].setState(D_SQUARE_TURN)
    current_turn = L_SQUARE_TURN

def playGame (p, b):
    global current_turn
    print(f"in playGame current turn is {current_turn}")
    boardSquareClicked = clickCheck(p, b)
    if boardSquareClicked == None:
        print("you didnt click on a square. Try again")
    else:

        if boardSquareClicked.getState() == SQUARE_EMPTY:
            boardSquareClicked.setState(currentTurn)
            captureCheck(boardSquareClicked, b, currentTurn)
            currentTurn *= -1


theBoard = makeBoard()
startGame(theBoard)

while gameOn:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
                print("peace")
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            if event.type == pygame.VIDEORESIZE:
                w = event.w
                h = event.h
                setup.updateBoard(w, h)
                screen = pygame.display.set_mode((setup.getFinalW(), setup.getFinalH()), pygame.RESIZABLE)

                resetSquares(theBoard)
    screen.fill(BG_BLUE)
    GameAreas()
    drawBoard(theBoard, screen)
    pygame.display.flip()
print("out")
pygame.quit()