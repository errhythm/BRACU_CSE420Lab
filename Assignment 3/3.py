import re

f = open("input.txt", "r")
code = f.readlines()
code = [x.strip() for x in code]
reg = []

n = code[0]
code.pop(0)

for j in range(int(n)):
    reg.append(code[j])

# remove items of reg from code array
for j in range(int(n)):
    code.remove(reg[j])

# remove the number of regex, we can get the number of regex from the len() of reg
code.pop(0)

# iterate the code array and match regex from reg array
for i in range(len(code)):
    matched = 0
    for j in range(len(reg)):
        if re.fullmatch(reg[j], code[i]):
            matched = 1
            print("YES,", j+1)
    if matched == 0:
        print("NO,", matched)