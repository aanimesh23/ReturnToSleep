import os

win = 0
lost = 0
tie = 0
for i in range(100):
	print("Game Number: ", i+1)
	X = os.popen("python3 AI_Runner.py 7 7 2 l Sample_AIs/Random_AI/main.py  ../src/checkers-python/main.py").read()
	X = X.split('\n')
	game_res = X[-2].strip()
	
	if game_res == 'player 2 wins':
		win += 1
	elif game_res == 'player 1 wins':
		lost += 1
	else:
		tie += 1

print("Wins: {} \t Lost: {} \t Tie: {}".format(win, lost, tie))