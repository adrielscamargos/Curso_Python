#!/usr/bin/python3
'''Exercicio sobre nota que entra float e retorna conceito
A,A-,B,B-,C,C-,D,D-,E,E-.'''


def nota_conceito(valor):
    nota = float(valor)


    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0.0:
        return 'E-'
    else:
        return 'Nota invalida!'


# Se o nome for == main eu chamo a função
# recebo valor informado a partir do input do usuário
# depois armazeno na variavel conceito o resultado da chamada da função nota_conceito
# passando o valor informado
# imprimir concneito no console

if __name__ == '__main__':
   valor_informado = input('nota do aluno: ')
   conceito = nota_conceito(valor_informado)
   print(conceito)
