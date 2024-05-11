Usuario = str(input('Qual o seu nome?'))
Saldo_bancario = 1000
Credito_especial = 1000
Limite = 500

opcao = -1  

while True:
    opcao = int(input(f'''
                      ===============MENU===============

                      OLÁ {Usuario.upper()} IFORME O QUE DESEJA
                      (1) SAQUE!
                      (2) DEPOSITAR! 
                      (3) EXIBIR SALDO BANCARIO!
                      (4) PARA CANCELAR A OPERAÇÃO!
                      
                      ==================================
                      '''))

    if opcao == 1:
        
        Saque = float(input (f'QUANDO DESEJA SACAR {Usuario.upper()} ?'))

        Validação_saque = Limite >= Saque

        Analise_de_saldo = (Saldo_bancario >= Saque) or (Credito_especial >= Saque)

        if Analise_de_saldo == True:
            Analise_de_saldo = f'{Usuario.upper()} SAQUE FEITO COM SUCESSO!'
        else:
            Analise_de_saldo = f'{Usuario.upper()} VOCÊ NÃO TEM SALDO O SUFICIENTE!'

        if Validação_saque == True:
            print(Analise_de_saldo)
        else:
            print (f'{Usuario.upper} VOCÊ ATINGIU SEU LIMITE!')
        

    elif opcao == 2:
        Valor_depósito = float(input('QUANTO DESEJA DEPOSITAR:'))

        print(f'VOCÊ TEM {Saldo_bancario + Valor_depósito}')
    elif opcao == 3:
        print(Saldo_bancario)
        print(Credito_especial)
    elif opcao == 4:
        break

    else:
        print('ERRO')