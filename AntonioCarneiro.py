# Definição da tarifa. Para alterar seu valor basta alterar o valor da variável.
tarifa = 4.8

# Inicialização de variáveis para uso posterior.
nome = ""
nome_social = ""
cpf = ""
categoria = ""
tarifa_estudante_idoso = tarifa * 0.5
tarifa_social = tarifa * 0.2
tarifa_usuario = 0
usuarios_padrao = 0
usuarios_estudante_idoso = 0
usuarios_social = 0
saldo = 0
saldo_padrao = 0
saldo_estudante_idoso = 0
saldo_social = 0
passagens_compradas = 0
passagens_compradas_padrao = 0
passagens_compradas_estudante_idoso = 0
passagens_compradas_social = 0
recarga = 0
recargas_padrao = 0
recargas_estudante_idoso = 0
recargas_social = 0
opcao_menu = ""
opcao_admin = ""
adm = ""
senha_adm = ""

# Menú interativo.
while opcao_menu != "6":
    print("\nTechVille Trans\n") # Nome do sistema e da cidade. Para ser utilizado por outras cidades basta alterar o nome do sistema e da cidade nesse comando print.
    print("1 - Cadastrar usuário;")
    print("2 - Visualizar saldo;")
    print("3 - Fazer recarga;")
    print("4 - Comprar passagem(ns);")
    print("5 - Gerar relatório;")
    print("6 - Fechar sistema.\n")

    opcao_menu = input("Escolha uma opção: ")

    # O menú pede para digitar uma opção válida até que esta seja digitada.
    while opcao_menu != "1" and opcao_menu != "2" and opcao_menu != "3" and opcao_menu != "4" and opcao_menu != "5" and opcao_menu != "6":
        opcao_menu = input("\nOpção inválida. Selecione uma opção válida: ")

    if opcao_menu == "1":
        nome = input("\nInsira seu nome completo: ")
            
        print("Deseja usar seu nome social?\n")
        print("1 - Sim;")
        print("2 - Não.\n")
            
        opcao_nome = input("Escolha uma opção: ")

        while opcao_nome != "1" and opcao_nome != "2":
            opcao_nome = input("Opção inválida. Selecione uma opção válida: ")

        if opcao_nome == "1":
            nome_social = input("Insira seu nome social: ")

        cpf = input("Informe seu CPF: ")
            
        print("\nCategorias:\n")
        print("1 - Padrão;")
        print("2 - Estudante/idoso;")
        print("3 - Social.\n")
            
        opcao_categoria = input("Escolha uma opção: ")
            
        while opcao_categoria != "1" and opcao_categoria != "2" and opcao_categoria != "3":
            opcao_categoria = input("Opção inválida. Insira uma opção válida: ")

        # As variáveis dentro dos comandos if, elif e else armazenam dados para serem exibidos no relatório posteriormente.
        if opcao_categoria == "1":
            categoria = "Padrão"
            tarifa_usuario = tarifa
            usuarios_padrao += 1
        elif opcao_categoria == "2":
            categoria = "Estudante/idoso"
            tarifa_usuario = tarifa_estudante_idoso
            usuarios_estudante_idoso += 1
        else:
            categoria = "Social"
            tarifa_usuario = tarifa_social
            usuarios_social += 1

        if nome_social == "":
            print(f"Usuário(a) cadastrado(a) com sucesso. Bem-vindo(a), {nome}")
        else:
            print(f"Usuário(a) cadastrado(a) com sucesso. Bem-vindo(a), {nome_social}")

        saldo = 0

    elif opcao_menu == "2":
        if nome == "":
            print("\nNenhum usuário cadastrado. Cadastre-se e tente novamente.")
        else:
            if nome_social == "":
                print(f"\nBem-vindo(a), {nome}, você possui R$ {saldo:.2f} de saldo disponível.")
            else:
                print(f"\nBem-vindo(a), {nome_social}, você possui R$ {saldo:.2f} de saldo disponível.")
    
    elif opcao_menu == "3":
        if nome == "":
            print("\nNenhum usuário cadastrado. Cadastre-se e tente novamente.")
        else:
            if nome_social == "":
                recarga = float(input(f"\nBem-vindo(a), {nome}, digite o valor da recarga: R$ "))
            else:
                recarga = float(input(f"\nBem-vindo(a), {nome_social}, digite o valor da recarga: R$ "))
            
            saldo += recarga

            if categoria == "Padrão":
                saldo_padrao += recarga
                recargas_padrao += 1
            elif categoria == "Estudante/idoso":
                saldo_estudante_idoso += recarga
                recargas_estudante_idoso += 1
            else:
                saldo_social += recarga
                recargas_social += 1

            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print(f"Saldo anterior: R$ {saldo - recarga:.2f}")
    
    elif opcao_menu == "4":
        if nome == "":
            print("\nNenhum usuário cadastrado. Cadastre-se e tente novamente.")
        else:
            if nome_social == "":
                print(f"\nBem-vindo(a), {nome}, você possui saldo para comprar até {saldo // tarifa_usuario:.0f} passagem(ns).")
            else:
                print(f"\nBem-vindo(a), {nome_social}, você possui saldo para comprar até {saldo // tarifa_usuario:.0f} passagem(ns).")

            passagens_compradas = int(input("Insira o número de passagem(ns) que você deseja comprar: "))

            if passagens_compradas > saldo // tarifa_usuario:
                print(f"Você não possui saldo suficiente para comprar {passagens_compradas} passagem(ns). Tente um valor válido ou faça uma recarga.")
            else:
                print(f"Você comprou {passagens_compradas} passagem(ns) com sucesso! Agora você poderá utilizá-las como quiser.")
                
                saldo -= passagens_compradas * tarifa_usuario

                print(f"\nSaldo atual: R$ {saldo:.2f}")
                print(f"Saldo anterior: R$ {saldo + passagens_compradas * tarifa_usuario:.2f}")

                if categoria == "Padrão":
                    saldo_padrao -= passagens_compradas * tarifa_usuario
                    passagens_compradas_padrao += passagens_compradas
                elif categoria == "Estudante/idoso":
                    saldo_estudante_idoso -= passagens_compradas * tarifa_usuario
                    passagens_compradas_estudante_idoso += passagens_compradas
                else:
                    saldo_social -= passagens_compradas * tarifa_usuario
                    passagens_compradas_social += passagens_compradas

    elif opcao_menu == "5":
        print("\nEsta funcionalidade é de uso exclusivo dos administradores do sistema. Para acessar o relatório você deve entrar com o usuário e senha da empresa.")
        print("Deseja continuar:")
        print("1 - Sim;")
        print("2 - Não.\n")

        opcao_admin = input("Escolha uma opção: ")

        while opcao_admin != "1" and opcao_admin != "2":
            opcao_admin = input("Opção inválida. Insira uma opção válida: ")

        if opcao_admin == "2":
            print("Voltando ao menú principal...")
        else:
            # Para ter acesso ao relatório do sistema é necessário entrar com o usuário e senha da empresa. Neste código foram adicionados dois funcionários fictícios, podendo ser alterados, ser adicionados mais funcionários ou remover funcionários existentes.
            adm = input("Usuário: ")
            senha_adm = input("Senha: ")

            if adm == "Jéssica" and senha_adm == "Jessy2025!":
                if usuarios_padrao + usuarios_estudante_idoso + usuarios_social == 0:
                    print("Nenhum usuário cadastrado.")
                else:
                    print(f"\nRelatório do sistema:\n")
                    print(f"Usuários padrões registrados: {usuarios_padrao};")
                    print(f"Usuários estudantes/idosos registrados: {usuarios_estudante_idoso};")
                    print(f"Usuários sociais registrados: {usuarios_social};")
                    print(f"Saldo total de usuários da categoria padrão: {saldo_padrao};")
                    print(f"Saldo total de usuários da categoria estudante/idoso: {saldo_estudante_idoso};")
                    print(f"Saldo total de usuários da categoria social: {saldo_social};")
                    print(f"Total de passagens compradas por usuários da categoria padrão: {passagens_compradas_padrao};")
                    print(f"Total de passagens compradas por usuários da categoria estudante/idoso: {passagens_compradas_estudante_idoso};")
                    print(f"Total de passagens compradas por usuários da categoria social: {passagens_compradas_social};")
                    print(f"Total de recargas de usuários da categoria padrão: {recargas_padrao};")
                    print(f"Total de recargas de usuários da categoria estudante/idoso: {recargas_estudante_idoso};")
                    print(f"Total de recargas de usuários da categoria social: {recargas_social}.")
            elif adm == "Pietro" and senha_adm == "techville.admin0000":
                if usuarios_padrao + usuarios_estudante_idoso + usuarios_social == 0:
                    print("Nenhum usuário cadastrado.")
                else:
                    print(f"\nRelatório do sistema:\n")
                    print(f"Usuários padrões registrados: {usuarios_padrao};")
                    print(f"Usuários estudantes/idosos registrados: {usuarios_estudante_idoso};")
                    print(f"Usuários sociais registrados: {usuarios_social};")
                    print(f"Saldo total de usuários da categoria padrão: {saldo_padrao};")
                    print(f"Saldo total de usuários da categoria estudante/idoso: {saldo_estudante_idoso};")
                    print(f"Saldo total de usuários da categoria social: {saldo_social};")
                    print(f"Total de passagens compradas por usuários da categoria padrão: {passagens_compradas_padrao};")
                    print(f"Total de passagens compradas por usuários da categoria estudante/idoso: {passagens_compradas_estudante_idoso};")
                    print(f"Total de passagens compradas por usuários da categoria social: {passagens_compradas_social};")
                    print(f"Total de recargas de usuários da categoria padrão: {recargas_padrao};")
                    print(f"Total de recargas de usuários da categoria estudante/idoso: {recargas_estudante_idoso};")
                    print(f"Total de recargas de usuários da categoria social: {recargas_social}.")
            else:
                print("Usuário e/ou senha incorreto(s).")

    else:
        print("\nEncerrando o sistema...")