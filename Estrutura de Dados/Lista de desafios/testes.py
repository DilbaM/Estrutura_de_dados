import time
def soma1(n):
    soma = 0
    for i in range(10 + 1):
        soma = soma + i
    return soma


def soma2(n):
    return (n * (n + 1)) / 2

print(soma1(10))
print(soma2(10))

#Calculando o tempo de execução

inicio=time.time()
resultado=soma1(100000)
termino=time.time()
resultado_time = termino - inicio
print(f'O resultado foi de ..: {resultado}')
print(f'O tempo de inicio...: {inicio:.5f} segundos')
print(f'O tempo de termino...: {termino:.5f} segundos')
print(f'O tempo total foi de...: {resultado_time:.5f} segundos')
      