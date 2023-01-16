import re

number = re.compile("^_?[0-9]+(\.[0-9]+)?$")

def operation(a, op, b):
    if a[0] == "_":
        a = "-" + a[1:]
    if b[0] == "_":
        b = "-" + b[1:]
    a = float(a)
    b = float(b)
    if op == "+":
        r = a + b
    if op == "-":
        r = a - b
    if op == "x":
        r = a * b
    if op == "/":
        r = a / b
    if r.is_integer():
        r = int(r)
    r = str(r)
    if r[0] == "-":
        r = "_" + r[1:]
    return r

def compute(e):
    if bool(number.search(e)):
        return e
    try:
        l = len(e)
        for i in range(l):
            if e[i] == "(":
                j = i + 1
                c = 1
                while c > 0:
                    if e[j] == "(":
                        c = c + 1
                    if e[j] == ")":
                        c = c - 1
                    j += 1
                j = j - 1
                if (i == 0 and j == l-1):
                    return compute(e[1:-1])
                elif i == 0:
                    return compute(compute(e[1:j]) + e[j+1:])
                elif j == l-1:
                    return compute(e[:i] + compute(e[i+1:-1]))
                else:
                    return compute(e[:i] + compute(e[i+1:j]) + e[j+1:])
        
        no_mult = True
        for i in range(l):
            if (e[i] == "x" or e[i] == "/"):
                no_mult = False
                break
        if no_mult:
            for i in range(l):
                if (e[i] == "+" or e[i] == "-"):
                    break
        j = 0
        k = l - 1
        for _ in range(l):
            if bool(number.search(e[j:i])):
                break
            else:
                j = j + 1
        for _ in range(l):
            if bool(number.search(e[i+1:k+1])):
                break
            else:
                k = k - 1
        if (j == 0 and k == l-1):
            return compute(operation(e[:i], e[i], e[i+1:]))
        elif j == 0:
            return compute(operation(e[:i], e[i], e[i+1:k+1]) + e[k+1:])
        elif k == l-1:
            return compute(e[:j] + operation(e[j:i], e[i], e[i+1:]))
        else:
            return compute(e[:j] + operation(e[j:i], e[i], e[i+1:k+1]) + e[k+1:])

    except:
        return "Error"