"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

def menorvalor(numeros):

    menorvalor_num = numeros[0]

    for num in numeros:
        if num < menorvalor_num:
            menorvalor_num = num

    return menorvalor_num


def maiorvalor(numeros):

    maiorvalor_num = numeros[0]

    for num in numeros:
        if num > maiorvalor_num:
            maiorvalor_num = num

    return maiorvalor_num

Vendas= [0,0,0,0,0,0]
ilhas = ["Terceira", "Sao Jorge", "Pico", "Faial", "Graciosa"]


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ilha= input('Insira o nome da ilha')
        pos = ilhas.index(ilha)
        valor1 = int(input('Insire o 1valor'))
        valor2 = int(input('Insire o 2valor'))
        valor3 = int(input('Insire o 3valor'))
        valor4 = int(input('Insire o 4valor'))
        valor5 = int(input('Insire o 5valor'))
        operação = "+"
        total= valor1 + valor2 + valor3 + valor4 + valor5
        average = total /5
        print(f'average: {average}')
        print(f"total : {total}")
        print(f"menor: {menorvalor(Vendas)}")
        print(f"maior: {maiorvalor(Vendas)}")









