# pig the dice game

import time
import random
from random import randint

# 최대 플레이어 수
max_players = 4

# 최대 점수
max_score = 100

# 컴퓨터 수
computers = 0

# 컴퓨터가 굴린 주사위 횟수
computer_roll_count = 0

# 현재 플레이중인 플레이어 번호 확인을 위한 값?
player = 0

# 현재 플레이중인 플레이어의 점수 계산하기 위한 값?
score = 0

while True:
	''' 입력받는 값이 int가 아니면 int 값을 입력 받을때까지 while문 반복 '''

	try:
		# 플레이할 플레이어 수 입력
		player_count = int(input("Please enter the number of players : "))

		# 만약 입력 받은 플레이어 수가 최대 플레이어 수 보다 크다면
		if player_count > max_players:
	
			# 최대 플레이어 수는 4명입니다. 4명으로 게임을 시작합니다.
			print('Maximum number of players is 4, Start with 4 players.')	
			player_count = max_players

		# 입력 받은 플레이어 수가 최대 플레이어 수 보다 작다면
		else:
			# 입력한 플레이어는 {n}명니, {max_players - n} 만큼의 컴퓨터를 추가한다는 문구 출력
			print(f'You inputted the {player_count} players, {max_players - player_count} computers are added.')

			# {max_players - n} 만큼의 컴퓨터 수 할당
			computers = (max_players - player_count)

			# 총 플레이어수는 max_players로 할당
			player_count = max_players
		break

	# 만약 입력 받은 값이 int(숫자)가 아니라면 숫자를 입력해달라는 문구 출력
	except ValueError:
		print('please input number, not string')

# 플레이어 수 만큼 총합 점수가 0으로 들어있는 list 생서
total_score = [0] * player_count




while max(total_score) < max_score:
	''' 플레이어중 누구든 max_score에 도달하면 while문 종료 (게임 종료) '''

	# 현재 플레이어가 컴퓨터일때
	if player >= (player_count - computers):

		# 현재 컴퓨터의 총합 점수와 주사위 굴림여부 물어보는 문구 출력
		print(f'computer {player+1}: total_score is {total_score[player]}, Rolling?')

		# 3초의 텀 생성 (컴퓨터의 고민 시간)
		time.sleep(3)

		# 컴퓨터가 처음 시작은 무조건 주사위를 굴리게 하기위한 if문
		if computer_roll_count <= 0:

			# 주사위를 굴림 여부에 yes 
			rolling = 'yes'

			# 컴퓨터가 굴린 주사위 횃수를 1번 증가
			computer_roll_count += 1

		# 컴퓨터가 한번이라도 주사위를 굴렸을때
		else:

			# 컴퓨터의 주사위 굴림 여부를 yes와 no중에 랜덤으로 선택
			rolling = random.choice(['yes', 'no'])

			# 컴퓨터의 주사위 굴림 여부가 yes이면 굴린 주사위 횃수를 1번 증가
			if rolling == 'yes':
				computer_roll_count += 1
		
		# 현재 컴퓨터의 주사위 굴림 결과 출력
		print(f'{rolling}')

		# 3초 텀 생성 (컴퓨터의 고민 시간)
		time.sleep(3)

	# 현재 플레이어가 컴퓨터가 아닐때
	else:
		# 주사위의 굴림 여부를 입력
		rolling = input(
			f"Player {player+1}: your total_score is {total_score[player]}, Rolling? (yes) or (no): "
		).strip().lower()

	# 주사위 굴림 여부를 yes 입력시
	if rolling == 'yes':

		# 주사위 굴림 (1 ~ 6중에 랜덤으로 선택됨)
		rolled = randint(1, 6)

		# 주사위 굴린 결과 출력 (랜덤으로 뽑힌 숫자 출력)
		print(f'Rolled {rolled}')

		# 만약 결과가 1이면
		if rolled == 1:

			# 결과가 1이라 다음 플레이어에거 턴이 넘어갔음을 출력
			print('Result is 1, the turn passes to the next player.')

			# 현재 플레이어의 총합 점수를 0으로 초기화
			total_score[player] = 0

			# 현재 플레이어의 score를 0으로 초기화, 
			# 현재 플레이어를 다음 플레이어 순서(값)으로 변경 만약 마지막 4번쨰 플레이어라면 1번째 플레이어 순서(값)으로 
			score, player = 0, (player + 1) % player_count

			# 컴퓨터의 주사위 굴림 횟수를 0으로 초기화
			# 컴퓨터의 턴일때 주사위 굴림 여부는 처음엔 무조건 yes여야 하기 때문에
			# 만약 컴퓨터 플레이어 다음 플레이어도 컴퓨터일때 주사위 굴림 횟수는 0이여야 하기 때문에
			computer_roll_count = 0

		# 결과가 1이 아니면
		else:

			# 현재 플레이어의 score를 현재 플레이어의 총합으로 변경 (기존에 누적된 값으로 시작하게 변경)
			score = total_score[player]

			# 현재 플레이어의 score에 주사위를 굴려서 나온 값을 더하기
			score += rolled

			# 현재 플레이어의 총합 점수에 현재 score를 입력
			total_score[player] = score

			# 만약 현재 플레이어의 총합 점수가 max_score와 같거나 크면 while문 종료 (게임 종료)
			if total_score[player] >= max_score:
				break
	
	# 주사위 굴림 여부를 no 입력시
	elif rolling == 'no':

		# 현재 플레이어의 score를 총합 스코어에 기록
		total_score[player] = score

		# 현재 플레이어의 score를 0으로 초기화
		score  = 0

		# 만약 현재 플레이어의 총합 점수가 max_score와 같거나 크면 while문 종료 (게임 종료)
		if total_score[player] >= max_score:
			break

		# 현재 플레이어의 총합 점수를 출력
		print(f'Total Score: {total_score[player]}')

		# 현재 플레이어를 다음 플레이어 순서(값)으로 변경 만약 마지막 4번쨰 플레이어라면 1번째 플레이어 순서(값)으로 
		player = (player + 1) % player_count

		# 컴퓨터의 주사위 굴림 횟수를 0으로 초기화
		# 컴퓨터의 턴일때 주사위 굴림 여부는 처음엔 무조건 yes여야 하기 때문에
		# 만약 컴퓨터 플레이어 다음 플레이어도 컴퓨터일때 주사위 굴림 횟수는 0이여야 하기 때문에
		computer_roll_count = 0

	# 만약 yes도 no도 아닌 다른값을 입력했을 경우
	else:

		# yes나 no 둘중에 하나를 입력해 달라고 출력
		print('please input (roll) or (stop)')

# 게임 종료시 몇번째 플레이어가 몇점으로 이겼는지 출력		
print(f'\nPlayer {player} wins with a score of {total_score[player]}')