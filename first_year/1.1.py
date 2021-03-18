a = int(input())
mn1 = 30001
mn2 = 0
mx1 = 0
mx2 = 30001
while a!=0:
    if a > mx1:
        mx2 = mx1
        mx1 = a
    elif a>mx2:
        mx2 = a
    if a < mn1:
        mn2 = mn1
        mn1 = a
    a = int(input())
print(mn1,mn2)
print(mx1,mx2)