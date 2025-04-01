import random

entrada = input ("Deseja gerar um cpf?").upper

def gerarcpf():
    pronto = random.randint (0,9)
    print(pronto)

if entrada=="S":
    
    gerarcpf()
        