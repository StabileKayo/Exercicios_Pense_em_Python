#Exercício 4.0

# 3. Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro 
# chamado n e altere o corpo para que desenhe um polígono regular de n lados.

import turtle
t = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(t, 100, 8)
turtle.mainloop()