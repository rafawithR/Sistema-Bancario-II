## Sistema Bancário

### Nesse sistema, as operações são separadas por 

```mermaid
graph
A[Digita CPF] --> B(CPF cadastrado?)
B --Não --> C(Cadastrar Usuario e criar conta)
B --Sim--> D{Rhombus}
C --> D(Login)
D --> Z(Cria nova conta) & E(Escolhe conta)
Z --> E
E --> F(Menu de Operações)
F --> G(Sacar)
G -- Verifica valor desejado, saldo limite saques e valor diarios --> J(Efetiva saque)
F --> H(Extrato)
H --> K(Gera Extrato)
F --> I(Depositar)
I -- Verifica valor --> L(Efetiva Deposito)
F --> Q(Sai do sistema)
F --> N(Criar nova conta)
