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

def fibonnaci_linear(n):
    proximo = 1
    anterior = 0
    if n <= 1:
        return n
    else:
        while n>1:
            valor = proximo + anterior
            anterior = proximo
            proximo = valor
            n-= 1
    return valor
n = leia_int_positivo()
print(f"O valor de fibonnaci para esse termo é {fibonnaci_linear(n)}")