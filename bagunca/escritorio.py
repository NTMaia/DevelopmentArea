operador = ''
contador = 0
pacotes = []

classificador_oper = int(input('''
-----------------------
  Quem está operando?
-----------------------
    PRESSIONE
Jacaré        [1]
Victor        [2]
Alexandre     [3]
Edlainovks    [4]
Natan         [5]
Desconhecido  [6]
Sua vez: '''))

contador = classificador_oper
if contador == 1:
    operador = 'Marajá'
elif contador == 2:
    operador = 'Victor'
elif contador == 3:
    operador = 'Alexandre'
elif contador == 4:
    operador = 'Edlainovks'
elif contador == 5:
    operador = 'Natan'
elif contador == 6:
    operador = 'Convidado'


# clear console
import os
os.system('cls' if os.name == 'nt' else 'clear')


print(f'Olá {operador}, seja bem-vindo!')

# informing number of boxes
caixas = int(input('Quantas caixas irá desempacotar? '))

os.system('cls' if os.name == 'nt' else 'clear')

# put program start time
print(f'''Operador: {operador}
Inicio: ... ''')


# filtering HD's
classificador_hd = int(input('''O HD é de PC ou Notebook? 
Pressione:
PC   [1]
NOT  [2]
MIX  [3]
Sua vez: '''))

contador = classificador_hd
if contador == 1:
    tipo_hd = 'Computador'
elif contador == 2:
    tipo_hd = 'Notebook'
elif contador == 3:
    tipo_hd =  'Computador e Notebook'
else:
    print('Não consegui compreender o tipo informado. Tente novamente!')
contador = 0

# Achando uma forma de criar a quantidade informada de caixas dentro da lista "pacotes"
# Estruturas de repeticao disponiveis
# While e For