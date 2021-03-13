lvl1 = [[],
        [],
        [],
        [],
        []]

outStr = "["
for i in range(30):
    row = []
    for i in range(200):
        row.append("  ")
    outStr+=str(row) + ",\n"
outStr += "]"
f = open("t.lvl", "w")
f.write(outStr)