#Exercício 2.2

#3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro)
# e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?


hora_s = 6 
min_s = 52
temp_saida_seg = hora_s * 3600 + min_s * 60

passo1_seg = 8 * 60 + 15
passo2_seg = 7 * 60 + 12

temp_passos = (passo1_seg + 3 * passo2_seg + passo1_seg)

temp_total = temp_passos + temp_saida_seg

hora_final = temp_total // 3600
min_final = (temp_total % 3600) // 60

print(f"Você deve chegar em casa às {hora_final} h {min_final} min")