from logins.comandos import pasta

# Ao final do programa adicionar a opção de escolher a pasta.
arquivo = '/Users/Natan/Documents/drive/exception.txt'
pasta.ExistePasta(arquivo)
pasta.Ver(arquivo)
chave = str(input('Quer escrever um novo login? ')).upper().strip()
if chave[0] == 'S':
    site = str(input('Site: ')).strip()
    login = str(input('Login: ')).strip()
    senha = str(input('Senha: ')).strip()
    pasta.Escrever(arquivo, site, login, senha)
else:
    pasta.Ver(arquivo)
