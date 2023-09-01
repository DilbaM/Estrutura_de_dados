numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]
maior_valor = max(numeros)
menor_valor = min(numeros)
print("O maior valor da lista é:", maior_valor)
print("O menor valor da lista é:", menor_valor)
