# read the contents of input.txt
f = open("input.txt", "r")
code = f.readlines()
print(code)
# ['int a, b, c;\n', 'float d, e;\n', 'a = b = 5;\n', 'c = 6;\n', 'if ( a > b)\n', '{\n', '    c = a - b;\n', '    e = d - 2.0;\n', '}\n', 'else\n', '{\n', '    d = e + 6.0;\n', '    b = a + c;\n', '}']
# remove the newline character from each line
code = [x.strip() for x in code]
# ['int a, b, c;', 'float d, e;', 'a = b = 5;', 'c = 6;', 'if ( a > b)', '{', '    c = a - b;', '    e = d - 2.0;', '}', 'else', '{', '    d = e + 6.0;', '    b = a + c;', '}']

# Get the list of keywords
keywords = ["abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized", "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while"];
math = ["+", "-", "*", "/", "=", "%"]
logical = ["<", ">", "<=", ">=", "==", "and", "or"]
others =[",", ";", "(", ")", "{", "}", "[", "]"]

#Making set() to add them in their own types to print output later
checkedkeywords = set()
checkedidentifiers = set()
checkedmath = set()
checkedlogical = set()
checkednumber = set()
checkedothers = set()




