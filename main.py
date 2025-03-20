from entity import Empresa, Usuario, Vaga


def main():
    usuarios = []
    empresas = []
    
    while True:
        print("\nMenu:")
        print("1. Criar Usuário")
        print("2. Criar Empresa")
        print("3. Criar Vaga")
        print("4. Candidatar a uma Vaga")
        print("5. Listar Usuários")
        print("6. Listar Empresas e suas Vagas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            area = input("Área de interesse: ")
            try:
                usuario = Usuario(nome, email, area)
                usuarios.append(usuario)
                print("Usuário criado com sucesso!")
            except Exception as e:
                print(e)

        elif opcao == "2":
            nome = input("Nome da empresa: ")
            setor = input("Setor da empresa: ")
            empresa = Empresa(nome, setor)
            empresas.append(empresa)
            print("Empresa criada com sucesso!")

        elif opcao == "3":
            if not empresas:
                print("Nenhuma empresa cadastrada!")
                continue
            print("Empresas disponíveis:")
            for i, empresa in enumerate(empresas):
                print(f"{i}. {empresa.nome}")
            escolha = int(input("Escolha uma empresa pelo número: "))
            empresa = empresas[escolha]
            titulo = input("Título da vaga: ")
            descricao = input("Descrição da vaga: ")
            requisitos = input("Requisitos (separados por vírgula): ").split(",")
            vaga = empresa.criar_vaga(titulo, descricao, requisitos)
            print("Vaga criada com sucesso!")

        elif opcao == "4":
            if not usuarios or not empresas:
                print("É necessário ter usuários e empresas cadastradas!")
                continue
            print("Usuários disponíveis:")
            for i, usuario in enumerate(usuarios):
                print(f"{i}. {usuario.nome}")
            user_choice = int(input("Escolha um usuário pelo número: "))
            usuario = usuarios[user_choice]
            print("Empresas com vagas disponíveis:")
            vagas_disponiveis = [(i, empresa, vaga) for i, empresa in enumerate(empresas) for vaga in empresa.vagas]
            for i, empresa, vaga in vagas_disponiveis:
                print(f"{i}. {vaga.titulo} - {empresa.nome} ({len(vaga.candidatos)} candidatos)")
            vaga_choice = int(input("Escolha uma vaga pelo número: "))
            _, empresa, vaga = vagas_disponiveis[vaga_choice]
            print(vaga.candidatar(usuario))

        elif opcao == "5":
            if not usuarios:
                print("Nenhum usuário cadastrado!")
            else:
                for usuario in usuarios:
                    print(usuario)

        elif opcao == "6":
            if not empresas:
                print("Nenhuma empresa cadastrada!")
            else:
                for empresa in empresas:
                    print(empresa)
                    for vaga in empresa.vagas:
                        print(f"  - {vaga.titulo} ({len(vaga.candidatos)} candidatos)")

        elif opcao == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente!")