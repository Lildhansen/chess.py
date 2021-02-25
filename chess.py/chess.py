
import pygame,time
import chess_module as cm
import os

print(os.getcwd())
x = []
for i in range(1000):
    x.append(i)
cm.displayBoard(x)


pygame.init()
logo = pygame.image.load("logo2.png")
pygame.display.set_icon(logo)
#window = pygame.display.set_mode((960,960)) #120 * 8 =960, so each tile is 120x120
pygame.display.set_caption("Chess")

#creating white pieces
whiteRook1 = cm.Rook(True,[1,1])
whiteRook2 = cm.Rook(True,[8,1])
whiteKnight1 = cm.Knight(True,[2,1])
whiteKnight2 = cm.Knight(True,[7,1])
whiteBishop1 = cm.Bishop(True,[3,1])
whiteBishop2 = cm.Bishop(True,[6,1])
whiteKing = cm.King(True,[5,1])
whiteQueen = cm.Queen(True,[4,1])
whitePawns = [cm.Pawn(True,[i,2]) for i in range(1,9)]

whitePieces = [whiteRook1,whiteRook2,whiteKnight1,whiteKnight2,whiteBishop1,whiteBishop2,whiteKing,whiteQueen,whitePawns]

#creating black pieces
blackRook1 = cm.Rook(False,[1,8])
blackRook2 = cm.Rook(False,[8,8])
blackKnight1 = cm.Knight(False,[2,8])
blackKnight2 = cm.Knight(False,[7,8])
blackBishop1 = cm.Bishop(False,[3,8])
blackBishop2 = cm.Bishop(False,[6,8])
blackKing = cm.King(False,[5,8])
blackQueen = cm.Queen(False,[4,8])
blackPawns = [cm.Pawn(False,[i,7]) for i in range(1,9)]

blackPieces = [blackRook1,blackRook2,blackKnight1,blackKnight2,blackBishop1,blackBishop2,blackKing,blackQueen,blackPawns]

def codePosToGamePos(codePos): #takes list as parameter
    gamePos = codePos.copy()
    return [(i-1)*120 for i in gamePos]

def gamePosToCodePos(gamePos):
    codePos = list(gamePos)
    countX = 1
    countY = 1
    while codePos[0] > 120 or codePos[1] > 120:
        if codePos[0] > 120:
            codePos[0] -= 120
            countX += 1
        if codePos[1] > 120:
            codePos[1] -= 120
            countY += 1
    return countX,countY

def displayAllPieces(whitePieces,blackPieces):
    for piece in whitePieces:
        if type(piece) == list:
            for pawn in piece:
                cm.window.blit(pawn.image,codePosToGamePos(pawn.pos))
        else:
           cm.window.blit(piece.image,codePosToGamePos(piece.pos))
    for piece in blackPieces:
        if type(piece) == list:
            for pawn in piece:
                cm.window.blit(pawn.image,codePosToGamePos(pawn.pos))
        else:
           cm.window.blit(piece.image,codePosToGamePos(piece.pos))

def activatePieceBasedOnPosition(position):
    x,y = gamePosToCodePos(position)
    for whitePiece in whitePieces:
        if type(whitePiece) == list:
            for pawn in whitePiece:
                if x == pawn.pos[0] and y == pawn.pos[1]:
                    pawn.selectPiece()
        else:
            if x == whitePiece.pos[0] and y == whitePiece.pos[1]:
                whitePiece.selectPiece() 
    for blackPiece in blackPieces:
        if type(blackPiece) == list:
            for pawn in blackPiece:
                if x == pawn.pos[0] and y == pawn.pos[1]:
                    pawn.selectPiece()
        else:
            if x == blackPiece.pos[0] and y == blackPiece.pos[1]:
                blackPiece.selectPiece() 

def isSquareEmpty(clickedPos): #return what piece it is, otherwise returns false. also un-selects the other pieces
     for whitePiece in whitePieces:
        if type(whitePiece) == list:
            for pawn in whitePiece:
                if pawn.isSelected:
                    pawn.unSelectPiece()
                if pawn.hitBox.collidepoint(clickedPos):
                    pawn.selectPiece()
        else:
            if whitePiece.isSelected:
                whitePiece.unSelectPiece()
            if whitePiece.hitBox.collidepoint(clickedPos):
                whitePiece.selectPiece() 
     for blackPiece in blackPieces:
        if type(blackPiece) == list:
            for pawn in blackPiece:
                if pawn.isSelected:
                    pawn.unSelectPiece()
                if pawn.hitBox.collidepoint(clickedPos):
                    pawn.selectPiece()
        else:
            if blackPiece.isSelected:
                blackPiece.unSelectPiece()
            if blackPiece.hitBox.collidepoint(clickedPos):
                blackPiece.selectPiece() 





cm.createBoardDisplay()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickedPos = pygame.mouse.get_pos()
            #activatePieceBasedOnPosition(clickedPos)
            isSquareEmpty(clickedPos)
        pygame.display.update()
    displayAllPieces(whitePieces,blackPieces)
pygame.quit()
