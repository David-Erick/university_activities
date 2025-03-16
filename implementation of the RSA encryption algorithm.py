#Aluno: David Erick Araujo Ferraz
import random


# Algoritmo de Euclides para calcular o MDC
def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

# Teste de primalidade usando o Pequeno Teorema de Fermat
def eh_primo(p, testes=40):
    if p < 2:
        return False
    for i in range(testes):
        a = random.randint(2, p - 1)
        if mdc(a, p) != 1:
            return False
        if pow(a, p - 1, p) != 1:
            return False
    return True

# Geração de um número primo grande
def gerar_primo():
    while True:
        p = random.randint(10**9, 10**10)  # Número grande com 10 dígitos
        if eh_primo(p):
            return p


# Algoritmo Euclidiano Estendido para encontrar 'd'
def euclides_estendido(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = euclides_estendido(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Geração das chaves RSA
def gerar_chaves():
    p = gerar_primo()
    q = gerar_primo()
    n = p * q
    f = (p - 1) * (q - 1)
    
    e = random.randint(100, n)
    while mdc(e, f) != 1:
        e = random.randint(100, n)
    
    i, d, i = euclides_estendido(e, f)
    d = d % f  # Garantir que d seja positivo
    
    return (e, n), (d, n)

# Cifrar mensagem com RSA
def cifrar(m, chave_publica):
    e, n = chave_publica
    return pow(m, e, n)

# Decifrar mensagem com RSA
def decifrar(c, chave_privada):
    d, n = chave_privada
    return pow(c, d, n)

# Exemplo de uso:
chave_publica, chave_privada = gerar_chaves()
M = random.randint(1, chave_publica[1])  # Mensagem como número
cifrado = cifrar(M, chave_publica)
decifrado = decifrar(cifrado, chave_privada)

print("Mensagem original:", M)
print("Mensagem cifrada:", cifrado)
print("Mensagem decifrada:", decifrado)
