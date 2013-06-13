# -*- coding: utf-8 -*-
import sys
from PySide import QtGui

from game import Rules

rules = Rules()
board = rules.board
player = rules.player
computer = rules.computer



class Interface(QtGui.QWidget):

        
    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Tic Tac Toe')
        #self.setWindowIcon(QtGui.QIcon('icon.png'))  
        self.show()
        
    def paintEvent(self,event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setWidth(5)
        painter.setPen(pen)
        
        #
        # On laisse une marge de 20% de chaque coté
        #  Ce qui laisse 60% à divisé en trois, soit 20%
        #
        
        step_x = self.width() / 5
        step_y = self.height() / 5
        
        #
        # dessiner les quatres lines
        #
        painter.drawLine(2*step_x, 1*step_y, 2*step_x, 4*step_y)
        painter.drawLine(3*step_x, 1*step_y, 3*step_x, 4*step_y)
        painter.drawLine(1*step_x, 2*step_y, 4*step_x, 2*step_y)
        painter.drawLine(1*step_x, 3*step_y, 4*step_x, 3*step_y)
    
        #
        # dessiner les "moves"
        #
        sub_step_x = (4 * step_x)/5 
        sub_step_y = (4 * step_y)/5 
        
        for move in board.moves:
            if move.player == computer:
                painter.drawEllipse( move.x * step_x + sub_step_x, # position x
                                     move.y * step_y + sub_step_y, # position y
                                     step_x - 2 * sub_step_x,      # width
                                     step_y - 2 * sub_step_y )     # height
            else:
                painter.drawLine(move.x * step_x + sub_step_x,
                                 move.y * step_y + sub_step_y,
                                 (move.x+1) * step_x - sub_step_x,
                                 (move.y+1) * step_y - sub_step_y)
                
                painter.drawLine(move.x * step_x + sub_step_x,
                                 (move.y+1) * step_y - sub_step_y,
                                 (move.x+1) * step_x - sub_step_x,
                                 move.y * step_y + sub_step_y)


    def mouseReleaseEvent(self,event):
                
        print "mouseReleaseEvent(%d,%d)" % ( event.x(), event.y())

        # nos lignes de séparations...
        step_x = self.width() / 5
        step_y = self.height() / 5
        
        # éliminer les clicks en dehors du jeu
        if event.x() <= step_x:
            print "x too small"
            event.accept()
            return
         
        if event.x() >= 4*step_x:
            print "x too big"
            event.accept()
            return
         
        if event.y() <= step_y:
            print "y too small"
            event.accept()
            return
         
        if event.y() >= 4*step_y:
            print "y too big"
            event.accept()
            return
        
        # convertir les coordonnées de la souris en coordonnées du jeux
        x = event.x() / step_x
        y = event.y() / step_y
        
        msg = rules.click(x, y)
        event.accept()
        self.repaint()
        
        if msg:
            QtGui.QMessageBox.question(self, 'Tic Tac Toe', msg, QtGui.QMessageBox.Yes)
         

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    wid = Interface()
    wid.initUI()
    wid.resize(500, 500)
    wid.setWindowTitle('Tic Tac Toe')
    wid.show()
    
    sys.exit(app.exec_())