"""
Criando e usando uma classe
    Podemos modelar de tudo usando classes, vamos começar escrevendo uma classe simples, #Dog. Essa classe dirá a Python como criar um objeto que represente um cachorro, depois que a classe estiver escrita, ela será usada para criar instâncias individuais, em que cada uma representará umm cachorro especifico.
    Cada instância criada a partir da classe #Dog armazenará um nome, idade, comer, rolando.
"""
print("Exemplo 1")
class Dog(): #u
    def __init__(self, nome, idade):#w
        self.nome = nome #x
        self.idade = idade #x

    def comendo(self): #y
        print(f"{self.nome.title()} vai comer!")

    def rolando(self): #y
        print(f"{self.nome.title()} está rolando!")

"""
    Em #u definimos uma classe chamada #Dog. Por convenção, nomes com a primeira letra maiúscula referem-se a classes em Python. Os parênteses na definição da classe estão vazios porque estamos criando essa classe do zero.

Método __init__()
    Uma função que faz parte de uma classe é cahamda de método.
    Tudo que aprendemos sobre função também se aplica aos métodos, a única diferença será como chamaremos os métodos.
    Em #w temos o método espeical de Python __init__(). Ele executa automaticamente sempre que criamos uma nova instância baseda na classe #Dog. Esse método tem dois underscores no início e fim, uma convenção que ajuda a evitar que os nomes default de métodos Python entrem em conflllito com os nomes de métodos criados por você.
    O parâmetro #self é obrigatório na definição do método e deve estar antes dos demais parâmetros, pois quando Python chama esse método __init__(), a chamada passará o argumento #self automaticamente. Ela dá acesso aos atributos e métodos da classe à instância individual. Sempre que quisermos criar uma instância de classe Dog forneceremos valores apenas para os dois últimos parâmetros, que são nome e idade.
    As duas variáveis definidas em #x têm o prefixo self, variáveis como essas, acessíveis por meio de instâncias, são chamadas de atributos. 
    *Importante: Se você esquecer o #self, os valores nome e idade ficam apenas como variáveis locais dentro do método e não viram atributos do objeto.
    Em #y temos outros dois métodos, esses métodos não precisam de informações adicionais como um nome ou idade, simplesmente os definimos com um parâmetro self. Pode parecer que é apenas uma mensagem, mas em uma situação real, se essa classe fizesse parte de um jogo de computador, esses métodos conteriam o código para fazer a animação de um cahorro ás utilizando.

Criando uma instância apartir de uma classe
    A classe #Dog é um conjunto de instruções que diz a Python como criar instâncias individuais que representa, cachorros específicos. Vamos criar no exemplo abaixo uma instância que represente um cachorro específico.
    Em #u o método __init()__ cria uma instância que representa esse cachorro em particular e define os atributos nome e idade com os valores fornecidos. Esse método não tem uma instrução #return, mas Python devolve automaticamente uma instância na variável #my_dog"""

print("\nExemplo 2")
my_dog = Dog("Pudge", 10) #u

print(f"O nome do meu cachorro é {my_dog.nome.title()}") #v
print(f"Meu cachorro tem {my_dog.idade} anos") #não se utiliza-se self para acessar atributos diretamente

"""
Acessando atributos
    Em #v vemos que para acessar os atributos de uma instância utilize a notação de ponto. Nesse caso, o interpretador olha para a instância my_dog e encontra o atributo nome associado a ela. É o mesmo atributo referenciado como #self.nome na classe #Dog
    Quando quisermos acessar atributos diretamente de um método não deve-se utilizar o #self.

Chamando métodos
    Para chamar um método, especifique o nome da instância (my_dog) e o método que você quer chamar, separados por um ponto. Quando Python lê #my_dog.comendo(), ele procura o método #comendo() na classe #Dog e executa esse código."""

my_dog.comendo()
my_dog.rolando()
