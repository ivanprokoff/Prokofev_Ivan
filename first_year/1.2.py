a = int(input())
mn = 30000
mx = 0
c = 0
dl = 0
while a!=0:
    dl = dl+1
    if a%2!=2 and a%3==0:
        c = c+1
        a = int(input())
else:
    c = c
print(c)
print(dl)
