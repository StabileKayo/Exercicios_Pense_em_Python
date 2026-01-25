#Exercício 3.3

# 2. Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.

def vertical():
    print('| ', ' ' * 8, '| ', ' ' * 8, '| ', ' ' * 8, '|')

def bloco_vertical():
    vertical()
    vertical()
    vertical()
    vertical()

def horizontal():
    print('+ ', '- ' * 4, '+ ', '- ' * 4, '+ ', '- ' * 4, '+' )

def grade():
    horizontal()
    bloco_vertical()
    horizontal()
    bloco_vertical()
    horizontal()
    bloco_vertical()
    horizontal()
    bloco_vertical()
    horizontal()

grade()