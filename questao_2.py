def verifica_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

# Número a ser verificado
numero_verificar = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero_verificar):
    print(f"O número {numero_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_verificar} não pertence à sequência de Fibonacci.")