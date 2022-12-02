with open('input.txt') as f:
    lines = f.readlines()

max_calories = 0
curr_calories = 0

for line in lines:
  if line == '\n':
    if curr_calories > max_calories:
      max_calories = curr_calories

    curr_calories = 0
  else:
    calories = int(line.strip())
    curr_calories += calories

print(max_calories)