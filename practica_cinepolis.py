from io import open
import os

class Boleto:
    __precioBoleto: int = 12  # Precio base por boleto

    def __init__(self, nombre: str, numPersonas: int, cantidad: int, tieneTarjeta: bool):
        self.nombre = nombre
        self.numPersonas = numPersonas
        self.cantidad = cantidad
        self.tieneTarjeta = tieneTarjeta
        self.total = 0.0

    def validar_cantidad(self):
        """Valida que la cantidad de boletos sea correcta según las reglas."""
        max_boletos = self.numPersonas * 7
        if self.cantidad > max_boletos:
            print(f"No se pueden comprar más de {max_boletos} boletos (7 por persona).")
            return False
        if self.cantidad < 1:
            print("La cantidad debe ser al menos 1.")
            return False
        return True

    def ajustar_boletos(self):
        os.system("cls")
        """Corrige la cantidad o el número de personas si la validación falla."""
        while not self.validar_cantidad():
            print("""
            1. Cambiar la cantidad de personas.
            2. Cambiar la cantidad de boletos.
            """)
            opcion = input("Elige una opción (1 o 2): ")
            if opcion == "1":
                self.numPersonas = int(input("Ingrese el nuevo número de personas: "))
            elif opcion == "2":
                self.cantidad = int(input("Ingrese la nueva cantidad de boletos: "))
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def calcular_total(self) -> float:
        """Calcula el total con descuentos aplicados."""
        if self.cantidad > 5:
            self.total = self.__precioBoleto * self.cantidad * 0.85
        elif 3 <= self.cantidad <= 5:
            self.total = self.__precioBoleto * self.cantidad * 0.90
        else:
            self.total = self.__precioBoleto * self.cantidad

        if self.tieneTarjeta:
            self.total *= 0.9

        return self.total

    def __str__(self):
        return f"Boleto de {self.nombre}: {self.numPersonas} personas, {self.cantidad} boletos, total: ${self.calcular_total():.2f}"


def main():
    print("""
    El boleto cuesta $12.
    Si tienes la tarjeta CINECO se te aplicará un descuento del 10%.
    No se pueden comprar más de 7 boletos por persona.
    """)

    boletos = []

    while True:
        os.system("cls")
        nombre = input("Nombre de la persona: ")
        numPersonas = int(input("¿Cuántas personas van a comprar?: "))
        cantidad = int(input("Ingrese la cantidad de boletos: "))
        tieneTarjeta = input("¿Pagarás con tarjeta CINECO? (Si o No): ").strip().lower() == "si"

        boleto = Boleto(nombre, numPersonas, cantidad, tieneTarjeta)

        # Validamos y ajustamos si es necesario
        boleto.ajustar_boletos()

        print(boleto)  # Mostramos el resumen del boleto
        boletos.append(boleto)

        # Preguntamos si desea continuar
        continuar = input("¿Quieres agregar algo más? (Si/No): ").strip().lower()
        if continuar != "si":
            break

    # Escribimos todos los boletos en el archivo
    with open("boletos.txt", "w", encoding="utf-8") as archivo:
        for boleto in boletos:
            archivo.write(f"{boleto}\n")
    
    # Calculamos el total recaudado
    total_recaudado = sum(map(lambda boleto: boleto.calcular_total(), boletos))
    print(f"\nTotal recaudado: ${total_recaudado:.2f}")


    print("Boletos registrados exitosamente en 'boletos.txt'.")


if __name__ == "__main__":
    main()