class Carro():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano

    def descrição(self):
        print(f"O carro {self.modelo.title()} é da marca {self.montadora.upper()}, ano {self.ano}.")


class Carro_Eletrico(Carro):
    def __init__(self, montadora, modelo, ano):
        super().__init__(montadora, modelo, ano)
        self.bateria = Bateria()

    def capacidade_desclocamento(self):
        print(f"O carro tem uma capacidade de deslocamento de {self.bateria.pot_bateria * 4}Km")

class Bateria():
    def __init__(self, pot_bateria=70):
        self.pot_bateria = pot_bateria

    def bateria_melhoria(self):
        if self.pot_bateria != 85:
            self.pot_bateria = 85

    def bateria_descricao(self):
        print(f"Este carro tem uma bateria com capacidade de {self.pot_bateria}KWh")
