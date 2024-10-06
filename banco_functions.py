from datetime import datetime as dt

HORA = dt.now()

if HORA.hour < 12:
    turno = 'Bom dia'
elif 12 <= HORA.hour <= 18:
    turno = 'Boa tarde'
else:
    turno = 'Boa noite'

USUARIOS = []
CONTAS = []
AGENCIA = '0001'
LIMITE = 500
LIMITE_SAQUES = 3
SALDO = 0
EXTRATO = ""
NUMERO_SAQUES = 0

def usuarios_cadastrados():
    global USUARIOS
    lista = [usuario['cpf'] for usuario in USUARIOS]
    return lista

def cadastra_usuario(lista_usuarios):
    cpf = int(input('Digite seu CPF: '))
    if cpf in lista_usuarios:
        print('Este usuário já está cadastrado!')
        return
    primeiro_nome = input('Digite seu Nome: ')
    sobrenome = input('Digite seu Sobrenome: ')
    nascimento_dia = input('Digite o DIA do seu Nascimento (ex: 03): ')
    nascimento_mes = input('Digite o MÊS do seu Nascimento (ex: 02): ')
    nascimento_ano = input('Digite o ANO do seu Nascimento (ex: 1989): ')
    logradouro = input('Digite seu logradouro: ')
    numero = input('Digite o número da sua residência: ')
    bairro = input('Digite o bairro: ')
    cidade = input('Digite a cidade: ')
    estado = input('Digite a sigla do estado: ')
    nome_completo= f'{primeiro_nome} {sobrenome}'
    data_nascimento = f'{nascimento_dia}/{nascimento_mes}/{nascimento_ano}'
    endereco = f'{logradouro.capitalize()},{numero}-{bairro.capitalize()}-{cidade.capitalize()}/{estado.upper()}'
    USUARIOS.append({'cpf':cpf, 'nome':nome_completo, 'nascimento':data_nascimento, 'endereco':endereco})
    print('''
          
          Cadastro realizado com sucesso!
          
          ''')

def contas_ativas():
    contas = []
    for ativas in CONTAS:
        contas.append(ativas['conta'])
    return contas

def cria_conta(usuario):
    if usuario not in usuarios_cadastrados():
        print('''
              
              Este CPF não consta no nosso sistema. Para abrir uma conta, cadastre-se!
              
              ''')
        return
    CONTAS.append({'agencia':AGENCIA, 'conta':contas_ativas()[-1] + 1, 'usuario':usuario} if len(contas_ativas()) != 0 else {'agencia':AGENCIA, 'conta': 1, 'usuario':usuario})
    print('\n Conta criada com sucesso! \n')
    return 

def saque(*,saldo, valor, extrato, saques, limite_diario, limite_numero_saque):
    global SALDO
    global EXTRATO
    global NUMERO_SAQUES
    if valor > saldo:
        print('Saldo não disponível')
        return
    elif saques >= limite_numero_saque:
        print('Você já excedeu o limite de saques hoje!')
        return
    elif limite_diario < valor <= 0:
        print('Este valor não pode ser sacado')
        return
    SALDO -= valor
    EXTRATO += f'Saque    {HORA.month}/{HORA.year} -R${valor:.2f}\n'
    NUMERO_SAQUES += 1
    print(f'\n Saque de R${valor:.2f} realizado com sucesso!')

def deposito(saldo, valor, extrato,/):
    global SALDO
    global EXTRATO
    if valor <=0:
        print('Este valor não pode ser depositado!')
    SALDO += valor
    EXTRATO += f'Deposito {HORA.month}/{HORA.year}  R${valor:.2f}\n'
    return saldo

def extrato(saldo,/,*,extrato):
    print('EXTRATO'.center(29, '-'),end='\n')
    print(f'Não há registros de movimentação na sua conta' if not EXTRATO else EXTRATO)
    print(f'''Seu saldo atual é R${SALDO:.2f}''')

def listar_contas():
    for usuario in USUARIOS:
        for conta in CONTAS:
            if usuario['cpf'] == conta['usuario']:
                print('CONTAS ATIVAS'.center(29, '-'),end='\n')
                print(f'''
Agencia: {conta['agencia']}, Conta: {conta['conta']}, Usuário: {usuario['nome']} 
''')
            
def inicio():
    global HORA
    while True:
        print(f'''
################################# MENU ##################################

Data: {HORA.day}/{HORA.month}/{HORA.year}  
Hora: {HORA.ctime()[10:16]}

{turno}! O que você gostaria de fazer?

[1] - Saque
[2] - Deposito
[3] - Extrato
[4] - Cadastrar novo usuário
[5] - Criar nova conta
[6] - Ver contas
[0] - Sair

    ''')

        opcao=str(input('Digite aqui o número da opção escolhida: '))
        if opcao == '1':
           valor = float(input('Quanto você deseja sacar? '))
           saque(saldo=SALDO,valor=valor,extrato=EXTRATO,saques=NUMERO_SAQUES,limite_numero_saque=LIMITE_SAQUES,limite_diario=LIMITE)
        elif opcao == '2':
            valor = float(input('Quanto você deseja depositar? '))
            deposito(SALDO,valor,EXTRATO)
        elif opcao == '3':
            extrato(SALDO,extrato=EXTRATO)
        elif opcao == '4':
            cadastra_usuario(usuarios_cadastrados())
        elif opcao == '5':
            usuario=int(input('Digite seu CPF (somente números): '))
            cria_conta(usuario,usuarios_cadastrados())
        elif opcao == '6':
            if len(CONTAS) != 0:
                listar_contas()
            else: print('''
Não há contas registradas
                        ''')     
        elif opcao == '0':
            print(f'''

Obrigado por escolher nosso banco! {turno} e volte sempre!

''')    
            break


inicio()