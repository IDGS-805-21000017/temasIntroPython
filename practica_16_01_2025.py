from math import sqrt, pow

def calcularDistancia(x1: int, y1: int, x2: int, y2: int):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def datos():
    x1 = int(input("Dame la primera X1: "))
    y1 = int(input("Dame la primera Y1: "))
    x2 = int(input("Dame la primera X2: "))
    y2 = int(input("Dame la primera Y2: "))
    print(f"[{x1}, {y1}], [{x2}, {y2}]")
    return calcularDistancia(x1, y1, x2, y2)

if __name__ == "__main__":
    print(datos())