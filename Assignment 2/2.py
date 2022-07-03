f = open("input.txt", "r")
code = f.readlines()
code = [x.strip() for x in code]

n = int(code[0])
print(n)
code.pop(0)

symbols = [".", ",", "-", "_", ";", ":", "!", "?", "=", "+", "*", "/", "(", ")", "{", "}", "[", "]", "#", "$", "%", "^", "&", "|"]

def checkValidEmail(email):
    if email.count("@") == 1 and "." in email:
        if email[0].isdigit() or email[-1].isdigit():
            return False
        else:
            split_email = email.split("@")
            for i in symbols:
                if split_email[0][0] == i:
                    return False
                if split_email[0][-1] == i:
                    return False
                for j in range(len(split_email[0]) - 1):
                    if split_email[0][j] == i:
                        if split_email[0][j] == split_email[0][j + 1]:
                            return False
            symbols.pop(0)
            for i in symbols:
                for j in range(len(split_email[0]) - 1):
                    if split_email[0][j] == i:
                        return False
            return True




for i in code:
    if checkValidEmail(i):
        print(i, code.index(i)+1)
    else:
        print("Invalid")

print(code)
