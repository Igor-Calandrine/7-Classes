"""Três restaurantes: Comece com a classe do Exercício anterior. Crie três instâncias diferentes da classe e chame describe_restaurant() para cada instância."""

class Restaurante():
    def __init__(self, nome, cozinha, bebidas, promoção, entregas):
        self.nome = nome.title()
        self.cozinha = cozinha
        self.bebidas = bebidas
        self.promoção = promoção
        self.entregas = entregas

    def descrição_restaurante(self):
        print(f"O restaurante {self.nome} serve comida {self.cozinha} e {self.bebidas}.")
        
        if self.promoção == True:
            print(f"Tem promoções em aberto, venha já conferir")
        else:
            print(f"Oferece promoções em alguns dias da semana, venha conferir os dias!")

        if self.entregas == True:
            print(f"Realiza entregas para sua maior comidade!")
        else:
            print(f"Tem uma boa recepção para sua experiência!")

        