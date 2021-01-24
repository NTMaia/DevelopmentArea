def existePasta(nome):
    try:
        pasta = open(nome, 'rt')
        pasta.close()
    except:
        return False
    else:
        print('Pasta existente.')
        return True
