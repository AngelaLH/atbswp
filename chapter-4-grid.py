#gives index error
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
        
for x in range(len(grid)):
  print(end="")
  for y in range(len(grid)):
    print([y][x], end="")

#alternative
x = 0
y = 0
while x > len(grid):
  while y > len(grid):
    print([y][x], end="")
    y+=1
  print('\n')
  x+=1
  y=0

#superior more complicated one
  def fish():
    for line in zip(*grid):
        print(''.join(line))
