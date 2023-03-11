class Cliente(Locadora):
 
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
 
    def alterar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o CPF : ")).upper()
            if Cliente.existe_cliente(self):
                for clt in self.ListaCliente:
                    if clt['cpf'] == self.cpf:
                        print(f"\n\tNome: {clt['nome']}")
                        print(f"\tCPF: {clt['cpf']}")
                        print(f"\tRG: {clt['rg']}")
 
                        clt['nome'] = str(input("Nome: ")).upper()
                        clt['cpf'] = str(input("CPF: "))
                        clt['rg'] = str(input("RG: "))
 
                        print(f"Os dados de {self.nome} foi alterado")
                        break
 
            else:
                print("Esse CPF não está cadastrado")
        else:
            print("Não existem clientes a serem alterados!")
 
    def listar_cliente(self):
        if len(self.ListaCliente) > 0:
            for i, clt in enumerate(self.ListaCliente):
                print(f"\nCliente {i+1}:")
                print(f"Nome: {clt['nome']}")
                print(f"CPF: {clt['cpf']}")
                print(f"RG: {clt['rg']}\n")
            print(f"Total de clientes é: {len(self.ListaCliente)}\n")
        else:
            print("\nNenhum cliente para listar!\n")
 
    def buscar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o cpf: ")).upper()
            for car in self.ListaCliente:
                if car['cpf'] == self.cpf:
                    print(f"\nNome: {car['nome']}")
                    print(f"CPF: {car['cpf']}")
                    print(f"RG: {car['rg']}\n")
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")
 
    def existe_cliente(self):
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt['cpf'] == self.cpf:
                    return True
        return False
 
    def novo_cliente(self):
        while True:
            self.cpf = str(input("Digite o CPF: "))
            if not Cliente.existe_cliente(self):
                break
            else:
                print("Já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        self.rg = str(input("RG: "))
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }
 
        self.ListaCliente.append(usuario)
        print(self.ListaCliente)