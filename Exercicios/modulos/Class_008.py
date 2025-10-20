class Usuario():
    def __init__(self, nome, sobrenome, pai, mae):
        self.nome = nome
        self.sobrenome = sobrenome
        self.pai = pai
        self.mae = mae
        
    def info_usuario(self):
        print(f"Nome: {self.nome.title()} {self.sobrenome.title()} ")
        print(f"Filiação:")
        print(f"\tMãe: {self.mae}")
        print(f"\tPai: {self.pai}")

class Adm(Usuario):
    def __init__(self, nome, sobrenome, pai, mae):
        super().__init__(nome, sobrenome, pai, mae)
        self.privilegios = Privilegios()

    # def info_adm(self):
    #     print(f"Adm privilégios:")
    #     for privilégio in self.privilegios:
    #         print(f"\t{privilégio}")

class Privilegios():
    def __init__(self):
        self.privilegios = ["add post", "delet post", "edit post", "ban usuario"]
    
    def info_privilegios(self):
        print(f"Adm privilégios:")
        for privilégio in self.privilegios:
            print(f"\t{privilégio}")



