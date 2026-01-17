#Exercício 2.2

#2.	Suponha que o preço de capa de um livro seja R$24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$3,00 para o primeiro exemplar e 75 centavos
# para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

#valor livro
valor_livro = 24.95
desconto_livro = 24.95 * 0.60
quant_livros = 60
total_valor_livro = desconto_livro * quant_livros

transporte = 3.00 + (0.75 * (quant_livros - 1))
total = transporte + total_valor_livro 

print(f"o custo total de atacado para {quant_livros} cópias é de: R$ {total:.2f}")