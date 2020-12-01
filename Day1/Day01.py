
with open('Day01.input', 'r') as f:
    data = f.read().splitlines()

# with open('Day01.example', 'r') as f:
#     data = f.read().splitlines()
   
data = [int(i) for i in data]


#--------
# Part 1
#--------

for idx, num1 in enumerate(data):
    for jdx, num2 in enumerate(data):
        if idx == jdx:
            continue
        else:
            mysum = num1 + num2
            if mysum == 2020:
                product = num1 * num2
                print('woohoo')
                print(num1, num2)
                print(product)
        

#--------
# Part 2
#--------

for a in data:
    for b in data:
        for c in data:
            mysum = a + b + c
            if mysum == 2020:
                product = a * b * c
                print ('woohoo')
                print (a, b, c)
                print (product)
