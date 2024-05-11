Usuario = str(input('Qual o seu nome?'))
Saldo_bancario = 0
Limite = 5000
extrato = ''

while True:
    opcao = int(input(f'''
                      ===============MENU===============

                      OLÁ {Usuario.upper()} IFORME O QUE DESEJA
                      (1) DEPOSITAR!
                      (2) SAQUE! 
                      (3) EXIBIR EXTRATO BANCARIO!
                      (4) PARA CANCELAR A OPERAÇÃO!
                      
                      ==================================
                      '''))

    if opcao == 1:
         Valor = float(input('QUANTO DESEJA DEPOSITAR:'))

         if Valor > 0:
            Saldo_bancario += Valor
            print(f"SALDO FEITO COM SUCESSO {Usuario.upper()}")
            extrato += f'Depósito: R$ {Valor:.2f}\n'
         else:
            print(f'SELECIONE UM VALOR VALIDO {Usuario.upper()}')
     
    elif opcao == 2:
       
         Valor = float(input (f'QUANDO DESEJA SACAR {Usuario.upper()} ?'))

         if Valor > 0:

            Validação_saque = Limite >= Valor

            Analise_de_saldo = Saldo_bancario >= Valor

            if Analise_de_saldo == True:
               Analise_de_saldo = f'{Usuario.upper()} SAQUE FEITO COM SUCESSO!'
               Saldo_bancario -= Valor
               extrato += f'Saque: R$ {Valor:.2f}\n'
            else:
               Analise_de_saldo = f'{Usuario.upper()} VOCÊ NÃO TEM SALDO O SUFICIENTE!'
  
            if Validação_saque == True:
               print(Analise_de_saldo)
            else:
               print (f'{Usuario.upper()} VOCÊ ATINGIU SEU LIMITE!')
         else:
             print(f'INSIRA UM VALOR VALIDO {Usuario.upper()}')
         
      

    elif opcao == 3:
         print('\n !============================EXTRATO============================!')
         print('\nSEM EXTRATOS!'if not extrato else extrato)
         print(f'\nSaldo : {Saldo_bancario:.2f}')
         print('\n!============================EXTRATO============================!')
    elif opcao == 4:
        break

    else:
        print('SELECIONE UMA OPÇÃO VALIDA')

#ADICIONADO SISTEM DE EXTRATO, VISUAL DE MENU MAIS BONITO, SISTEMA MAIS INTERATIVO E INTUITIVO!S