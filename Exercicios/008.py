"""Privilégios: Escreva uma classe Privileges separada. A classe deve ter um atributo  privileges  que  armazene  uma  lista  de  strings  conforme  descrita  no Exercício 7. Transfira o método show_privileges() para essa classe. Crie uma instância  de  Privileges  como  um  atributo  da  classe  Admin. Crie uma  nova instância de Admin e use seu método para exibir os privilégios."""

from modulos.Class_008 import Usuario, Adm

igor_usuario = Usuario("Igor", "Araújo", "Mário Célio", "Ana Cristina")
igor_usuario = Adm("Igor", "Araújo", "Mário Célio", "Ana Cristina")

igor_usuario.info_usuario()
igor_usuario.privilegios.info_privilegios()