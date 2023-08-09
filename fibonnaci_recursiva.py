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

def fibonnaci_recursiva(n):
    if n <= 1:
        return n
    else:
        return fibonnaci_recursiva(n-1) + fibonnaci_recursiva(n-2)

n = leia_int_positivo()
print(f"O valor de fibonnaci para esse termo é {fibonnaci_recursiva(n)}")
