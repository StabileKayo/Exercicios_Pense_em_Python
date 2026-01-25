#Exercício 4.0

#4. Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros
# e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de
# lados adequados. Teste a sua função com uma série de valores de r.

import turtle
import math

t = turtle.Turtle()


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circ = 2 * math.pi * r
    n = int(circ/3) #número de segmentos (lado)
    length = circ/n #comprimento de cada lado
    polygon(t, length, n)

circle(t, 50)
turtle.mainloop()