#Exercício 3.3

#1. Escreva uma função que desenhe uma grade como a seguinte:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def vertical():
    print('| ', ' ' * 8, '| ', ' ' * 8, '|')

def bloco_ver():
    vertical()
    vertical()
    vertical()
    vertical()

def horizontal():
    print('+ ', '- ' * 4, '+ ', '- ' * 4, '+' )

horizontal()
bloco_ver()
horizontal()
bloco_ver()
horizontal()