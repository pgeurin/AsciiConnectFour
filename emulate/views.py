# AsciiConnectFour
# Philip Geurin
# This is a module that simulates Connect Four and
# creates an AI to play it.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


import random
import math
import random

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [ [' ']*width for row in range(height) ]
        # do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        
        for col in range( self.width ):
            s += ' ' + str(col%10)

        s += '\n'
        return s       # the board is complete, return it

    def htmlSelf(self):
        """ this method returns a string representation
            for an object of type Board as an overt html string.
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s       # the board is complete, return it

    def set_board( self, LoS ):
        """ sets the board to the characters in the
            list of strings named LoS
        """
        for row in range( self.height ):
            for col in range( self.width ):
                self.data[row][col] = LoS[row][col]
                

    def setBoard( self, moves, show=False ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print self


    def set( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print self

    def clear( self ):
        """ the software version of the little
            blue slider that releases all of the checkers!
        """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def addMove( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        row = self.height - 1
        while row >= 0:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            row -= 1
        
    def addMove2( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def delMove( self, col ):
        """ removes the checker from column col """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return
        
    def allowsMove( self, col ):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '

    def isFull( self ):
        """ returns True if the board is completely full """
        for col in range( self.width ):
            if self.allowsMove( col ):
                return False
        return True

    def gameOver( self ):
        """ returns True if the game is over... """
        if self.isFull() or self.winsFor('X') or self.winsFor('O'):
            return True
        return False

    def isOX( self, row, col, ox ):
        """ checks if the spot at row, col is legal and ox """
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.data[row][col] == ox:
                    return True
        return False

    def winsFor( self, ox ):
        """ checks if the board self is a win for ox """
        for row in range( self.height ):
            for col in range( self.width ):
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col, ox ) and \
                   self.isOX( row+2, col, ox ) and \
                   self.isOX( row+3, col, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row, col+1, ox ) and \
                   self.isOX( row, col+2, ox ) and \
                   self.isOX( row, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col+1, ox ) and \
                   self.isOX( row+2, col+2, ox ) and \
                   self.isOX( row+3, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col-1, ox ) and \
                   self.isOX( row+2, col-2, ox ) and \
                   self.isOX( row+3, col-3, ox ):
                    return True
        return False

    def hostGame( self ):
        """ hosts a game of Connect Four """

        nextCheckerToMove = 'X'
        
        while True:
            # print the board
            print self

            # get the next move from the human player...
            col = -1
            while not self.allowsMove( col ):
                col = input('Type a number to play in that column:')
            self.addMove( col, nextCheckerToMove )

            # check if the game is over
            if self.winsFor( nextCheckerToMove ):
                print self
                print '\n' + nextCheckerToMove + ' wins! Congratulations!\n\n'
                break
            if self.isFull():
                print self
                print '\nThe game is a draw.\n\n'
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'

        print 'Come back soon 4 more!'

    def playGame(self, px, po):
        """ hosts a game of Connect Four. Handles the case in which
either px or po is the string 'human' instead of an object of type
Player. In this 'human' case, the playGame method should simply puase
and ask the user to input the next column to move for that player"""

        nextCheckerToMove = 'X'
        turn=-1
        player=[px,po]
        while True:
            turn=turn+1
            # print the board
            print self
            
            if player[turn%2]=='human': # get the next move from the player if HUMAN...
                col = -1
                while not self.allowsMove( col ):
                    col = input('Type a number to move:')
                self.addMove( col, nextCheckerToMove )

            else:
                print "Thinking..."
                print
                self.addMove(player[turn%2].nextMove(b),player[turn%2].ox)
                
            # check if the game is over
            if self.winsFor( nextCheckerToMove ):
                print self
                print '\n' + nextCheckerToMove + ' wins! Congratulations!\n\n'
                break
            if self.isFull():
                print self
                print '\nThe game is a draw.\n\n'
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'

        print 'Come back soon 4 more!'

class  Player:
    """
    An AI for connect four that will output a move given a board state.
"""
    def __init__(self, ox, tbt, ply):
        """ the constructor for objects of type Player """
        self.ox  =  ox
        self.tbt =  tbt
        self.ply =  ply

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Player
        """
        
    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        """returns the other kind of checker or playing piece"""
        if self.ox=='X':
            return 'O'
        elif self.ox=='O':
            return 'X'

    def scoreBoard(self, b):
        """return a single float value representing the score of the
input b, which you may assume will be an object of type Board."""
        if b.winsFor(self.ox)==True:
            return 100.0
        elif b.winsFor(self.oppCh())==True:
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self, scores):
        """takes in scores, which will be a nonempty list of
floating-point numbers. If there is only one highest score in that
scores list, this method will return its COLUMN number"""
        scores=findMaxScores(scores)
        if self.tbt=='LEFT':
            return min(scores)
        elif self.tbt=='RIGHT':
            return max(scores)
        elif self.tbt=='RANDOM':
            return random.choice(scores)
        else:
            print 'not a possible choice /n use only "RIGHT", LEFT, OR "RANDOM" /n choosing random as defalt'
            return random.choice(scores)

    def scoresFor(self, b):
        scores=[50]*b.width
        for col in range(b.width):
            if b.allowsMove(col)==False:
                scores[col]=-2.0
            elif b.winsFor(self.ox)==True: #is this line necessary? especially if the previous line 
                scores[col]=[100]
            elif b.winsFor(self.oppCh())==True:
                scores[col]=[0.0]
            elif self.ply==0:
                scores[col]=50 #this would be the 'evaluation moment'
            elif 0<scores[col]<100:
                b.addMove(col,self.ox)
                if b.winsFor(self.ox)==True:
                    scores[col]=100
                else:
                    scores[col]=min(myScore(Player(self.oppCh(), self.tbt ,self.ply-1).scoresFor(b)))
                b.delMove(col)
        return scores

    def nextMove(self, b):
        """takes in b, an object of type Board and returns an
integer -- namely, the column number that the calling object
(of class Player) chooses to move to"""
        scores=self.scoresFor(b)
        #b.addMove(self.tiebreakMove(scores),self.ox)
        return self.tiebreakMove(scores)
        

def findMaxScores(scores):
    """takes the list 'scores' and outputs a list of columns which
contain all maximum 'scores' elements"""
    big=scores[0]
    s=[]
    for col in range(len(scores)):
        if big<scores[col]:
            s=[col]
            big=scores[col]
        elif big==scores[col]:
            s=s+[col]
    return s

def myScore(scores):
    for col in range(len(scores)):
        if 0.0<=scores[col]<=100.0:
            scores[col]=100-scores[col]
        else:
            scores[col]=[]
    return scores

print "Welcome to Ascii Connect Four"
print "You are about to play an AI named Ascii."
print "Ascii calculates the next three moves into the future."
print "Type a number to put your piece in that column."
print "You move first. You are 'X'. Ascii is 'O'. "
po = Player('O', 'RANDOM', 3)
b = Board(7,6)
#THIS LINE WAS REOMVED SIMPLY TO REMOVE THE INPUT() ERROR FROM PLAYGAME() WITHIN THE SSCRIPT
#b.playGame('human', po)

from django.template import RequestContext, loader

def index(request):
	#take in the entry
	#if ('q' in request.GET) and request.GET['q'].strip():
    if ('q' in request.GET) and ('b' in request.GET) and ('nextPlay' in request.GET):
                #LATER: check to make sure nextPlay is a integer between 0 and 6.
        #build the board
        q = request.GET['q']
        nextPlay = request.GET['nextPlay']
        b = request.GET['b']
        b = Board(7,6)
        b.setBoard(q)
        #insert the players' move 
        b.addMove(int(nextPlay),'X') 
        #(they would probably like to see their move displayed before we think about it and then make our move... oh well! We'll separate them later!)
	#see if they won
        if b.winsFor('X'):
            print '\n X wins! Congratulations!\n\n'
        # check if it's a draw
        if b.isFull():
            print '\nThe game is a draw.\n\n'
        #Insert the compters' move
        po = Player('O', 'RANDOM', 3)
        nextPlay = po.nextMove(b)
        b.addMove(int(nextPlay),'O')
        #see if they won
        if b.winsFor('O'):
            print '\n O wins! Too Bad!\n\n'
        #see if it's a draw
        if b.isFull():
            print '\nThe game is a draw.\n\n'
    #draw the new board, it's their move!
    #q=q+str(nextPlay)
    else:
        b="try smeting"
        q="write sommething"
        nextPlay="writesomething"
    template = loader.get_template('emulate/home.html')
    context = RequestContext(request, {
        'b': b,
        #'b': b.htmlSelf(),
        'nextPlay': nextPlay, #I need to access poem in there! will this do it?
        'q': q, 
        })
    return HttpResponse(template.render(context)) 



