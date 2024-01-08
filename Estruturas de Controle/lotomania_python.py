#!/usr/bin/python3
#Criação de script com python do curso da Cod3r.com na Udemy 
#para validar numeros escolhidos e sorteados na Lotomania de 1 a 50
#aluno: Adriel Silva Camargos


from random import randint

#Sorteando 50 números de 0 a 99
#numero_preenchido = 1
#minha_cartela = []
#cartela in range (1, 100):
#resultado_sorteio = []

# Criei uma lista indexada com índice começando com 0 ela usa []
#if cartela = int(numero_preenchido)
 #    continue
#	 else:
#	     return 'Número inválido'
		 
# Preenchendo a Cartela	
minha_cartela = [int(input('Preencha sua cartela da Lotomania 1 a 99 com até 50 números')) for i in range (1, 15)] 
print (minha_cartela)
    
#Sorteando 50 números da LOTO
lista = [randint(1,100) for i in range (0, 50)]
texto = "Resultado do Sorteio da Lotomania :"
resultado_sorteio = lista
print(str(texto), resultado_sorteio)  # Saída: "Resultado"
 
		 
#comparando os números iguais na lista para ver resultado do sorteio
for i in lista:
    for j in minha_cartela:
        if i == j:
            acertos =[++i]
            print(acertos)
            len(acertos)
            break
