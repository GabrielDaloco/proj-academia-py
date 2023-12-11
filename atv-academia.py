import sqlite3

#Tela de Seleção do Cadastro ==========================================================================
def cadastrar():
    print("\n")
    print("=================")
    print("# Cadastramento #")
    print("=================")

    print("\n")

    acoes = ['Professor','Aluno','Treino','Exercício','Sair']

    print('1.' + acoes[0]) #Professor
    print('2.' + acoes[1]) #Aluno
    print('3.' + acoes[2]) #Treino
    print('4.' + acoes[3]) #Exercício

    print('9.' + acoes[4]) #Sair

    selecao_cadastro = int(input("Sua opção: "))

    match selecao_cadastro:
        case 1:
            cadastro_prof()
        case 2 :
            cadastro_aluno()
        case 3:
            cadastro_treino()
        case 4:
            cadastro_exercicio()
        case 9:
            exit()
        case _:
            print("Não está na lista.")

#Cadastro de Professores ================================================================
def cadastro_prof():
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        print("\n")
        vCPF = input("CPF do Professor: ")
        vNome = input("Nome do Professor: ")
        vData_Nasc = input("Data de Nascimento do Professor: (Formato: AAAA-MM-DD) ")

        vConfirma = input("Deseja cadastrar? (S/N) ")
        if vConfirma.upper() == "S":
            cursor.execute("select count(*) from Professor where CPF = ?", (vCPF,) )
            dado = cursor.fetchone()
            if dado:
                contador = dado[0]
                if(contador == 1):
                    print("\n")
                    print("Já existe um professor com esse CPF.")
                    print("Repetindo...")
                    cadastro_prof()
                else:
                    conn.execute("insert into Professor values(?, ?, ?)",(vCPF,vNome,vData_Nasc) )
                    conn.commit()
                    print("\n")
                    print("Professor cadastrado com sucesso!")

            print("\n")
            vContinua = input("Deseja continuar cadastrando? (S/N) ")
            if(vContinua.upper() == "S"):
                print("Repetindo...")
                print("\n")
            else:
                conn.close()
                exit()
        else:
            print("Repetindo...")
            print("\n")

#Cadastro de Alunos =====================================================================
def cadastro_aluno():
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        print("\n")
        vCPF = input("CPF do Aluno: ")
        vNome = input("Nome do Aluno: ")
        vData_Nasc = input("Data de Nascimento do Aluno: (Formato: AAAA-MM-DD) ")

        vConfirma = input("Deseja cadastrar? (S/N) ")
        if vConfirma.upper() == "S":
            cursor.execute("select count(*) from Aluno where CPF = ?", (vCPF,) )
            dado = cursor.fetchone()
            if dado:
                contador = dado[0]
                if(contador == 1):
                    print("\n")
                    print("Já existe um aluno com esse CPF.")
                    print("Repetindo...")
                    cadastro_aluno()
                else:
                    conn.execute("insert into Aluno values(?, ?, ?)",(vCPF,vNome,vData_Nasc) )
                    conn.commit()
                    print("\n")
                    print("Aluno cadastrado com sucesso!")   

            vContinua = input("Deseja continuar cadastrando? (S/N) ")
            if(vContinua.upper() == "S"):
                print("Repetindo...")
                print("\n")
            else:
                conn.close()
                exit()
        else:
            print("Repetindo...")
            print("\n")

#Cadastro de Treinos ===================================================================
def cadastro_treino():
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        print("\n")
        vCPF_aluno = input("CPF do Aluno: ")
        cursor.execute("select Nome, data_nasc from Aluno where CPF = ?", (vCPF_aluno,) )
        dado = cursor.fetchone()
        if dado:
            nome, data_nasc = dado
            print("Aluno: ", nome)
            print("Data de Nascimento: ", data_nasc)
            vContinua = input("Deseja continuar? (S/N) ")
            if (vContinua.upper() == "S"):
                break
            else:
                print("Repetindo...")
        else:
            print("Não há um aluno com esse CPF.")

    while True:
        print("\n")
        vCPF_prof = input("CPF do Professor: ")
        cursor.execute("select Nome, data_nasc from Professor where CPF = ?", (vCPF_prof,) )
        dado = cursor.fetchone()
        if dado:
            nome, data_nasc = dado
            print("Professor: ", nome)
            print("Data de Nascimento: ", data_nasc)
            vContinua = input("Deseja continuar? (S/N) ")
            if (vContinua.upper() == "S"):
                break
            else:
                print("Repetindo...")
        else:
            print("Não há um professor com esse CPF.")

    print("\n")
    vConfirma = input("Deseja cadastrar? (S/N) ")
    if vConfirma.upper() == "S":
        cursor.execute("select count(*) from Treino where CPF_aluno = ?", (vCPF_aluno,) )
        dado = cursor.fetchone()
        if dado:
            contador = dado[0]
            if(contador == 1):
                print("\n")
                print("Aluno já tem um treino existente.")
                print("Repetindo...")
                cadastro_treino()
            else:
                conn.execute("insert into Treino (CPF_aluno, CPF_prof) values(?, ?)",(vCPF_aluno,vCPF_prof))
                conn.commit()
                print("\n")
                print("Treino cadastrado com sucesso!")
                print("\n")
    else:
        print("Recomeçando...")
        print("\n")
        cadastro_treino()
    
    vContinua = input("Deseja colocar os exercícios? (S/N) ")
    if(vContinua.upper() == "S"):
        while True:
            vNome_exerc = input("Nome do exercício: ")
            vRepeticoes_exerc = input("Repetições do exercício: ")
            vSeries_exerc = input("Quantidade de Séries: ")

            vConfirma = input("Está correto? (S/N) ")
            if(vConfirma.upper() == "S"):
                conn.execute("insert into Exercicios (nome, series, repeticoes, CPF_aluno) values(?, ?, ?, ?)",(vNome_exerc, vSeries_exerc, vRepeticoes_exerc, vCPF_aluno))
                conn.commit()
                print("\n")
                print("Exercício cadastrado com sucesso!")
                vContinua_Exercicio = input("Deseja colocar mais Exercícios no Treino? (S/N) ")
                if(vContinua_Exercicio.upper() == "S"):
                    print("\n")
                    print("Repetindo...")
                    print("\n")
                else:
                    vContinua_Treino = input("Deseja colocar mais treinos? (S/N) ")
                    if(vContinua_Treino.upper() == "S"):
                        cadastro_treino()
                    else:
                        conn.close()
                        exit()
            else:
                print("Repetindo...")
                print("\n")

#Cadastro de Exercícios =================================================================
def cadastro_exercicio():
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        print("\n")
        while True:
            vCPF_aluno = input("CPF do Aluno: ")
            cursor.execute("select count(*) from Aluno where CPF = ?", (vCPF_aluno,) )
            dado = cursor.fetchone()
            if dado:
                contador = dado[0]
                if(contador == 0):
                    print("\n")
                    print("Não há aluno com esse CPF.")
                    print("Repetindo...")
                    cadastro_exercicio()
                else:
                    print("\n")
                    break
            
        while True:
            vNome_exerc = input("Nome do Exercício: ")
            vRepeticoes_exerc = input("Repetições do exercício: ")
            vSeries_exerc = input("Quantidade de Séries: ")

            vConfirma = input("Deseja cadastrar? (S/N) ")
            if vConfirma.upper() == "S":
                conn.execute("insert into Exercicios (nome, series, repeticoes, CPF_aluno) values(?, ?, ?, ?)",(vNome_exerc, vSeries_exerc, vRepeticoes_exerc, vCPF_aluno) )
                conn.commit()
                print("Exercício Cadastrado com Sucesso!")

                print("\n")
                vContinua = input("Deseja continuar cadastrando exercícios para este aluno? (S/N) ")
                if(vContinua.upper() == "S"):
                    print("Repetindo...")
                    print("\n")
                else:
                    vContinua_exercicio = input("Deseja cadastrar exercícios para outros alunos? (S/N): ")
                    if(vContinua_exercicio.upper() == "S"):
                        cadastro_exercicio()
                    else:
                        conn.close()
                        exit()
            else:
                print("Repetindo...")
                print("\n")

#Tela de Seleção da Consulta ============================================================
def consultar():
    print("\n")
    print("=================")
    print("#   Consultar   #")
    print("=================")

    print("\n")

    acoes = ['Professor','Aluno','Treino e Exercícios', 'Sair']

    print('1.' + acoes[0]) #Professor
    print('2.' + acoes[1]) #Aluno
    print('3.' + acoes[2]) #Treino e Exercícios

    print('9.' + acoes[3]) #Sair

    selecao_consulta = int(input("Sua opção: "))

    match selecao_consulta:
        case 1:
            consulta_prof()
        case 2 :
            consulta_aluno()
        case 3:
            consulta_treino()
        case 9:
            exit()
        case _:
            print("Não está na lista.")

#Consulta de Professores ================================================================
def consulta_prof():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Professor: ")
        cursor.execute("select Nome, data_nasc from Professor where CPF = ?", (vCPF,) )
        dado = cursor.fetchone()
    
        if(dado):
            nome, data_nasc = dado
            print("O nome no Professor é: ", nome)
            print("A data de Nascimento do Professor é: ", data_nasc)
            
            vContinua = input("Deseja procurar mais? (S/N) ")
            if(vContinua.upper() == "S"):
                consulta_prof()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Professor inexistente.")
        
#Consulta de Alunos =====================================================================
def consulta_aluno():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Aluno: ")
        cursor.execute("select Nome, data_nasc from Aluno where CPF = ?", (vCPF,) )
        dado = cursor.fetchone()
    
        if(dado):
            nome, data_nasc = dado
            print("O nome no Aluno é: ", nome)
            print("A data de Nascimento do Aluno é: ", data_nasc)
            
            vContinua = input("Deseja procurar mais? (S/N) ")
            if(vContinua.upper() == "S"):
                consulta_aluno()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Aluno inexistente.")

#Consulta de Treino =====================================================================
def consulta_treino():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF_aluno = input("Insira o CPF do Aluno: ")
        cursor.execute("select Exercicios.nome, Exercicios.repeticoes, Exercicios.series, Treino.CPF_prof from Exercicios INNER JOIN Treino on Exercicios.CPF_aluno=Treino.CPF_aluno WHERE Treino.CPF_aluno = ?", (vCPF_aluno,) )
        dados = cursor.fetchall()
    
        if(dados):
            print("\n")
            print("CPF do Professor: ", dados[0][3])
            print("\n")
            print("{:<35} {:<15} {:<30}".format("Exercício", "Repetições", "Séries"))
            print("\n")
            for row in dados:
                print("{:<35} {:<15} {:<30}".format(row[0], row[1], row[2]))
                print("-----------------------------------------------------------------")
            
            print("\n")
            vContinua = input("Deseja procurar mais? (S/N) ")
            if(vContinua.upper() == "S"):
                consulta_treino()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Aluno inexistente.")

#Tela de Seleção da Alteração ===========================================================
def alterar():
    print("\n")
    print("=================")
    print("#   Alteração   #")
    print("=================")

    print("\n")

    acoes = ['Professor','Aluno','Exercício', 'Sair']

    print('1.' + acoes[0]) #Professor
    print('2.' + acoes[1]) #Aluno
    print('3.' + acoes[2]) #Exercício

    print('9.' + acoes[3]) #Sair

    selecao_alterar = int(input("Sua opção: "))

    match selecao_alterar:
        case 1:
            alterar_prof()
        case 2 :
            alterar_aluno()
        case 3:
            alterar_exercicio()
        case 9:
            exit()
        case _:
            print("Não está na lista.")

#Alterar Professor ======================================================================
def alterar_prof():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Professor: ")
        cursor.execute("select Nome, data_nasc from Professor where CPF = ?", (vCPF,) )
        dado = cursor.fetchone()
        
        if dado:
            nome, data_nasc = dado
            vNome = input(f"Insira o novo nome para alteração (antigo: {nome}): ")
            vData_nasc = input(f"Insira a nova data de nascimento para alteração (antigo: {data_nasc}): ")

            conn.execute("update Professor set Nome = ?, data_nasc = ? WHERE CPF = ?", (vNome, vData_nasc, vCPF))
            conn.commit()

            print("\n")
            print("Dado Alterado com Sucesso!")
            print("\n")

            vContinua = input("Deseja alterar dados de outros Professores? (S/N) ")
            if(vContinua.upper() == "S"):
                alterar_prof()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Professor inexistente.")

#Alterar Aluno ==========================================================================
def alterar_aluno():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Aluno: ")
        cursor.execute("select Nome, data_nasc from Aluno where CPF = ?", (vCPF,) )
        dado = cursor.fetchone()
        
        if dado:
            nome, data_nasc = dado
            vNome = input(f"Insira o novo nome para alteração (antigo: {nome}): ")
            vData_nasc = input(f"Insira a nova data de nascimento para alteração (antigo: {data_nasc}): ")

            conn.execute("update Aluno set Nome = ?, data_nasc = ? WHERE CPF = ?", (vNome, vData_nasc, vCPF))
            conn.commit()

            print("\n")
            print("Dado Alterado com Sucesso!")
            print("\n")

            vContinua = input("Deseja alterar dados de outros Alunos? (S/N) ")
            if(vContinua.upper() == "S"):
                alterar_prof()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Aluno inexistente.")

#Alterar Exercícios =====================================================================
def alterar_exercicio():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Aluno: ")
        cursor.execute("select Exercicios.id, Exercicios.nome, Exercicios.repeticoes, Exercicios.series from Exercicios INNER JOIN Treino on Exercicios.CPF_aluno=Treino.CPF_aluno WHERE Treino.CPF_aluno = ?", (vCPF,) )
        dados = cursor.fetchall()
        
        if dados:
            print("\n")
            print("{:<8} {:<35} {:<15} {:<30}".format("ID","Exercício", "Repetições", "Séries"))
            print("\n")
            for row in dados:
                print("{:<8} {:<35} {:<15} {:<30}".format(row[0],row[1], row[2], row[3]))
                print("-----------------------------------------------------------------")
            
            print("\n")

            while True:
                vID = input("Selecione o ID do exercício existente: ")

                cursor.execute("select nome, repeticoes, series from Exercicios where id = ?", (vID,) )
                dado = cursor.fetchone()

                if dado:
                    exercicio, repeticoes, series = dado
                    vExercicio = input(f"Insira o novo nome do exercício para alteração (antigo: {exercicio}): ")
                    vRepeticoes = input(f"Insira a nova qtde de repetições para alteração (antigo: {repeticoes}): ")
                    vSeries = input(f"Insira a nova qtde de séries para alteração (antigo: {series}): ")

                    conn.execute("update Exercicios set nome = ?, series = ?, repeticoes = ? WHERE id = ?", (vExercicio, vSeries, vRepeticoes, vID))
                    conn.commit()

                    print("\n")
                    print("Dados Alterados com Sucesso!")
                    print("\n")
                    break
                else:
                    print("Exercício não existente.")

            vContinua = input("Deseja alterar dados de outros exercícios? (S/N) ")
            if(vContinua.upper() == "S"):
                alterar_exercicio()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Aluno inexistente.")

#Tela de Seleção da Exclusão
def excluir():
    print("\n")
    print("==================")
    print("#    Exclusão    #")
    print("==================")

    print("\n")

    acoes = ['Professor','Aluno', 'Treino' ,'Exercício', 'Sair']

    print('1.' + acoes[0]) #Professor
    print('2.' + acoes[1]) #Aluno
    print('3.' + acoes[2]) #Treino
    print('4.' + acoes[3]) #Exercício

    print('9.' + acoes[4]) #Sair

    selecao_excluir = int(input("Sua opção: "))

    match selecao_excluir:
        case 1:
            excluir_professor()
        case 2 :
            excluir_aluno()
        case 3:
            excluir_treino()
        case 4:
            excluir_exercicio()
        case 9:
            exit()
        case _:
            print("Não está na lista.")

#Exclusão de Professores ================================================================
def excluir_professor():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Professor a ser excluido: ")
        cursor.execute("select Nome, data_nasc from Professor where CPF = ?", (vCPF,) )
        dado = cursor.fetchone()
        if dado:
            nome, data_nasc = dado
            print("Professor: ", nome)
            print("Data de Nascimento: ", data_nasc)
            print("\n")

            vConfirma = input("Deseja excluir? (Tenha em mente que esta exclusão PODE acarretar a exclusão de outros dados.) (S/N): ")
            if(vConfirma.upper() == "S"):
                conn.execute("DELETE from Professor where CPF = ?",(vCPF,) )
                conn.commit()
                print("Professor Excluído com Sucesso!")

                print("\n")
                vContinua = input("Deseja continuar excluindo? (S/N) ")
                if(vContinua.upper() == "S"):
                    print("Repetindo...")
                    print("\n")
                else:
                    conn.close()
                    exit()
            else:
                conn.close()
                exit()
        else:
            print("Não foi encontrado o Professor")
            print("\n")


#Exclusão de Alunos
def excluir_aluno():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Aluno a ser excluido: ")
        cursor.execute("select Nome, data_nasc from Aluno where CPF = ?", (vCPF,) )
        dado = cursor.fetchone()
        if dado:
            nome, data_nasc = dado
            print("Aluno: ", nome)
            print("Data de Nascimento: ", data_nasc)
            print("\n")

            vConfirma = input("Deseja excluir? (Tenha em mente que esta exclusão PODE acarretar a exclusão de outros dados.) (S/N): ")
            if(vConfirma.upper() == "S"):
                conn.execute("DELETE from Aluno where CPF = ?",(vCPF,) )
                conn.commit()
                print("Aluno Excluído com Sucesso!")

                print("\n")
                vContinua = input("Deseja continuar excluindo? (S/N) ")
                if(vContinua.upper() == "S"):
                    print("Repetindo...")
                    print("\n")
                else:
                    conn.close()
                    exit()
            else:
                conn.close()
                exit()
        else:
            print("Não foi encontrado o Aluno")
            print("\n")

#Exclusão de Treinos ====================================================================
def excluir_treino():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Aluno para exclusão do Treino: ")
        cursor.execute("select Aluno.Nome, Treino.CPF_prof from Aluno INNER JOIN Treino on Treino.CPF_aluno=Aluno.CPF where CPF = ? ", (vCPF,) )
        dado = cursor.fetchone()
        if dado:
            nome_aluno, cpf_prof = dado
            print("Aluno: ", nome_aluno)
            
            cursor.execute("select nome from Professor where CPF = ? ", (cpf_prof,) )
            dado = cursor.fetchone()

            nome_prof = dado[0]
            print("Professor: ", nome_prof)
            print("\n")

            vConfirma = input("Deseja excluir o Treino? (Tenha em mente que esta exclusão PODE acarretar a exclusão de outros dados.) (S/N): ")
            if(vConfirma.upper() == "S"):
                conn.execute("DELETE from Treino where CPF_aluno = ?",(vCPF,) )
                conn.commit()
                print("Treino Excluído com Sucesso!")

                print("\n")
                vContinua = input("Deseja continuar excluindo? (S/N) ")
                if(vContinua.upper() == "S"):
                    print("Repetindo...")
                    print("\n")
                else:
                    conn.close()
                    exit()
            else:
                conn.close()
                exit()
        else:
            print("Não foi encontrado o Treino do Aluno")
            print("\n")

#Exclusão de Exercícios ================================================================
def excluir_exercicio():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        vCPF = input("Insira o CPF do Aluno: ")
        cursor.execute("select Exercicios.id, Exercicios.nome, Exercicios.repeticoes, Exercicios.series from Exercicios INNER JOIN Treino on Exercicios.CPF_aluno=Treino.CPF_aluno WHERE Treino.CPF_aluno = ?", (vCPF,) )
        dados = cursor.fetchall()
        
        if dados:
            print("\n")
            print("{:<8} {:<35} {:<15} {:<30}".format("ID","Exercício", "Repetições", "Séries"))
            print("\n")
            for row in dados:
                print("{:<8} {:<35} {:<15} {:<30}".format(row[0],row[1], row[2], row[3]))
                print("-----------------------------------------------------------------")
            
            print("\n")

            while True:
                vID = input("Selecione o ID do exercício existente para exclusão: ")

                cursor.execute("select * from Exercicios where id = ?", (vID,) )
                dado = cursor.fetchone()

                if dado:
                    conn.execute("delete from Exercicios where id = ?", (vID,))
                    conn.commit()
                    
                    print("Exercício Excluído com sucesso!")
                    
                    vContinua = input("Deseja excluir mais algum exercício? (S/N): ")
                    if(vContinua.upper() == "S"):
                        print("Repetindo...")
                        print("\n")
                    else:
                        break
                else:
                    print("Exercício não existente.")

            vContinua = input("Deseja excluir dados de outras pessoas? (S/N) ")
            if(vContinua.upper() == "S"):
                excluir_exercicio()
            else:
                conn.close()
                exit()
        else:
            print("CPF errado ou Aluno inexistente.")


#Tela de Seleção da Listagem
def listar():
    print("\n")
    print("==================")
    print("#     Listar     #")
    print("==================")

    print("\n")

    acoes = ['Professor','Aluno', 'Treino' ,'Exercício', 'Sair']

    print('1.' + acoes[0]) #Professor
    print('2.' + acoes[1]) #Aluno
    print('3.' + acoes[2]) #Treino
    print('4.' + acoes[3]) #Exercício

    print('9.' + acoes[4]) #Sair

    selecao_excluir = int(input("Sua opção: "))

    match selecao_excluir:
        case 1:
            listar_prof()
        case 2 :
            listar_aluno()
        case 3:
            listar_treino()
        case 4:
            listar_exercicio()
        case 9:
            exit()
        case _:
            print("Não está na lista.")

#Listar Professores =====================================================================
def listar_prof():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        cursor.execute("select * from Professor")
        dados = cursor.fetchall()
        
        if dados:
            print("\n")
            print("{:<15} {:<25} {:<30}".format("CPF", "Nome", "Data de Nascimento (AAAA-MM-DD)"))
            print("\n")
            for row in dados:
                print("{:<15} {:<25} {:<30}".format(row[0],row[1], row[2]))
                print("-----------------------------------------------------------------")
            
            print("\n")
            input('Pressione ENTER para sair')

            conn.close()
            exit()
        else:
            print("Não há nenhum Professor cadastrado.")
            break

        
        
#Listar Alunos
def listar_aluno():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        cursor.execute("select * from Aluno")
        dados = cursor.fetchall()
        
        if dados:
            print("\n")
            print("{:<15} {:<25} {:<30}".format("CPF", "Nome", "Data de Nascimento (AAAA-MM-DD)"))
            print("\n")
            for row in dados:
                print("{:<15} {:<25} {:<30}".format(row[0],row[1], row[2]))
                print("-----------------------------------------------------------------")
            
            print("\n")
            input('Pressione ENTER para sair')

            conn.close()
            exit()
        else:
            print("Não há nenhum Aluno cadastrado.")
            break


#Listar Treinos =========================================================================
def listar_treino():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        cursor.execute("select * from Treino")
        dados = cursor.fetchall()
        
        if dados:
            print("\n")
            print("{:<15} {:<15}".format("CPF do Aluno", "CPF do Professor"))
            print("\n")
            for row in dados:
                print("{:<15} {:<15}".format(row[0],row[1]))
                print("-----------------------------------------------------------------")
            
            print("\n")
            input('Pressione ENTER para sair')

            conn.close()
            exit()
        else:
            print("Não há nenhum Treino cadastrado.")
            break


#Listar Exercícios ======================================================================
def listar_exercicio():
    print("\n")
    conn = sqlite3.connect("AcadPacoca.db")
    cursor = conn.cursor()

    while True:
        cursor.execute("select * from Exercicios")
        dados = cursor.fetchall()
        
        if dados:
            print("\n")
            print("{:<8} {:<20} {:<15} {:<15} {:<15}".format("ID", "Exercício", "Repetições", "Séries", "CPF do Aluno"))
            print("\n")
            for row in dados:
                print("{:<8} {:<20} {:<15} {:<15} {:<15}".format(row[0],row[1], row[2], row[3], row[4]))
                print("---------------------------------------------------------------------------------------")
            
            print("\n")
            input('Pressione ENTER para sair')

            conn.close()
            exit()
        else:
            print("Não há nenhum Treino cadastrado.")
            break
        
#Tela de Seleção ========================================================================
acoes = ['Cadastrar','Consultar','Alterar','Excluir','Listar','Sair']

print("=========================")
print("#  Sistema de Usuários  #")
print("#    Academia Paçoca    #")
print("=========================")

print("\n")

print('1.' + acoes[0]) #cadastrar
print('2.' + acoes[1]) #consultar
print('3.' + acoes[2]) #alterar
print('4.' + acoes[3]) #excluir
print('5.' + acoes[4]) #listar

print('9.' + acoes[5]) #sair

selecao = int(input("Sua opção: "))

match selecao:
    case 1:
        cadastrar() #Feito
    case 2:
        consultar() #Feito
    case 3:
        alterar() #Feito
    case 4:
        excluir() #Feito
    case 5:
        listar() #Feito
    case 9:
        exit()
    case _:
        print("Não está na lista.")
