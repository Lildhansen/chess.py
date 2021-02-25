import pygame as pg
import time

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


class ChessPiece():
    def __init__(self,startPosition,isWhite,type):
        self.pos = startPosition
        if isWhite == True: 
            self.image = pg.image.load("chess_Pieces\\white\\" + type + ".png")   
        else:
            self.image = pg.image.load("chess_Pieces\\black\\" + type + ".png")  
    def changePos(self):
        print("pos change")
    def highlightPiece(self): #denne funktion kan ikke bruges men hvis den slettes er jeg bange for den fucker - den kan dog bruges af ekslusivt af blackPawns
        print(self.pos)
        #fjern instance af den
        #gør pladsen til 0
    def die(self):
        print("die")
    def selectPiece(self):
        print(self.pos)



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


