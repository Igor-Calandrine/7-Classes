"""Usuários: Crie uma classe chamada User. Crie dois atributos de nomes first_name e last_name e, então,  crie vários outros atributos normalmente armazenados em um perfil de usuário. Escreva um método de nome describe_user() que apresente um resumo das informações do usuário. Escreva outro método chamado greet_user() que mostre uma saudação personalizada ao usuário. Crie várias instâncias que representem diferentes  usuários e chame os dois métodos para cada usuário."""

class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome, nome_pai, nome_mae, estado_civil, profissao):
        self.primeiro_nome = primeiro_nome.title()
        self.ultimo_nome = ultimo_nome.title()
        self.nome_pai = nome_pai.title()
        self.nome_mae = nome_mae.title()
        self.estado_civil = estado_civil
        self.profissao = profissao

    def descrição(self):
        print("Usuário")
        print("-" * 15)
        print(f"\tNome: {self.primeiro_nome}")
        print(f"\tÚltimo nome: {self.ultimo_nome}")
        print("Filiação:")
        print(f"\tPai: {self.nome_pai}")
        print(f"\tMãe: {self.nome_mae}")
        print(f"\n\tEstado Civil: {self.estado_civil}")
        print(f"\tProfissão: {self.profissao}")
        print()

    

