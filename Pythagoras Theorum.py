import math
a = 5
b = 0
c = 13

if c == 0:
    ans = math.sqrt(a ** 2 + b ** 2)
elif b == 0:
    ans = math.sqrt(c ** 2 - a ** 2)
else:
    raise "Bad arguments"

print(ans)
