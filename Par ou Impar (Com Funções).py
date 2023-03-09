
def multiplicador(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

def par_ou_impar(numero):
    par = numero % 2 == 0
    impar = numero % 2 != 0

    if par:
        print("O número é par")
        return par
    else:
        print("O numero é impar")
        return impar

multiplicacao1 = multiplicador(5, 10)

print(multiplicacao1)
par_ou_impar(multiplicacao1)
