import math

def linearRule(a, b, typing=True):
    return f"{'linear:    ' if typing else ''}{b - a}n {'-' if (b - a) > a else '' if (b -a) == a else '+'} {abs(a - (b - a)) if abs(a - (b - a)) != 0 else ''}"

def init():
    a, b, c = int(input("a:\n")), int(input("b:\n")), int(input("c:\n"))
    type = False
    termRule = False
    if b - a == c - b:
        type = "linear"       
        return linearRule(a, b)
    else:
        if c / b == b / a:
            type = "geometric"
            termRule = f"{type}:    {a} * {round(b / a)}ⁿ⁻¹"
            return termRule
        else: 
            type = "quadratic"
            x = round(((c - b) - (b - c))*0.5)
            termRule = f"{type}:    {x}n² {linearRule(a - x, b = b - x * 4, typing=False)}"
            return termRule


# print(f"b\N{SUPERSCRIPT THREE}")

print(init())

#    https://unicode.org/Public/UNIDATA/NamesList.txt

# print(f"b\N{Superscript Latin Small Letter N}")
# print('3ⁿ')

# LOOK THROUGH THIS THOROUGLY https://unicode-table.com/en/sets/mathematical-signs/

# https://unicode-table.com/en/207F/ superscript n
# https://unicode-table.com/en/00B2/ superscript 2 ie squared
# https://unicode-table.com/en/207B/ superscript minus
# https://unicode-table.com/en/00B9/ superscript 1 