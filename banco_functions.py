from datetime import datetime as dt

HORA = dt.now()

if HORA.hour < 12:
    turno = 'Bom dia'
elif 12 <= HORA.hour <= 18:
    turno = 'Boa tarde'
else:
    turno = 'Boa noite'

USUARIOS=[]
CONTAS = []

#USUARIOS = [[cpf, {nome: None, Sobrenome: None, nascimento: None, endereco: '', contas_validas:[numero_conta]}]]  Dicionário usuário

#CONTAS = [[numero_conta, {saldo: '', extrato:''}]]  

# pensar em como usar LIMITE DIARIO DE SAQUES e DATE TIME nas CONTAS INDIVIDUALIZADAS

#Testado
def cadastrar_conta(cpf):
    global USUARIOS
    global CONTAS
    contas_existentes = [i[0] for i in CONTAS]
    if len(contas_existentes) == 0:
        nova_conta = [1, {'saldo': '', 'extrato': ''}]
    else:
        nova_conta = [int(contas_existentes[-1]) + 1, {'saldo': '', 'extrato': ''}] 
    for i in USUARIOS:
        if i[0] == cpf:
            i[1]['contas_validas'].append(nova_conta[0]) 
    CONTAS.append(nova_conta) 
    return nova_conta   

#Testado
def cadastrar_usuario(cpf,nome,sobrenome, data_nascimento, endereço):
    global USUARIOS
    global CONTAS
    novo_usuario=[cpf, {'nome': nome, 'sobrenome': sobrenome, 'nascimento': data_nascimento, 'endereco': endereço, 'contas_validas':[]}]
    print(novo_usuario[1])
    USUARIOS.append(novo_usuario)
    return True

#Testado    
def mostrar_conta(cpf):
    global CONTAS
    global USUARIOS
    for usuario in USUARIOS:
        if usuario[0] == int(cpf):
            contas_ativas = usuario[1]['contas_validas']        
        else:
            continue
    return contas_ativas
    
#Testado    
def selecionar_conta(numero_conta,cpf):
    global CONTAS
    contas_ativas = mostrar_conta(cpf)
    if numero_conta in contas_ativas:
        for conta in CONTAS:
            if conta[0] == numero_conta:
                return conta
            else:
                continue
    else:
        return None

def extrato_saldo(saldo, extrato_conta_ativa=True):
    conta_ativa = selecionar_conta(numero_conta) 
    if extrato_conta_ativa == True:
        return conta_ativa[1]['extrato']
    else:
        return saldo

def saque(saldo=saldo_conta_ativa,valor=total_saque,extrato=True,limite=500,numero_saques=LIMITE_DIARIO_SAQUES,limite_saques=LIMITE_VALOR_SAQUES):
    global VALORES
    global saldo
    saldo -= quantia
    VALORES += f'Saque    {hora.month}/{hora.year} -R${quantia:.2f}\n'
    return saldo, extrato

def deposito(saldo, valor, extrato):
    global VALORES
    global saldo
    saldo += quantia
    VALORES += f'Deposito {hora.month}/{hora.year}  R${quantia:.2f}\n'
    return saldo, extrato

def busca_cpf(cpf,usuarios=USUARIOS):
    global USUARIOS
    if len(cpf) != 11:
        return print('CPF inválido!')
    else:
        lista_cpfs=[]
        for usuario in USUARIOS:
            lista_cpfs.append(usuario[0])
        if cpf in lista_cpfs:
            nome = USUARIOS[cpf.index()][1]['nome']
            return cpf, nome
        else:
            return None

def inicio():
    global HORA
    while True:
        print(f'''
################################# MENU ##################################

Data: {HORA.day}/{HORA.month}/{HORA.year}  
Hora: {HORA.ctime()[10:16]}

{turno}! O que gostaria de fazer:

[1] - Login em conta de CPF já cadastrado
[2] - Cadastrar novo CPF e abrir conta
[3] - Sair

    ''')

        opcao=input('Digite aqui sua opção: ')
        if opcao == str(1):
            cpf =input('Digite aqui seu CPF: ')
            cliente = busca_cpf(cpf)
            if cliente != None:
                print(f'''Seja bem-vindo, {cliente[1]}!
                      
                      -----------------------------------------------------
                      
                      Estas são as suas contas disponiveis:

======================================================
Agência:  0001
                      ''')
                for conta in mostrar_conta(cpf):
                    print(f'Conta: {conta}')

                print(f'''Cliente: {cliente[1]})
======================================================''')
                
                conta_escolhida = input('Digite o numero da conta que você deseja acessar: ')
                operacoes(cliente[0],conta_escolhida)
                break    
            else: 
                print('''Não foi possivel localizar seu CPF. Verifique se o CPF digitado está correto''')
                continue
        elif opcao == str(2):
            print('''Ok! Vamos começar. Para isso precisaremos de algumas informações
              
              ''')
            cpf = input('Digite seu CPF: ')
            nome = input('Digite seu Nome: ')
            sobrenome = input('Digite seu Sobrenome: ')
            nascimento_dia = input('Digite sua data de Nascimento (ex: 03): ')
            nascimento_mes = input('Digite sua data de Nascimento (ex: 02): ')
            nascimento_ano = input('Digite sua data de Nascimento (ex: 1989): ')
            logradouro = input('Digite seu logradouro: ')
            numero = input('Digite o número da sua residência: ')
            bairro = input('Digite o bairro: ')
            cidade = input('Digite a cidade: ')
            estado = input('Digite a sigla do estado: ')
            data_nascimento = f'{nascimento_dia}/{nascimento_mes}/{nascimento_ano}'
            endereco = f'{logradouro.upper},{numero}-{bairro.upper}-{cidade.upper}/{estado.capitalize}'
            pronomes = input('''Quais seus pronomes? 
                         [1] Ela/Dela
                         [2] Ele/Dele
                         [3] Elu/Delu
                         
                         : ''')
            genero = ''
            if pronomes == str(1):
                genero == 'a'
            elif pronomes == str(2):
                genero == 'o'
            else:
                genero == 'e'
            if cadastrar_usuario(cpf,nome,sobrenome,data_nascimento,endereco) == True:
                print(f'Cadastro concluido com sucesso! Seja muito bem-vind{genero} ao nosso banco, {nome}!')
                conta_escolhida = mostrar_conta(cpf)[0]
                operacoes(cpf,conta_escolhida)
            else:
                print('Algo deu errado, vamos tentar novamente!')
        else:
            print('Até a próxima!')
        break

def operacoes(cliente):
    global CONTAS
    global USUARIOS
    global HORA
    limite_valor_saque = 500
    limite_diario_saque = 3
    while True:
        print(f'''
{turno}, {cliente}! O que você gostaria de fazer?

        [1] - Sacar 
        [2] - Depositar
        [3] - Verificar extrato bancário
        [4] - Cadastrar nova conta
        [0] - Sair do sistema
''')

        opcao = input(': ')

        if int(opcao) == 1:
            quantia = float(input("Quanto você deseja sacar? "))
            if (float(quantia) >= limite_valor_saque):
                print('O valor máximo por saque é de R$500.')
            elif limite_diario_saque >= 3:
                print('Limite de 3 saques diários já atingidos.')
            elif (float(quantia) > saldo) :
                print(f'Saldo insuficiente! Seu saldo atual é R${saldo:.2f}.')
            elif quantia <= 0:
                print(f'Valor incorreto informado.')
            else:
                #TODO: IMPLEMENTAR SAQUE
                LIMITE_DIARIO_SAQUES += 1
                print(f'''
Saque realizado com sucesso!
            
Seu saldo atual é R${saldo:.2f}.
''')

        elif int(opcao) == 2:
            quantia = float(input('Quanto você gostaria de depositar? '))
            if quantia <= 0:
                print(f'Valor incorreto informado.')
            else:
                #TODO:Implementar deposito
                print(f'''
                Deposito realizado com sucesso!

Seu saldo atual é R${saldo:.2f}
''')
        elif int(opcao) == 3:
            print('EXTRATO'.center(29, '-'))
            print(f'Não há registros de movimentação na sua conta' if not VALORES else VALORES)
            print(f'''Seu saldo atual é {saldo:.2f}
------------------------------''')
        elif int(opcao) == 0:
            print(f'''

Obrigado por escolher nosso banco! {turno} e volte sempre!

''')
            break
        else:
            print('Opção inválida')
