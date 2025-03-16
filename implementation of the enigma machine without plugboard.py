#Aluno : David Erick Araujo Ferraz

#Mesmo codigo para decifrar e cifrar.
#A mensagem já é considerada como limpa(só o alfabeto e tudo minusculo).

# Definição dos cinco rotores disponíveis (exemplo simplificado)
ROTORES = [
    "ekmflgdqvzntowyhxuspaibrcj",  # Rotor I
    "ajdksiruxblhwtmcqgznpyfvoe",  # Rotor II
    "bdfhjlcprtxvznyeiwgakmusqo",  # Rotor III
    "esovpzjayquirhxlnftgkdcmwb",  # Rotor IV
    "vzbrgityupsdnhlxawmjqofeck"   # Rotor V
]

# Refletor fixo (exemplo simplificado)
REFLETOR = "yruhqsldpxngokmiebfzcwvjat"

ALFABETO ="abcdefghijklmnopqrstuvwxyz"

def configurar_rotores(indices_rotores, posicoes_iniciais):
    rotores = [ROTORES[i] for i in indices_rotores]
    deslocamentos = posicoes_iniciais[:]
    return rotores, deslocamentos

def avancar_rotores(deslocamentos):
    deslocamentos[0] = (deslocamentos[0] + 1) % 26  # Primeiro rotor sempre avança
    if deslocamentos[0] == 0:  # Se completou uma volta, o segundo rotor avança
        deslocamentos[1] = (deslocamentos[1] + 1) % 26
        if deslocamentos[1] == 0:  # Se o segundo completar uma volta, o terceiro avança
            deslocamentos[2] = (deslocamentos[2] + 1) % 26

def enigma_cifrar(mensagem, rotores, deslocamentos):
    mensagem = mensagem.lower()
    resultado = ""
    
    for letra in mensagem:
        if letra not in ALFABETO:
            continue
        
        # Passa pelos rotores na ordem direta
        for i in range(3):
            indice = (ALFABETO.index(letra) + deslocamentos[i]) % 26
            letra = rotores[i][indice]
        
        # Passa pelo refletor
        letra = REFLETOR[ALFABETO.index(letra)]
        
        # Passa pelos rotores na ordem inversa
        for i in range(2, -1, -1):
            indice = rotores[i].index(letra)
            letra = ALFABETO[(indice - deslocamentos[i]) % 26]
        
        resultado += letra
        
        # Avança os rotores corretamente
        avancar_rotores(deslocamentos)
    
    return resultado

# Exemplo de uso:
indices_rotores = [0, 1, 2]  # Escolhendo os rotores I, II e III
posicoes_iniciais = [1, 5, 10]  # Posições iniciais de cada rotor

# Carregar a mensagem de um arquivo txt
with open("mensagem.txt", "r") as arquivo:
    mensagem = arquivo.read().strip()

# Verificar se a mensagem contém apenas letras minúsculas sem espaços
if not mensagem.isalpha() or not mensagem.islower():
    print("Usuário reprovado: A mensagem deve conter apenas letras maiúsculas sem espaços ou caracteres especiais.")
    exit()

# Configuração da máquina
rotores, deslocamentos = configurar_rotores(indices_rotores, posicoes_iniciais)

# Cifrar a mensagem
texto_cifrado = enigma_cifrar(mensagem, rotores, deslocamentos)
print("Texto cifrado:", texto_cifrado)
