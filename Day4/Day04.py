# with open('Day04.input', 'r') as f:
#     data = f.read().splitlines()

# with open('Day04.example', 'r') as f:
#     data = f.read().splitlines()

with open('Day04pt2_invalid.example', 'r') as f:
    data = f.read().splitlines()

"""
byr : birth year
iyr : Issue year
eyr : expiry year
hgt : height
hcl : hair color
ecl : eye color
pid : passport ID
cid : country ID

Everything but CID is required"""

validTags = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

# blank lines starts new entry
# if line == '': starts new entry

passportData = {}

# Parse Data
count = 1
passportData[1] = {}
for line in data:
    if line == '': # start new entry
        count += 1
        passportData[count] = {}
        continue
    info = line.split(' ')
    for i in info:
        tag, value = i.split(':')
        passportData[count][tag] = value
        

def validate(passport):
    if all(elem in passport.keys() for elem in validTags): # if validTags are present
        return True
    else:
        return False
    
validcount = 0
for p in passportData:
    if validate(passportData[p]):
        validcount += 1

print(validcount)
        

#-------
# Part two
#--------



def validate2(passport):
    byr = passport['byr']
    iyr = passport['iyr']
    eyr = passport['eyr']

    hgt = passport['hgt']
    num = int(hgt[0:3])
    unit = hgt[3:]

    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']

    if not(1920 <= int(byr) <= 2002) or len(byr) != 4:
        return False

    elif not(2010 <= int(iyr) <= 2020) or len(iyr) != 4:
        return False

    elif not(2020 <= int(eyr) <= 2030) or len(eyr) != 4:
        return False


    elif unit not in ['in','cm']:
        return False
    elif unit.lower() == 'in':
        if not(59<= num <= 76):
            return False
    elif unit.lower() == 'cm':
        if not(150<= num <= 193):
            return False

    elif hcl[0] != '#' or len(hcl) != 7:
        print('False')
        return False

    elif ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False

    elif len(pid) != 9:
        return False
    
    else:
        return True


"""
byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
"""