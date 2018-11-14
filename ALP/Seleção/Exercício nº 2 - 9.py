a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))
if a==b==c:
    print('equilátero')
else:
    if a==b or a==c or b==c:
        print('isósceles')
    else:
        print('escaleno')
