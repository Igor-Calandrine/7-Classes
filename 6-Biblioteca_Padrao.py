"""
Biblioteca-padrão Python
    A biblioteca-padrão de Python é um conjunto de módulos incluído em todas as instalações de Python. Podemos usar qualquer função ou classe da bibioteca-padrão com uma instrução #import simples no início do arquivo. Vamos analisar a classe OrderedDict do módulos collections.
    Os dicionários permitem associar informações, mas eles não mantêm um controle da ordem em que os pares chave-valor são acrescentadas, então faremos uso da classe OrderedDict do módulo collections. Vamos usar um exemplo do Cap 6 para demonstrar."""

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'   
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(f"A linguagem favorita de {name.title()} é {language.title()}")

    """Observe que não há chaves, a chamada da classe cria um dicionário ordenado vazio para nós e o armazena em #favorite_languages. Agora quando percorremos com um laço, sabemos que sempre teremos as respostas na ordem em que os itens foram adicionados.
    
Módulo random
    É um módulo muito importante para cohecer, ele gera números aleatórios de várias maneiras. Para acessá-lo escreva."""
    
import random
    
"""Para gerar um número aleatório entre 0.0 e 1.0 (exclusivo 1.0)"""
print(random.random())

"""Para gerar um número inteiro entre a e b (incluindo ambos)"""
print(random.randint(1, 20))

"""Para gerar um número flutuante aleatório entre a e b (incluindo ambos)"""
print(random.uniform(1.5, 3.5))

"""Para escolher um item aleatório de uma sequência (lista, tupla, string, etc)"""
nomes = ["Igor", "Bianca", "Yuri", "Ana", "Mário"]
print(random.choice(nomes))

"""
    O módulo #random não é seguro para uso criptográfico, como em senhas, tokens de segurança. Para isso use:"""

import secrets
print(secrets.token_bytes(16))

"""
    Um execelente recurso para explorar a biblioteca-padrão de Python é um site chamado Python Module of the Week. E observe a tabela de conteúdo. Encontre um módulo que pareça ser interessante e leia sua descrição.
        http://pymotw.com/
"""

"""Estilizando Classes
    Os nomes das classes devem ser escritos com CamelCaps, para isso cada palavra do nome deve ter a primeira letra maipuscula, e você não deve usar underscores.
    Nomes de instâncias e de módulos devem ser escritos com letras minúsculas e underscores entre as palavras.
    Toda classe deve ter uma docstring logo deopis de sua definição. Cada módulo também deve ter uma docstring que descreva para que servem as classes de um módulo.
    Se houver a necessidade de importar um módulo da biblioteca-padrão e um módulo escrito por você, coloque a instrução de importação do módulo da biblioteca-padrão antes, depois uma linhas em branco e a instrução do módulo que você escreveu."""