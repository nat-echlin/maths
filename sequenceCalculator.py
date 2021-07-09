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
        else: 
            type = "quadratic"
            termRule = f"{type}:    "


# print(f"b\N{SUPERSCRIPT THREE}")

#    https://unicode.org/Public/UNIDATA/NamesList.txt