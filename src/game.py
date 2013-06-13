# -*- coding: utf-8 -*-

class Move:
    """Cette classe représente les coups joués ou à jouer"""
    x = 0  # les valeurs valides sont 1,2,3
    y = 0  # les valeurs valides sont 1,2,3
    player = None

class Board:
    moves = []


class Player:
    def play(self,x,y):
        """reçoit la position x,y clickée par la souris du joueur
        retourne le coup du jour correspondant"""
        move = Move()
        move.x = x
        move.y = y
        move.player = self
        return move


class Computer:
    def play(self,rules):
        """reçoit l'état du jeu actuel
        décide du prochain coup à faire
        retourne le coup en question"""
        move = Move()
        move.player = self
        
        # ça c'est de l'intelligence artificiel!
        for x in range(1,4):
            for y in range(1,4):
                move.x = x
                move.y = y
                if not rules.occupied(move):
                    return move
                
        


class Rules:
    board = Board()
    player = Player()
    computer = Computer()
    
    def occupied(self, next_move):
        for move in self.board.moves:
            if move.x == next_move.x and move.y == next_move.y:
                return True
        return False

    def exequo(self):
        if len(self.board.moves) == 9 and not self.win(self.player) and not self.win(self.computer):
            return True
        return False

    def win(self,player):
        
        #
        # on va garder les explications de ce code pour un peu plus tard.
        # c'est de la paresse de ma part de ne pas trouver une façon plus simple
        #
        player_moves = set()
        for move in self.board.moves:
            if move.player == player:
                player_moves.add((move.x, move.y))

        for i in range(1,4):            
            if set([(i,1),(i,2),(i,3)]).issubset(player_moves):
                return True
            if set([(1,i),(2,i),(3,i)]).issubset(player_moves):
                return True
        if set([(1,1),(2,2),(3,3)]).issubset(player_moves):
            return True
        if set([(3,1),(2,2),(1,3)]).issubset(player_moves):
            return True
    
        return False
    
    def click(self, x, y):
        
        # on interprête le coup du joueur
        move = self.player.play(x,y)
        
        # on considère le coup du joueur seulement s'il est valide
        if self.occupied(move):
            return False
        
        # le coup est valide, ajoutons-le
        self.board.moves.append(move)
        
        if self.win(self.player):
            return "Félicitation, vous avez gagner!"
        
        if self.exequo():
            return "Exequo!"
        
        # faire jouer l'ordinateur
        move = self.computer.play(self)
        
        # le coup est automatiquement valide, ajoutons-le
        self.board.moves.append(move)

        if self.win(self.computer):
            return "L'ordinateur gagne"

        if self.exequo():
            return "Exequo!"
        
