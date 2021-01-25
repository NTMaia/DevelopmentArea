from time import sleep
from logins.comandos import pasta


def Cabecalho(txt):
    tamanho = len(txt) + 14
    print('-'*tamanho)
    print(txt.center(tamanho))
    print('-'*tamanho)


def Menu(nome):
    Cabecalho('MENU DE OPÇÕES v1.0')
    print('''1 | Validação do arquivo
2 | Criar pasta no diretorio
3 | Ler arquivo 
4 | Editar o arquivo
5 | Sair''')

    try:
        acao = int(input('Sua opção: '))
    except:
        print('ERRO: Digite um valor válido.')
    else:
        while True:
            if acao == 1:
                pasta.Existe(nome)
                sleep(1.5)
                return Menu(nome)
            elif acao == 2:
                if pasta.Existe(nome):
                    print('\033[31mATENÇÃO! Você está prestes a criar um arquivo que já existe.\033[m')
                pasta.CriarArquivo(nome)
                return Menu(nome)
            elif acao == 3:
                pasta.Ver(nome)
                return Menu(nome)
            elif acao == 4:
                site = str(input('Site: ')).strip()
                login = str(input('Login: ')).strip()
                senha = str(input('Senha: ')).strip()
                pasta.Escrever(nome, site, login, senha)
                return Menu(nome)
            elif acao == 5:
                print('Finalizando...')
                sleep(0.2)
                break
            else:
                print('Tente uma das opções oferecidas!')
                sleep(1.5)
                return Menu(nome)