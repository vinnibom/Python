n=int(input('n: '))
ac=0
for i in range(n):
    lido=int(input('lido: '))
    if lido%2==0:
        ac=ac+lido
print(ac)
