# pig the dice game

from random import randint

playercount = int(input("Please enter the number of players : "))
maxscore = 100
safescore = [0] * playercount
player = 0
score=0

while max(safescore) < maxscore:
	rolling = input(f"Player {player}: ({safescore[player]}, {score}) Rolling? (Y) ").strip().lower() in {'yes', 'y', ''}

	print((player, safescore[player], score))

	if rolling:
		rolled = randint(1, 6)
		print(f'Rolled {rolled}')
		if rolled == 1:
			print(f'  Bust! you lose {score} but still keep your previous {safescore[player]}')
			score, player = 0, (player + 1) % playercount
		else:
			score += rolled
	else:
		safescore[player] += score
		if safescore[player] >= maxscore:
			break
		print(f'  Sticking with {safescore[player]}')
		score, player = 0, (player + 1) % playercount
		
print(f'\nPlayer {player} wins with a score of {safescore[player]}')