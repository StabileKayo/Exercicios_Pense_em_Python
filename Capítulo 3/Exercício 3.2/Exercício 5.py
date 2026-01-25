#Exercício 3.2

#5.Defina uma função nova chamada do_four que receba um objeto de função e um valor
# e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só
# duas afirmações no corpo desta função, não quatro.

def do_twice(f,valor):
    f(valor)
    f(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)

def print_twice(texto):
    print(texto)
    
do_four(print_twice, 'spam')