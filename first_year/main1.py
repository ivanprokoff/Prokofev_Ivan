f = open('plant.txt', encoding="utf-8", mode='rt')
f1 = open('double.txt', 'w', encoding="utf-8")
res = []
r2 = []
res_str = ''
symbols = {}
r = f.readline()
r1 = list(r)
for i in r1:
    if i not in r2:
        r2.append(i)
for i in r2:
    res.append((r1.count(i), i))
for i in res:
    if i[0] == 2:
        res_str = res_str + i[1]
print(res_str)
print(res_str, file=f1)
f.close()
f1.close()
