import math


def init():
    a, b, c = int(input("a:\n")), int(input("b:\n")), int(input("c:\n"))
    type = False
    termRule = False
    if b - a == c - b:
        type = "linear"
        termRule = f"{type}:    {b - a}n {'-' if (b - a) > a else '' if (b -a) == a else '+'} {abs(a - (b - a)) if abs(a - (b - a)) != 0 else ''}"
    else:
        if c / b == b / a:
            type = "geometric"
            termRule = f"{type}:    {a} {b / a}^ (n-1)"
            # test  this
        else: 
            type = "quadratic"
            x = ((c - b) - (b - c))*0.5
            termRule = f"{type}:    {x}n\N{}"


# print(f"b\N{SUPERSCRIPT THREE}")

#    https://unicode.org/Public/UNIDATA/NamesList.txt

# print(f"\N{00B0}")

# LOOK THROUGH THIS THOROUGLY https://unicode-table.com/en/sets/mathematical-signs/

# https://unicode-table.com/en/207F/ superscript n
# https://unicode-table.com/en/00B2/ superscript 2 ie squared
# https://unicode-table.com/en/207B/ superscript minus
# https://unicode-table.com/en/00B9/ superscript 1 