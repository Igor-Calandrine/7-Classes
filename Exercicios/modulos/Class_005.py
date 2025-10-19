"""Tentativas de login: Acrescente um atributo chamado login_attempts à sua classe  User do Exercício  003. Escreva um método chamado increment_login_attempts() que incremente o valor de login_attempts em 1. Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0. Crie uma instância da classe User e chame increment_login_attempts()"""

class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome, nome_pai, nome_mae, estado_civil, profissao):
        self.primeiro_nome = primeiro_nome.title()
        self.ultimo_nome = ultimo_nome.title()
        self.nome_pai = nome_pai.title()
        self.nome_mae = nome_mae.title()
        self.estado_civil = estado_civil
        self.profissao = profissao
        self.tentativa_loggin = 0

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

    def soma_tentativa_loggin(self):
        self.tentativa_loggin += 1
        print(f"\nTentavivas de loggin: {self.tentativa_loggin}")

    def reset_tentativa_loggin(self):
        self.tentativa_loggin = 0
        print("\nTentativas de loggin reiniciadas")
        print(f"Tentavivas de loggin: {self.tentativa_loggin}")