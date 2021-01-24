def CriarArquivo(diretorio):
    arquivo = open(diretorio, 'wt+')


def ExistePasta(nome):
    try:
        pasta = open(nome, 'rt')
        pasta.close()
    except:
        chave = str(input(f'deseja criar o arquivo "\033[31m{nome}\033[m" nesse diretorio? ')).upper()
        if chave[0] == 'S':
            CriarArquivo(nome)
        else:
            print('\033[34mPasta não encontrada\033[m')
    else:
        print('\033[34mPasta existente.\033[m')
        return True


def Ver(nome):
    arquivo = open(nome, 'r')
    for linha in arquivo:
        palavra = linha.split()
        print(f'{palavra[0]}\nLogin: {palavra[1]}\t\tSenha: {palavra[2]}\n')


def Escrever(nome, a, b, c):
    try:
        arquivo = open(nome, 'at')
        arquivo.write(f'{a}\t\t{b}\t\t\t{c}')
    except:
        print('Erro ao adicionar novo login')
    else:
        print('Dados adicionados')
        Ver(nome)
    finally:
        arquivo.close()
