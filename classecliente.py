class Cliente(Locadora):
 
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
 
    def alterar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.id = str(input("Digite o ID : ")).upper()
            if Cliente.existe_cliente(self):
                for clt in self.ListaCliente:
                    if clt['id'] == self.id:
                        print(f"\n\tNome: {clt['nome']}")
                        print(f"\tID: {clt['id']}")
 
                        clt['nome'] = str(input("Nome: ")).upper()
                        clt['id'] = str(input("ID: "))
 
                        print(f"Os dados de {self.nome} foram alterados")
                        break
 
            else:
                print("Usuário não está cadastrado!")
        else:
            print("Não existem clientes a serem alterados!")
 
    def listar_cliente(self):
        if len(self.ListaCliente) > 0:
            for i, clt in enumerate(self.ListaCliente):
                print(f"\nCliente {i+1}:")
                print(f"Nome: {clt['nome']}")
                print(f"ID: {clt['id']}")
            print(f"O total de clientes é: {len(self.ListaCliente)}\n")
        else:
            print("\nNão há cliente para listar!\n")
 
    def buscar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o ID: ")).upper()
            for car in self.ListaCliente:
                if car['id'] == self.cpf:
                    print(f"\nNome: {car['nome']}")
                    print(f"ID: {car['id']}")
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")
 
    def existe_cliente(self):
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt['id'] == self.id:
                    return True
        return False
 
    def novo_cliente(self):
        while True:
            self.id = str(input("Digite a ID: "))
            if not Cliente.existe_cliente(self):
                break
            else:
                print(" Usuário já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        usuario = {
            'nome': self.nome,
            'id': self.id
        }
 
        self.ListaCliente.append(usuario)
        print(self.ListaCliente)