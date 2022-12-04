with open('input.txt') as f:
  lines = f.readlines()

  total = 0

  for line in lines:
    line = line.strip()
    [worker1, worker2] = line.split(',')

    worker1_range = worker1.split('-')
    worker2_range = worker2.split('-')

    if (int(worker1_range[0]) <= int(worker2_range[0]) and int(worker1_range[1]) >= int(worker2_range[1])):
      total += 1
    elif (int(worker1_range[0]) >= int(worker2_range[0]) and int(worker1_range[1]) <= int(worker2_range[1])):
      total += 1

print(total)