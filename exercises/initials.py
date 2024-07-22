letterN="N"
letterH="H"
letterI="I"
space=" "
height=5

#letter N
for row in range(height):
        lineN = [' '] * height
        lineN[0] = 'N'
        lineN[row] = 'N'
        lineN[-1] = 'N'
        print(''.join(lineN))
print()

#letter H
for row in range(height):
  lineH = [' '] * height
  lineH[0] = 'H'  
  lineH[-1] = 'H'
  if row == height // 2:
    for i in range(height):
      lineH[i] = 'H'
  print(''.join(lineH))
print() 

#letter I
for row in range(height):
  print(" ","I")
print()