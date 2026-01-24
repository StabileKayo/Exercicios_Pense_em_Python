#Exercício 3.2

#4.Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
# 'spam' como um argumento.

def print_twice(spam):
    print(spam)
    print(spam)
    
def do_twice(f, valor):
    f(valor)
    f(valor)
do_twice(print_twice, 'spam')