x = 0

while x <= 10:
    print(x)
    x+=1
x=1

num1 = int(input("Dame un numero: "))

if x != 0:
    while x <= 10:
        total = num1*x
        print(f'{num1} x {x} = {total}')
        x+=1
else:
    print("No debe ser 0")