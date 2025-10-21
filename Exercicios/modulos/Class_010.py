class Restaurante():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.entregas = False
        self.clientes = 0
    
    def descrição(self):
        print(f"Restaurante: {self.nome.title()}")
        print(f"Comida: {self.tipo.title()}")

    def info_entregas(self):
        if self.entregas == True:
            print("Entregas: Realiza")
        else:
            print("Entregas: Não realiza")


class Sorveteria(Restaurante):
    def __init__(self, nome, tipo, sabores):
        super().__init__(nome, tipo)
        self.entregas = True
        self.sabores = sabores

    def lista_sobres(self):
        print(f"Sabores:", end=" ")
        for x, sabor in enumerate(self.sabores, 1):
            if x < len(self.sabores):
                print(sabor.title(), end= ", ")
            else:
                print(sabor.title(), end= ".")
        print()