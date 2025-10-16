class Restaurante():
    def __init__(self, nome, cozinha):
        self.nome = nome
        self.cozinha = cozinha
        self.qnt_servidos = 0
        self.qnt = 0
        self.horas = 0
        self.minu = 0


    def descrição_restaurante(self):
        print(f"O restaurante {self.nome} serve comida {self.cozinha}.")
    
    def total_qnt_servidos(self):
        print("\n\tRegisto da quantidade de clientes servidos - Japa Loko")
        print(f"Clientes servidos: {self.qnt_servidos}")
        print(f"Última atualização: {self.horas}hr e {self.minu}min")
        print("-" * 50)
        print("Atualização de clientes servidos")

        while True:
            qnt = int(input("Digite a quantidade de clientes servidos depois da última atualização.\n\t"))
            if qnt >= 0:
                self.qnt = qnt
                self.qnt_servidos = self.qnt_servidos + self.qnt
                break
            else:
                print("Quantidade de clientes impossíveis, por favor digite novamente.")

        while True:
            horas = int(input("Digite a hora atual: "))
            if 0 <= horas <= 23:
                self.horas = horas
                break
            else:
                print("Hora impossível, por favor digite novamente")

        while True:        
            minu = int(input("Digite os minutos atuais: "))
            if 0 <= minu <= 59:
                self.minu = minu
                break
            else:
                print("Minuto impossível, por favor digite novamente")

        print(f"\nClientes servidos: {self.qnt_servidos} - {self.horas}hr e {self.minu}min")