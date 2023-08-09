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

def primos_linear(n):
    nao_primo =1
    for i in range(2,n+1):
        for k in range(2,i):
            if i%k==0:
                nao_primo = 0
                break
        if nao_primo:
            primos.append(i)
        nao_primo = 1
    return primos
primos =[]
n = leia_int_positivo()
print(primos_linear(n))