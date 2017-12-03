s1 = 8
s2 = 16
s3 = 28

SeType = None
dif2 = 0
dif1 = 0
nsqrd = 0
difa1 = 0
difa2 = 0
ComRat = 0

# Linear Sequences
if s2 - s1 == s3 - s2:
    print("This is a LINEAR sequence.")
    SeType = "Lin"

    dif1 = s2 - s1

    if s1 - dif1 == 0:
        print(f"nth term = {dif1}n")

    elif s1 - dif1 < 0:
        dif2 = s1 - dif1
        print(f"nth term = {dif1}n{dif2}")

    else:
        dif2 = s1 - dif1
        print(f"nth term = {dif1}n+{dif2}")

# Geometric Sequences
elif s3/s2 == s2/s1:
    print("This is a GEOMETRIC sequence")
    SeType = "Geo"

    ComRat = s3/s2
    print(f"The common ratio is {ComRat}")


# Quadratic Sequences
elif s2 - s1 != s3 - s2:
    print("This is a QUADRATIC sequence.")
    SeType = "Qua"

    nsqrd = ((s3 - s2) - (s2 - s1)) / 2
    ns1 = nsqrd * 1 ** 2
    ns2 = nsqrd * 2 ** 2
    ns3 = nsqrd * 3 ** 2
    difa1 = (s2 - ns2) - (s1 - ns1)
    difa2 = (s1 - ns1) - difa1

    poscheck1 = difa1 >= 0
    poscheck2 = difa2 >= 0

    if poscheck1:
        if poscheck2:
            print(f"nth term = {str(nsqrd)}n²+{str(difa1)}n+{str(difa2)}")
        else:
            print(f"nth term = {nsqrd}n²+{difa1}n{difa2}")
    else:
        if poscheck2:
            print(f"nth term = -{nsqrd}n²{difa1}n+{difa2}")
        else:
            print(f"nth term = -{nsqrd}n²{difa1}n{difa2}")

TermN1 = int(input("Input term n"))

if SeType == "Lin":
    SeqN = dif1 * TermN1 + dif2
    print(SeqN)

elif SeType == "Qua":
    SeqN = nsqrd * TermN1 ** 2 + difa1 * TermN1 + difa2
    print(SeqN)

elif SeType == "Geo":
    SeqN = s1 * ComRat ** (TermN1 - 1)
    print(SeqN)

print("Hello World")
