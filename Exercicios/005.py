"""Tentativas de login: Acrescente um atributo chamado login_attempts à sua classe  User do Exercício  003. Escreva um método chamado increment_login_attempts() que incremente o valor de login_attempts em 1. Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0. Crie uma instância da classe User e chame increment_login_attempts()"""

from modulos.Class_005 import Usuario

igor = Usuario("Igor", "Calandrine", "mário célio", "anna cristina", "solteiro", "desenvolvedor")
bianca = Usuario("Bianca", "Rohssar", "mário célio", "anna cristina", "casada", "nutricionista")
yuri = Usuario("Yuri", "Guimarães", "mário célio", "anna cristina", "casado", "engenheiro")

igor.descrição()
igor.soma_tentativa_loggin()
igor.soma_tentativa_loggin()
igor.soma_tentativa_loggin()
igor.soma_tentativa_loggin()
igor.soma_tentativa_loggin()
igor.reset_tentativa_loggin()