#Exercício 3.2

#2.Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e
# chame a função duas vezes, passando o valor como um argumento.
def do_twice(f, valor):
    f(valor)
    f(valor)
def print_spam(texto):
    print(texto)
do_twice(print_spam, 'spam')
