# read the contents of input.txt
f = open("input.txt", "r")
code = f.readlines()
# remove the newline character from each line
code = [x.strip() for x in code]
# Get the list of keywords
keywords = ["abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized",
            "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte",
            "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch",
            "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally",
            "long", "strictfp", "volatile", "const", "float", "native", "super", "while"]
math = ["+", "-", "*", "/", "=", "%"]
logical = ["<", ">", "<=", ">=", "==", "and", "or"]
others = [",", ";", "(", ")", "{", "}", "[", "]"]

# Making set() to add them in their own types to print output later
checkedkeywords = set()
checkedidentifiers = set()
checkedmath = set()
checkedlogical = set()
checkednumber = set()
checkedothers = set()

def lexical_analyzer(code, check, store):
    for i in check: #taking all the values of the check list
        if i in code:
            store.add(i)
            code = code.replace(i, "")
    return code

# Making an array which I will use later for identifiers and number
code_array = []

for i in code:
    if i.startswith("//"):
        code = code.replace(i, "")
    else:
        code = lexical_analyzer(i, keywords, checkedkeywords)
        code = lexical_analyzer(code, math, checkedmath)
        code = lexical_analyzer(code, logical, checkedlogical)
        code = lexical_analyzer(code, others, checkedothers)
    # if the code is not empty, then it is an identifier or a number.
    # So, I will add it to the code_array for later use out of this loop.
    code_arr = code.split()
    code_array.append(code_arr)

for i in code_array:
    for j in i:
        if j.isalpha():
            checkedidentifiers.add(j)
        else:
            checkednumber.add(j)


def print_output(type, set):
    print(type, end="")
    for i in sorted(set):
        print(i, end=" ")
    print("")


print_output("Keywords: ", checkedkeywords)
print_output("Identifiers: ", checkedidentifiers)
print_output("Math: ", checkedmath)
print_output("Logical: ", checkedlogical)
print_output("Number: ", checkednumber)
print_output("Others: ", checkedothers)
