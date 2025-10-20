"""Admin: Um administrador é um tipo especial de usuário. Escreva uma classe chamada Admin que herde da classe User escrita no Exercício 3, ou no Exercício 5. Adicione um atributo privileges que armazene uma lista de strings como "can add post", "can delete post" "can ban user", e assim por diante. Escreva um método chamado show_privileges() que liste o conjunto de privilégios de um administrador. Crie uma instância de Admin e chame seu método."""

from modulos.Class_007 import Usuario, Adm

igor_usuario = Usuario("Igor", "Araújo", "Mário Célio", "Ana Cristina")
igor_usuario = Adm("Igor", "Araújo", "Mário Célio", "Ana Cristina")

igor_usuario.info_usuario()
igor_usuario.info_adm()