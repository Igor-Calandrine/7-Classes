"""
Trabalhando com classes e instâncias
    Podemos usar classes para representar muitas situações do mundo real. Depois de escrever uma classe, você gastará a maior parte de seu tempo trabalhando com unstâncias dessa classe. Uma das primeiras tarefas que você vai querer fazer é modificar os atributos associados a uma instância em particular. Podemos modificar os atributos de uma instância diretamente, ou escrever métodos que atualizaem os atributos de formas específicas. Usaremos a classe abaixo para trabalharmos nesse capítulo."""

print("Exemplo 1")
class Carro_1():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano

    def descrição(self):
        descrição_nome = f"O carro {self.modelo} é da marca {self.montadora}, ano {self.ano}."
        return descrição_nome
    
meu_carro_novo = Carro_1("Cintroen", "C3", 2024)

print(meu_carro_novo.descrição())

"""
Definindo um valor default para um atributo
    Todo atributo de uma classe precisa de um valor inicial, mesmo que esse valor seja 0 ou uma string vazia. Em alguns casos quando definimos um valor default, faz sentido especificar esse valor inicial no corpo do método __init__(), se isso for feito para um atrbuto, você não precisará incluir um parâmetro para ele."""

print("\nExemplo 2")
class Carro_2():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.km = 0 #Observe que não é necessário colocar nos parâmetros

    def descrição(self):
        print(f"O carro {self.modelo} é da marca {self.montadora}, ano {self.ano}.")
        
    def leitura_km(self):
        print(f"Esse carro já percorreu {self.km} Km.")
        
meu_carro_novo = Carro_2("Cintroen", "C3", 2024) #Observe que não foi dada informações para self.km

meu_carro_novo.descrição()
meu_carro_novo.leitura_km()

"""
Modificando valores de atributos
    Você pode alterar o valor de um atributo de três maneiras: podemos modificar o valor diretamente por meio de uma instância, definir o valor com um método ou incrementá-lo.
    
    *Modificando o valore de um atributo diretamente
    A maneira mais simples de modificar o valor de um atributo é acessá-lo diretamente por meio de uma instância. Observe no exemplo abaixo que para acessar o atributo não é necessário incluir o #self em sua sintaxe."""

print("\nExemplo 3")
meu_carro_novo.km = 15 
meu_carro_novo.descrição()
meu_carro_novo.leitura_km()

"""
    *Modificando o valor de um atributo com um método
    Pode ser conveniente ter métodos que atualizem determinados atributos para você. Em vez de acessar o atributo de modo direto, passe o novo valor para um étodo que trate a atualização internamente."""

print("\nExemplo 4")
class Carro_4():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    def descrição(self):
        print(f"O carro {self.modelo} é da marca {self.montadora}, ano {self.ano}.")
        
    def leitura_km(self):
        print(f"Esse carro já percorreu {self.km} Km.")

    def atual_km(self, km):
        if km <= self.km:
            print("Km inferior a atual, por favor corrija o número.")
        else:
            self.km = km
        
meu_carro_novo = Carro_4("Cintroen", "C3", 2024)
meu_carro_novo.atual_km(45)

meu_carro_novo.descrição()
meu_carro_novo.leitura_km()

"""
    *Incrementando o valor de um atributo com um método
    Para incrementar o valor de um atributo em determinanada quantidade, você pode criar um método que nos permite passar essa quantidade incremental e somar esse valor ao valor de leitura do hodômetro, ou utilizar-se de um acesso direto do atributo. Abaixo utilizaremos as duas formas como exemplo."""

print("\nExemplo 5")
class Carro_5():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    def descrição(self):
        print(f"O carro {self.modelo} é da marca {self.montadora}, ano {self.ano}.")
        
    def leitura_km(self):
        print(f"Esse carro já percorreu {self.km} Km.")

    def atual_km(self, km):
        if km <= self.km:
            print("Km inferior a atual, por favor corrija o número.")
        else:
            self.km = km

    def percorrido_km(self, km):
        if km < 0:
            print("Km inferior a zero, por favor corrija o número.")
        else:
            self.km += km


meu_carro_novo = Carro_5("Cintroen", "C3", 2024)
meu_carro_novo.atual_km(45)
meu_carro_novo.percorrido_km(100)

meu_carro_novo.descrição()
meu_carro_novo.leitura_km()

meu_carro_novo.km += 200

meu_carro_novo.descrição()
meu_carro_novo.leitura_km()