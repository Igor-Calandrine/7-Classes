"""
Herança
    Nem sempre você precisará começar do zero para escrever uma classe. Se a classe que você estiver escrevendo for uma versão especializada de outra classe já criada, a herança poderá ser usada. Quando uma classe herda de outra, ela assumirá automaticamente todos os atributos e métodos da primeira classe.
    *A classe original se chama classe-pai e a nova classe é a classe-filha.
    Vejamos o exemplo abaixo que criaremos uma classe-filha partindo da classe Carro"""

print("Exemplo 1")
class Carro(): #u
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    def descrição(self):
        print(f"O carro {self.modelo.title()} é da marca {self.montadora.upper()}, ano {self.ano}.")
        
    def leitura_km(self):
        print(f"Esse carro já percorreu {self.km} Km.")

class Carro_Eletrico(Carro): #v
    def __init__(self, montadora, modelo, ano): #w
        super().__init__(montadora, modelo, ano) #x

my_tesla = Carro_Eletrico("tesla", "modelo s", 2025)

my_tesla.descrição()

"""
    Em #u começamos com #Carros, pois quando criamos uma classe-filha, a classe-pai deve fazer parte do arquivo atual e deve aparecer antes da classe-filha no arquivo.
    Em #v definimos a classe-filha, note que o nome da classe-pai deve ser incluído entre parênteses na definição da classe-filha.
    Em #w temos o método __init__() que aceita as informações necessárias para criar uma instância da classe #Carros.
    Em #x temos função super(), que é uma função especial que ajuda Python a criar conexões entre a class-pai e a classe-filha. Essa linhas diz a Python para chamar o método __init__() da classe-pai, que da todos os atributos da classe-pai a #Carro_Eletrico.
    
Definindo atributos e métodos da classe-filha
    Depois que tiver uma classe-filha que herde de uma classe-pai, você pode adicionar qualquer atributo ou método novo necessários para diferenciar a classe-filha da classe-pai. Vejamos no exemplo abaixo."""
    
print("\nExemplo 2")
class Carro_2():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano

    def descrição(self):
        print(f"O carro {self.modelo.title()} é da marca {self.montadora.upper()}, ano {self.ano}.")

class Carro_Eletrico_2(Carro):
    def __init__(self, montadora, modelo, ano):
        super().__init__(montadora, modelo, ano)
        self.bateria_potencia = 70 #u

    def bateria_descricao(self): #v
        print(f"Este carro tem uma bateria com capacidade de {self.bateria_potencia}KWh")

my_tesla_2 = Carro_Eletrico_2("tesla", "modelo s", 2025)

my_tesla_2.descrição()
my_tesla_2.bateria_descricao()

"""
    Em #u adicionamos um novo atributo e definimos seu valor inicial, esse atributo será associado a todas as intâncias criadas a partir da classe #Carro_Eletrico_2, mas não será associado a nenhuma instâncias de Carro_2
    Em #v criamos um método que exibe informações sobre a bateria, algo que é claramente específico de um carro elétrico.
    
Sobrescrevendo métodos da classe-pai
    Qualquer método da classe-pai que não se enquadre no que você estiver tentando modelar com a classe-filha pode ser sobrescrito. Para isso, defina um étodo na classe-filha com o mesmo nome do método da classe-pai que você deseja sobrescrever. Python desprezará o método da classe-pai e só prestará atenção no método definido na classe-filha.
    Em #a temos um exemplo de método que foi sobrescrito pois ele não fará sentido em existir na classe-filha. Em seguida temos o método sendo chamado na classepai e depois da classe-filha para demonstrar que o método da classe-pai não foi alterado."""

print("\nExemplo 3")

class Carro_3():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano
        self.tanque_combustivel = 50

    def descrição(self):
        print(f"O carro {self.modelo.title()} é da marca {self.montadora.upper()}, ano {self.ano}.")

    def capacidade_tanque(self):
        print(f"Este carro tem um tanque de combustível com {self.tanque_combustivel}L")

class Carro_Eletrico_3(Carro_3):
    def __init__(self, montadora, modelo, ano):
        super().__init__(montadora, modelo, ano)
        self.bateria_potencia = 70
    
    def capacidade_tanque(self): #a
        print(f"Este carro não tem um tanque de combustível.")

my_car_3 = Carro_3("Cintroen", "C3", 2024)
my_tesla_3 = Carro_Eletrico_3("tesla", "modelo s", 2025)

my_car_3.descrição()
my_car_3.capacidade_tanque()
my_tesla.descrição()
my_tesla_3.capacidade_tanque()

"""
Instância como atributos
    Ao modelar algo você pode perceber que há uma lista crescente de atributos e métodos e que seus arquivos estão começando a ficar extensos, nessas situações pode ser melhor escrever parte de uma classe como uma classe separada, dividindo-a em partes menores que funcionem em conjunto."""

print("\nExemplo 4")
class Carro_4():
    def __init__(self, montadora, modelo, ano):
        self.montadora = montadora
        self.modelo = modelo
        self.ano = ano

    def descrição(self):
        print(f"O carro {self.modelo.title()} é da marca {self.montadora.upper()}, ano {self.ano}.")

class Bateria_4(): #b
    def __init__(self, pot_bateria=70): #c
        self.pot_bateria = pot_bateria

    def bateria_descricao(self):
        print(f"Este carro tem uma bateria com capacidade de {self.pot_bateria}KWh")

class Carro_Eletrico_4(Carro_4):
    def __init__(self, montadora, modelo, ano):
        super().__init__(montadora, modelo, ano)
        self.bateria = Bateria_4() #d

my_tesla_4 = Carro_Eletrico_4("tesla", "modelo s", 2025) #e

my_tesla_4.bateria.bateria_descricao()
my_tesla_4.bateria.pot_bateria = 90 #f
my_tesla_4.bateria.bateria_descricao()

"""
    Em #b definimos uma nova classe chamada #Bateria_4 que não herda de nenhuma outra classe.
    Em #c no método __init__() tem uma parâmetro opicional que define a capacidade a pot_bateria em 70 se nenhum valor for especificado.
    Em #d adicionamos um atributo chamado self.bateria, essa linhas diz a Python para criar uma nova instância de #Bateria_4 (com default de 70, pois não estamos especificando nenhum valor).
    Toda vez que o método __init__() for chamado, qualquer instância de Carro_Eletrico_4 agora terá uma instância de Bateria_4 criada automaticamente.
    Em e# é importante observar que quando quisermos descrever a bateria, precisamos trabalhar com o atributo #bateria e depois chamar o método bateria_descricao() que foi associado a instância #Bateria_4 armazenada nesse atributo.
    Em #f é demonstrado que para alterar o atributo #pot_bateria foi necessário primeiro acessar o atributo #bateria, local onde está armazenado todos os atributos da classe Bateria_4.
    
Modelando objetos do mundo real"""
    