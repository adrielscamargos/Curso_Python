#!/usr/bin/python3
#Programação funcional com python do curso da Cod3r.com na Udemy
#aluno: Adriel Silva Camargos

#from math import pi

def executar(função):
    função()

def bom_dia():
    print ('Bom dia!')
		
def boa_tarde():
    print ('Boa Tarde!')


if __name__== "__main__":
    executar(bom_dia)
    executar(boa_tarde)
	
