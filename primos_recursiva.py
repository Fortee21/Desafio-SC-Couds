def leia_int_positivo():
    while True:
        try:
            valor = int(input("Qual o termo voce quer calcular?"))
            if valor >= 0:
                return valor
            else:
                print("Digite um número inteiro positivo válido.")
        except ValueError:
            print("Digite um número inteiro positivo válido.")

def primos_recursiva(n):

    div = 2
    if n == 1:
        primos.sort()
        return primos
    while div < n:
        if n%div==0:
            return primos_recursiva(n-1)
        div+=1
    primos.append(n)

    return primos_recursiva(n-1)
primos =[]
n = leia_int_positivo()
print(primos_recursiva(n))
