from time import sleep
from logins.comandos import menu


def CriarArquivo(nome):
    chave = str(input(f'Tem certeza de criar o arquivo em {nome}? ')).upper().strip()
    if chave[0] == 'S':
        arquivo = open(nome, 'wt+')
    else:
        pass


def Existe(nome):
    try:
        pasta = open(nome, 'rt')
        pasta.close()
    except:
        print('\033[34m*Pasta não encontrada\033[m')
    else:
        print('\033[34m*Pasta existente.\033[m')
        return True


def Ver(nome):
    menu.Cabecalho('LENDO ARQUIVO')
    arquivo = open(nome, 'r')
    for linha in arquivo:
        palavra = linha.split()
        print(f'{palavra[0]}\nLogin: {palavra[1]}\t\tSenha: {palavra[2]}\n')
        sleep(0.6)


def Escrever(nome, a, b, c):
    try:
        arquivo = open(nome, 'at')
        arquivo.write(f'{a}\t\t{b}\t\t\t{c}\n')
    except:
        print('Erro ao adicionar novo login')
    else:
        print('Dados adicionados')
