import json

class Aluno:
    def __init__(self, nome, data_nasc, email, fone, endereco):
        self.nome = nome
        self.data_nasc = data_nasc
        self.email = email
        self.fone = fone
        self.endereco = endereco

    def to_dict(self):
        return {
            'nome': self.nome,
            'data_nasc': self.data_nasc,
            'email': self.email,
            'fone': self.fone,
            'endereco': self.endereco
        }

    @staticmethod
    def from_dict(data):
        return Aluno(
            nome=data['nome'],
            data_nasc=data['data_nasc'],
            email=data['email'],
            fone=data['fone'],
            endereco=data['endereco']
        )

class CadastroAlunos:
    def __init__(self, arquivo='alunos.json'):
        self.arquivo = arquivo
        self.carregar_alunos()

    def carregar_alunos(self):
        try:
            with open(self.arquivo, 'r') as file:
                self.alunos = json.load(file)
        except FileNotFoundError:
            self.alunos = []
        except json.JSONDecodeError:
            self.alunos = []

    def salvar_alunos(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.alunos, file, indent=4)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno.to_dict())
        self.salvar_alunos()

    def listar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno['nome'].lower() == nome.lower():
                return aluno
        return None

    def listar_todos_alunos(self):
        return self.alunos

    def alterar_endereco(self, nome, novo_endereco):
        for aluno in self.alunos:
            if aluno['nome'].lower() == nome.lower():
                aluno['endereco'] = novo_endereco
                self.salvar_alunos()
                return True
        return False

def main():
    cadastro = CadastroAlunos()

    while True:
        print("\n1. Adicionar aluno")
        print("2. Listar aluno por nome")
        print("3. Listar todos os alunos")
        print("4. Alterar endereço do aluno")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
            email = input("E-mail: ")
            fone = input("Telefone: ")
            endereco = input("Endereço: ")
            aluno = Aluno(nome, data_nasc, email, fone, endereco)
            cadastro.adicionar_aluno(aluno)
            print("Aluno adicionado com sucesso!")

        elif opcao == '2':
            nome = input("Digite o nome do aluno que deseja pesquisar: ")
            aluno = cadastro.listar_aluno(nome)
            if aluno:
                print("\nInformações do aluno:")
                for chave, valor in aluno.items():
                    print(f"{chave}: {valor}")
            else:
                print("Aluno não encontrado.")

        elif opcao == '3':
            alunos = cadastro.listar_todos_alunos()
            if alunos:
                print("\nLista de todos os alunos:")
                for aluno in alunos:
                    print("\nAluno:")
                    for chave, valor in aluno.items():
                        print(f"{chave}: {valor}")
            else:
                print("Nenhum aluno cadastrado.")

        elif opcao == '4':
            nome = input("Digite o nome do aluno cujo endereço deseja alterar: ")
            novo_endereco = input("Novo endereço: ")
            if cadastro.alterar_endereco(nome, novo_endereco):
                print("Endereço atualizado com sucesso!")
            else:
                print("Aluno não encontrado.")

        elif opcao == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
