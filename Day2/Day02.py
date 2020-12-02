
with open('Day02.input', 'r') as f:
    data = f.read().splitlines()

# with open('Day02.example', 'r') as f:
#     data = f.read().splitlines()


#------
# Part One
#-------
TotalNumber = 0
for line in data:
    password = line.split(': ')[-1]
    rule = line.split(': ')[0]
    letter = rule.split(' ')[-1]
    nMin = rule.split(' ')[0].split('-')[0]
    nMin = int(nMin)
    nMax = rule.split(' ')[0].split('-')[-1]
    nMax = int(nMax)
    
    count = 0
    for char in password:
        if char == letter:
            count += 1
    
    if count >= nMin:
        if count <= nMax:
            TotalNumber += 1

print(TotalNumber)


#-----
# Part Two
#-----

TotalNumber = 0
for line in data:
    password = line.split(': ')[-1]
    rule = line.split(': ')[0]
    letter = rule.split(' ')[-1]
    pos1 = rule.split(' ')[0].split('-')[0]
    pos1 = int(pos1) - 1 # I'm working in python
    pos2 = rule.split(' ')[0].split('-')[-1]
    pos2 = int(pos2) - 1 # I'm working in python
    
    flag = False
    
    if password[pos1] == letter:
        flag = True
    if password[pos2] == letter:
        if flag:  #There's got to be a better way to xor
            flag = False
        else:
            flag = True
        
    
    if flag:
        TotalNumber += 1
        
print(TotalNumber)
    