from logins.comandos import pasta, menu

menu.Cabecalho('Informe a pasta a ser manipulada')
diretorio = str(input('Diretorio: ')).strip()  # 'C:/Users/Natan/Documents/drive/exception.txt'
menu.Menu(diretorio)
