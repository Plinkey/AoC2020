debug = False


# %% Load Inputs
if debug:
    with open('Day08.example', 'r') as f:
        data = f.read().splitlines()
else:    
    with open('Day08.input', 'r') as f:
        data = f.read().splitlines()
        
# %% 
# Initialize stuff
seenLines = []
accumulator = 0

curLine = 0


# %%
# Do Stuff with input string.
def process(inline):
    instr = data[inline]
    command, num = instr.split(' ')
    return command, int(num)

# %%
# ACC command
def acc(lineNo):
    command, num = process(lineNo)
    seenLines.append(lineNo)
    global accumulator
    accumulator += num
    print('On Line: {}, the accumulator is {}'.format(lineNo, accumulator))
    return lineNo+1

# %%
# NOP command
def nop(lineNo):
    command, num = process(lineNo)
    if command != 'nop':
        print('STUPID! This is not the acc command. Line {}'.format(lineNo))
    seenLines.append(lineNo)
    return lineNo+1

# %%
# JMP command
def jmp(lineNo):
    command, num = process(lineNo)
    seenLines.append(lineNo)
    return lineNo + num

# %%
def runLine(lineNo):
    if 'nop' in data[lineNo]:
        print('nop lineNo: {}'.format(lineNo))
        nextLine = nop(lineNo)
    elif 'jmp' in data[lineNo]:
        nextLine = jmp(lineNo)
    elif 'acc' in data[lineNo]:
        nextLine = acc(lineNo)
    return nextLine

while True:
    if curLine in seenLines:
        print('The answer to part one is: {}'.format(accumulator))
        break
    curLine = runLine(curLine)
    
"""# %%
# Part Two


#%%
def resetData():
    global debug
    if debug:
        with open('Day08.example', 'r') as f:
            data = f.read().splitlines()
    else:    
        with open('Day08.input', 'r') as f:
            data = f.read().splitlines()
    return data

def changeThisLine(lineNo):
    cmd, num = process(lineNo)
    if cmd == 'nop':
        new = 'jmp'
    else:
        new = 'nop'
    return '{} {}'.format(new, num)

# %%
def part2Trial(changeLine):
    curLine = 0
    global seenLines
    global data
    seenLines = []
    print('line was: {}'.format(data[changeLine]))
    data[changeLine] = changeThisLine(changeLine)
    print('line is now: {}'.format(data[changeLine]))
    
    flag = True
    while True:
        print(seenLines)
        if curLine in seenLines:
            print('Infinite Loop. changeLine: {}'.format(changeLine))
            return flag
        elif curLine == len(data):
            print('The answer to part two is: {}'.format(accumulator))
            flag = False
            return flag
        print('the current line(error): {}'.format(curLine))
        curLine = runLine(curLine)
        



changeLine = 0
while True:
    print('The changeLine is now: {}'.format(changeLine))
    if 'jmp' in data[changeLine] or 'nop' in data[changeLine]:
        flag = part2Trial(changeLine)
        if flag:
            changeLine += 1
            data = resetData()
        else:
            break
    else:
        changeLine += 1
"""
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        