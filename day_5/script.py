with open('input.txt') as f:
  lines = f.readlines()

stacks = {}

for i in range(1, 10):
  stacks[i] = []


new_index = 0

for i, line in enumerate(lines):
  if (line[0] == ' '):
    new_index = i+2
    break

  index = 0

  for i in range(1, 10):
    block = line[index : index+4]

    letter = block[1]

    if letter != ' ':
      stacks[i].append(letter)

    index+=4

for i in range(1, 10):
  stacks[i].reverse()

for line in lines[new_index:]:
  words = line.split(' ')
  num_move = int(words[1])
  from_crate = int(words[3])
  to_crate = int(words[5])

  moved_crates = []

  for i in range(num_move):
    moved_crates.append(stacks[from_crate].pop())

  stacks[to_crate] += moved_crates

res = []

for i in range(1, 10):
  res.append(stacks[i][-1])

print(res)

# ----------------------------------------------
# PART 2 >:(

stacks_2 = {}

for i in range(1, 10):
  stacks_2[i] = []


for i, line in enumerate(lines):
  if (line[0] == ' '):
    new_index = i+2
    break

  index = 0

  for i in range(1, 10):
    block = line[index : index+4]

    letter = block[1]

    if letter != ' ':
      stacks_2[i].append(letter)

    index+=4


for i in range(1, 10):
  stacks_2[i].reverse()


for line in lines[new_index:]:
  words = line.split(' ')
  num_move = int(words[1])
  from_crate = int(words[3])
  to_crate = int(words[5])

  old_crates = stacks_2[from_crate]
  new_crates = old_crates[:len(old_crates)-num_move]
  moved_crates = old_crates[len(old_crates)-num_move:]

  stacks_2[from_crate] = new_crates
  stacks_2[to_crate] += moved_crates

res_2 = []

for i in range(1, 10):
  res_2.append(stacks_2[i][-1])

print(res_2)