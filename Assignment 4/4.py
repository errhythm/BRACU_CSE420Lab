import re

f = open("input.txt", "r")

code = f.readlines()


method = []

mainMethod = r"public static void main(.*)"
reg = r"(public|private|default)( static)? (Boolean|char|byte|short|int|long|float|double|String|void) \w+\((.*)?\)"

for line in code:
    if re.match(reg, line) and not re.match(mainMethod, line):
        method.append(re.findall("(Boolean|char|byte|short|int|long|float|double|String|void) (\w+)\((.+)?\)", line)[0])
        print(method)
print("Methods:")
for m in method:
    print("{} ({}), return type: {}".format(m[1], m[2], m[0]))



