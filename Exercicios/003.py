"""Usuários: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e, então,  crie vários outros atributos normalmente armazenados em um perfil de usuário. Escreva um método de nome describe_user() que apresente um resumo das informações do usuário. Escreva outro método chamado greet_user() que mostre uma saudação personalizada ao usuário. Crie várias instâncias que representem diferentes  usuários e chame os dois métodos para cada usuário."""

from modulos.Class_003 import Usuario

igor = Usuario("Igor", "Calandrine", "mário célio", "anna cristina", "solteiro", "desenvolvedor")
bianca = Usuario("Bianca", "Rohssar", "mário célio", "anna cristina", "casada", "nutricionista")
yuri = Usuario("Yuri", "Guimarães", "mário célio", "anna cristina", "casado", "engenheiro")

igor.descrição()
bianca.descrição()
yuri.descrição()

