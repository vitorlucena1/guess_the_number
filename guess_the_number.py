import random
from sympy import isprime

def intervalo(numero_aleatorio):
    dezenas = numero_aleatorio // 10 * 10
    intervalo_minimo = dezenas
    intervalo_maximo = dezenas + 10
    return f"O número sorteado está entre {intervalo_minimo} e {intervalo_maximo}"


dificuldade = input("Digite a dificuldade: Fácil, Médio ou Difícil: ")

if dificuldade.lower() in ["fácil", "facil"]:
    numero_aleatorio = random.randint(0, 100)
    while True:
        chute = int(input("Digite o número: "))
        if(chute == numero_aleatorio):
            print("Acertou! Parabéns!!")
            break
        else:
            if(isprime(numero_aleatorio)):
                print("Dica: O número sorteado é primo!")
            if(numero_aleatorio % 2 == 0):
                print("Dica: O número é par!")
            else:
                print("Dica: O número é ímpar!")

            print(intervalo(numero_aleatorio) + "\nTente novamente!")

if dificuldade.lower() in ["médio", "medio"]:
    print("Digite dois intervalos de números para adivinhar (Exemplo: 0 100): ")
    inicio, fim = map(int, input().split())
    numero_aleatorio = random.randint(inicio, fim)
    while True:
        chute = int(input("Digite o número: "))
        if(chute == numero_aleatorio):
            print("Acertou! Parabéns!!")
            break
        else:
            if(isprime(numero_aleatorio)):
                print("Dica: O número sorteado é primo!")
            if(numero_aleatorio % 2 == 0):
                print("Dica: O número é par!")
            else:
                print("Dica: O número é ímpar!")
            if(chute<numero_aleatorio):
                print("Dica: O número sorteado é maior")
            else:
                print("Dica: O número sorteado é menor")
        print("Tente novamente!")

if dificuldade.lower() in ["difícil", "dificil"]:
    numero_aleatorio = random.randint(0, 20)
    print("Você tem 5 tentativas para acertar o número. Boa sorte!")
    for i in range(5):
            chute = int(input("Tentativa " + str((i+1)) +"\nDigite o número: "))
            if(chute == numero_aleatorio):
                print("Acertou! Parabéns!!")
                break
            else:
                if(i+1==5):
                    print("Infelizmente você não acertou. O número sorteado era " + str(numero_aleatorio) + ".")
                    break
                else:
                    if(chute>numero_aleatorio):
                        print("O número sorteado é menor")
                    else:
                        print("O número sorteado é maior")
            print("Tente novamente!")
