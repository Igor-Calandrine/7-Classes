"""Importando Admin: Comece com seu programa do Exercício 8. Armazene as classes User, Privileges e Admin em um módulo. Crie um arquivo separado e uma instância de Admin e chame show_privileges() para mostrar que tudo está funcionando de forma apropriada."""

import modulos.Class_011

igor_usuario = modulos.Class_011.Usuario("Igor", "Araújo", "Mário Célio", "Ana Cristina")
igor_usuario = modulos.Class_011.Adm("Igor", "Araújo", "Mário Célio", "Ana Cristina")

igor_usuario.info_usuario()
igor_usuario.privilegios.info_privilegios()