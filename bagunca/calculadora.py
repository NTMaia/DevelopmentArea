import os


def Adicao(valor1, valor2):
    soma = valor1 + valor2
    return soma


def Subtracao(valor1, valor2):
    sub = valor1 - valor2
    return sub


def Divisao(valor1, valor2):
    div = valor1 / valor2
    return div


def Multiplicacao(valor1, valor2):
    multi = valor1 * valor2
    return multi


print('''[1] Adição
[2] Subtração 
[3] Multiplicação
[4] Divição''')
opcao = int(input('Resposta: '))
# limpar tela
print('\n')
os.system('cls' if os.name == 'nt' else 'clear')

digito1 = int(input('Primeiro digito: '))
digito2 = int(input('Segundo digito: '))