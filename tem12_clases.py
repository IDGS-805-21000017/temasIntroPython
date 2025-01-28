class OperasBass:
    #Propiedades
    __num1 = 0
    __num2 = 0
    res = 0

    #Contructor
    def __init__(self, a:int, b:int):
        self.num1 = a
        self.num2 = b

    #Metodos
    def suma(self):
        self.res = self.num1+self.num2
        print(f"La suma es {self.res}")
    
    def resta(self):
        self.res = self.num1-self.num2
        print(f"La resta es {self.res}")
    
    def division(self):
        try:
            self.res = self.num1 / self.num2
        except Error:
            print()
    
def main():
    obj = OperasBass(2,4)
    obj.suma()
    obj.resta()
    print(obj.num1)
    
if __name__ == "__main__":
    main()