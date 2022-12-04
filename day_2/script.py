with open('input.txt') as f:
  lines = f.readlines()

WIN = 6
LOSE = 0
TIE = 3

lose_dic = {
  'X': 'B',
  'Y': 'C',
  'Z': 'A'
}

tie_dic = {
  'X': 'A',
  'Y': 'B',
  'Z': 'C'
}

win_dic = {
  'X': 'C',
  'Y': 'A',
  'Z': 'B'
}

default_points = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

total_points = 0

for line in lines: 
  [opponenet_choice, your_choice] = line.strip().split(' ') 
  
  total_points += default_points[your_choice]

  if (win_dic[your_choice] == opponenet_choice):
    total_points += WIN
  elif (lose_dic[your_choice] == opponenet_choice):
    total_points += LOSE
  else:
    total_points += TIE

print(total_points)

# ------------------------------------------
# part 2
ROCK = 1
PAPER = 2
SCISSOR = 3

opponent_win = {
  'A': SCISSOR,
  'B': ROCK,
  'C': PAPER
}

opponent_tie = {
  'A': ROCK,
  'B': PAPER,
  'C': SCISSOR
}

opponent_lose = {
  'A': PAPER,
  'B': SCISSOR,
  'C': ROCK
}

total_points = 0

for line in lines: 
  [opponenet_choice, strategy] = line.strip().split(' ')

  if strategy == 'X':
    total_points += LOSE
    total_points += opponent_win[opponenet_choice]
  elif strategy == 'Y':
    total_points += TIE
    total_points += opponent_tie[opponenet_choice]
  else :
    total_points += WIN
    total_points += opponent_lose[opponenet_choice]

print(total_points)