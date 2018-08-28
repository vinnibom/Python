n = int(input('n: '))
soma = n//100 + n%100
if soma*soma==n:
    print('sim')
else:
    print('não')
