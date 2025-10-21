"""Vários módulos: Armazene a classe User em um módulo e as classes Privileges e Admin em um módulo separado. Em outro arquivo, crie uma instância de Admin e chame show_privileges() para mostrar que tudo  continua funcionando de forma apropriada."""

from modulos.Class_012a import Usuario
from modulos.Class_012b import Adm, Privilegios

igor_usuario = Usuario("Igor", "Araújo", "Mário Célio", "Ana Cristina")
igor_usuario = Adm("Igor", "Araújo", "Mário Célio", "Ana Cristina")

igor_usuario.info_usuario()
igor_usuario.privilegios.info_privilegios()