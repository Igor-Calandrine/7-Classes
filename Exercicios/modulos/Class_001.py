"""Restaurante: Crie uma classe chamada Restaurant. O método __init__() de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type. Crie  um  método  chamado  describe_restaurant()  que  mostre  essas duas informações, e um método de nome  open_restaurant() que exiba uma mensagem informando que o restaurante está aberto. Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois
atributos individualmente e, em seguida, chame os dois métodos.
"""

class Restaurante():
    def __init__(self, nome, cozinha):
        self.nome = nome
        self.cozinha = cozinha

    def descrição_restaurante(self):
        print(f"O restaurante {self.nome} serve comida {self.cozinha}.")