with open('input.txt') as f:
  lines = f.readlines()

total = 0

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letter_points = {}

for i, letter in enumerate(lower + upper):
  letter_points[letter] = i + 1

def find_same_letter(str1, str2):
  str1_set = set(str1)

  for letter in str2:
    if letter in str1_set:
      return letter


for line in lines:
  length = len(line.strip())
  first_half = line.strip()[:length//2]
  second_half = line.strip()[(length//2):]

  letter = find_same_letter(first_half, second_half)
  total += letter_points[letter]

print(total)

# ------------------------------------
# part 2

def find_same_letter_3(strings):
  [str1, str2, str3] = strings
  str1_set = set(str1)

  same_letters = []
  for letter in str2:
    if letter in str1_set:
      same_letters.append(letter)

  str2_filtered_set = set(same_letters)

  for letter in str3:
    if letter in str2_filtered_set:
      return letter

group_by_three = []
total = 0

for i, line in enumerate(lines):
  group_by_three.append(line.strip())

  if i % 3 == 2:
    letter = find_same_letter_3(group_by_three)
    total += letter_points[letter]
    group_by_three = []
  

print(total)