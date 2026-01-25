#Exercício 4.0

# 1. Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle.
# Ela deve usar o turtle para desenhar um quadrado. 
# Escreva uma chamada de função que passe bob como um argumento para o square
# e então execute o programa novamente.

import turtle
t = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(t)
turtle.mainloop()