from modulos.Class_012a import Usuario

class Adm(Usuario):
    def __init__(self, nome, sobrenome, pai, mae):
        super().__init__(nome, sobrenome, pai, mae)
        self.privilegios = Privilegios()

class Privilegios():
    def __init__(self):
        self.privilegios = ["add post", "delet post", "edit post", "ban usuario"]
    
    def info_privilegios(self):
        print(f"Adm privilégios:")
        for privilégio in self.privilegios:
            print(f"\t{privilégio}")