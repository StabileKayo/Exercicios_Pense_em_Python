#Exercício 1.2


# 3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio
# (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

distancia_km = 10
km_p_milha = 1.61


tempo_min = 42
tempo_seg = 42

#tempo total
total_temp_min = tempo_min +  tempo_seg / 60
total_temp_hor = total_temp_min / 60

#distancia
total_dist_milha = distancia_km / km_p_milha

#passo médio
passo_med = total_temp_min / total_dist_milha 
passo_min = int(passo_med)
passo_seg = int((passo_med - passo_min) * 60)

#velocidade media
vm_hor = total_dist_milha / total_temp_hor

print(f"O passo médio é: {passo_min} min {passo_seg} seg por milha")
print(f"A velocidade média percorrida em {total_dist_milha:.2f} milhas em {total_temp_hor:.2f} horas é: {vm_hor:.2f} milhas/hora")