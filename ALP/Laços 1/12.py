ac=0
soma=0
while True:
    n=float(input('n: '))
    ac=ac+1
    soma=soma+n
    media=soma/ac
    if n==0: break
print(media)
