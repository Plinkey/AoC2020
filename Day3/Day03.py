 with open('Day03.input', 'r') as f:
    data = f.read().splitlines()

# with open('Day03.example', 'r') as f:
    # data = f.read().splitlines()


right = 1
down  = 2

treeCount = 0
xPos = 0
yPos = 0
while True:
    if data[yPos][xPos] == '#':
        treeCount += 1
    xPos = (xPos + right) % len(data[yPos])
    yPos += down
    if yPos >= len(data):
        break
    
print(treeCount)



#------
# Part two
#-------

# I did it the lazy way by modifying the variables right and down
# I know I should be calling a function....

r1d1 = 61
r3d1 = 265
r5d1 = 82
r7d1 = 70
r1d2 = 34

print(r1d1 * r3d1 * r5d1 * r7d1 * r1d2)