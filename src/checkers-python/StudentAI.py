from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
        self.f = open("debug.txt", "w")
    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1
        moves = self.board.get_all_possible_moves(self.color)
        self.f.write("Curr Moves: " + str(moves) + '\n')
        move = self.minimax(moves)
        self.f.write("Chosen Move: " + str(move) + '\n')
        # index = randint(0,len(moves)-1)
        # inner_index =  randint(0,len(moves[index])-1)
        # move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move

    def minimax(self, moves):
    	dic_l1 = dict()
    	for peice in range(len(moves)):
    		for i in range(len(moves[peice])):
    			move = moves[peice][i]
    			self.board.make_move(move,self.color)
    			l2_moves = self.board.get_all_possible_moves(self.opponent[self.color])
    			# print("Opponent Moves: \n peice: ",peice, "\n dir: ",i, "\nMoves\n", l2_moves)
    			dic_l2 = dict()
    			for opp_peice in range(len(l2_moves)):
    				for j in range(len(l2_moves[opp_peice])):
    					move = l2_moves[opp_peice][j]
    					self.board.make_move(move,self.opponent[self.color])
    					
    					l3_moves = self.board.get_all_possible_moves(self.color)
    					dic_l3 = dict()
    					# print("L3 ",l3_moves)
    					for my_peice in range(len(l3_moves)):
    						for k in range(len(l3_moves[my_peice])):
    							move = l3_moves[my_peice][k]
    							self.board.make_move(move,self.color)
		    					value = -1
		    					if self.color == 1:
		    						value = self.board.black_count - self.board.white_count
		    					else:
		    						value = self.board.white_count - self.board.black_count

		    					key = str(my_peice) + ' ' + str(k)
		    					# print(key, ' ', value)
		    					dic_l3[key] = value
		    					self.board.undo()

		    			inverse = [(value, key) for key, value in dic_l3.items()]
		    			l2_value = max(inverse)[0]
		    			key = str(opp_peice) + ' ' + str(j)
		    			dic_l2[key] = l2_value
    					self.board.undo()

    			inverse = [(value, key) for key, value in dic_l2.items()]
		    	l1_value = min(inverse)[0]
    			key = str(peice) + ' ' + str(k)
    			dic_l1[key] = l1_value
    			self.board.undo()

    	inverse = [(value, key) for key, value in dic_l1.items()]
    	l0_value = max(inverse)[1]
    	# print(dic_l1)
    	# print(l0_value)
    	x,y = l0_value.split(' ')
    	return moves[int(x)][int(y)]