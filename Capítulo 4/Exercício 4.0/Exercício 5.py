#Exercício 4.0

#5.	Faça uma versão mais geral do circle chamada arc, que receba um parâmetro
# adicional de angle, para determinar qual fração do círculo deve ser desenhada.
# angle está em unidades de graus, então quando angle=360, o arc deve desenhar
# um círculo completo.

import turtle
import math

t = turtle.Turtle()

def arc(t, r, angle):
    circ = 2 * math.pi * r
    n = int(circ/3) #número de segmentos (lado)
    arc_length = circ * angle / 360 # comprimento do arco
    length = arc_length/n #comprimento de cada lado
    
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

arc(t, 50, 160)
turtle.mainloop()