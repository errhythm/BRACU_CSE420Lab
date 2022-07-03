f = open("input.txt", "r")
code = f.readlines()
code = [x.strip() for x in code]

n = int(code[0])
code.pop(0)

symbols = [".", ",", "-", "_", ";", ":", "!", "?", "=", "+", "*", "/", "(", ")", "{", "}", "[", "]", "#", "$", "%", "^",
           "&", "|"]


def checkValidEmail(email):
    if email.count("@") == 1 and "." in email:
        split_email = email.split("@")

        for i in symbols:
            for k in range(len(split_email)):
                if split_email[k][0].isdigit() or split_email[1][-1].isdigit():
                    return False
                if split_email[k][0] == i or split_email[k][-1] == i:
                    return False
                for j in range(len(split_email[k]) - 1):
                    if split_email[k][j] == i:
                        if split_email[k][j] == split_email[k][j + 1]:
                            return False
        symbols.remove(".")
        symbols.remove("-")
        for i in symbols:
            for k in range(len(split_email)):
                for j in range(len(split_email[k]) - 1):
                    if split_email[k][j] == i:
                        return False
                if " " in split_email[k]:
                    return False
        if split_email[1].count(".") < 1:
            return False
        return True


def checkValidDomain(domain):
    split_domain = domain.split(".")
    if "" in split_domain:
        split_domain.remove("")

    symbols.insert(0, ".")
    symbols.insert(0, "-")

    for i in symbols:
        for k in range(len(split_domain)):
            if split_domain[k][0].isdigit():
                return False
            if split_domain[k][0] == i or split_domain[k][-1] == i:
                return False
            for j in range(len(split_domain[k]) - 1):
                if split_domain[k][j] == i:
                    if split_domain[k][j] == split_domain[k][j + 1]:
                        return False
    symbols.remove(".")
    symbols.remove("-")
    for i in symbols:
        for k in range(len(split_domain)):
            for j in range(len(split_domain[k]) - 1):
                if split_domain[k][j] == i:
                    return False
            if split_domain[-1][-1].isdigit():
                return False
            if " " in split_domain[k]:
                return False
            if "://" in split_domain[k]:
                return True
    return True


for i in code:
    if checkValidEmail(i):
        print("Email,", code.index(i) + 1)
    elif checkValidDomain(i):
        print("Domain,", code.index(i) + 1)
    else:
        print("Invalid")

print(code)
