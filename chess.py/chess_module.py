
import pygame as pg
import time

window = pg.display.set_mode((960,960)) #120 * 8 =960, so each tile is 120x120

#var før i chess.py - ændre måske
def createBoardDisplay():
    startPos = 120
    for y in range(8):
        for x in range(8):
            if y % 2 == 0:
                if x % 2 == 0:
                    color = 211
                else:
                    color = 50
            else:
                if x % 2 == 0:
                    color = 50
                else:
                    color = 211
            pg.draw.rect(window,(color,color,color),(startPos*x,startPos*y,120,120))

def printRow(rowToPrint,board):
    x = rowToPrint+10
    while x < 90:
        print(board[x],end=" ")
        x += 10  
    print("\n") 

def displayBoard(board):
    for x in reversed(range(1,9)):
        printRow(x,board)

def createStartBoard():
    return board


def codePosToGamePos(codePos): #takes list as parameter  #denne funktion er også i den anden fil, måske de blot skal skrives i en fil alt sammen
    gamePos = codePos.copy()
    return [(i-1)*120 for i in gamePos]

class ChessPiece():
    def __init__(self,startPosition,isWhite,type):
        self.pos = startPosition
        self.gamePosX,self.gamePosY = codePosToGamePos(self.pos)
        print("AAAAAAHHHHH:",codePosToGamePos(self.pos))
        if isWhite == True: 
            self.image = pg.image.load("chess_Pieces\\white\\" + type + ".png")  
        else:
            self.image = pg.image.load("chess_Pieces\\black\\" + type + ".png")
        self.rect = self.image.get_rect() #det giver størrelsen på billedet. dette kan måske bruges til at lave en rect omkring den størrelse - men her skal vi alligevel bruge 120x120
        self.hitBox = pg.draw.rect(window,(0,0,0,0.0),(self.gamePosX,self.gamePosY,120,120))
        self.isSelected = False
    def changePos(self):
        print("pos change")
    def highlightPiece(self): #denne funktion kan ikke bruges men hvis den slettes er jeg bange for den fucker - den kan dog bruges af ekslusivt af blackPawns
        print(self.pos)
    def die(self):
        print("die")
        #fjern instance af den
        #måske bare gør pladsen til uden for 0,0 og 8,8
    def selectPiece(self):
        self.hitBox = pg.draw.rect(window,(255,255,0),(self.gamePosX,self.gamePosY,120,120))
        self.isSelected = True
    def unSelectPiece(self):
        createBoardDisplay() #skal måske fjernes
        #self.hitBox = pg.draw.rect(window,((0,0,0,0)),(self.gamePosX,self.gamePosY,120,120))
        self.isSelected = False
        



class King(ChessPiece):
    def __init__(self,isWhite,startPosition): #position = [x,y] where x and y range from 1-8 (both inclusive) (top left is [1,1])
        if isWhite == True:
            ChessPiece.__init__(self,startPosition,True,"King")
        else:
            ChessPiece.__init__(self,startPosition,False,"King")


class Queen(ChessPiece):
    def __init__(self,isWhite,startPosition):
        if isWhite == True:
            ChessPiece.__init__(self,startPosition,True,"Queen")
        else:
            ChessPiece.__init__(self,startPosition,False,"Queen")
class Rook(ChessPiece): #tårn
    def __init__(self,isWhite,startPosition):
        if isWhite == True:
            ChessPiece.__init__(self,startPosition,True,"Rook")
        else:
            ChessPiece.__init__(self,startPosition,False,"Rook")
class Bishop(ChessPiece): #løber
    def __init__(self,isWhite,startPosition):
        if isWhite == True:
            ChessPiece.__init__(self,startPosition,True,"Bishop")
        else:
            ChessPiece.__init__(self,startPosition,False,"Bishop")
class Knight(ChessPiece): #hest
    def __init__(self,isWhite,startPosition):
        if isWhite == True:
            ChessPiece.__init__(self,startPosition,True,"Knight")
        else:
            ChessPiece.__init__(self,startPosition,False,"Knight")

class Pawn(ChessPiece): #bonde
    def __init__(self,isWhite,startPosition):
        if isWhite == True:
            ChessPiece.__init__(self,startPosition,True,"Pawn")
        else:
            ChessPiece.__init__(self,startPosition,False,"Pawn")

