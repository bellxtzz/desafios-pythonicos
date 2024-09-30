print("\33[1;35;40mSequência de Sequência!\33[m")
sequencia = []
numero = int(input("Informe um número: "))
x = numero 
if numero<=200:
    if numero==1:
        sequencia.append(numero)
    else:
        total = len(sequencia)*numero
        contador = 0
        while(numero!=0):
            while(numero!=contador):
                sequencia.append(numero)
                contador+=1
            numero=numero-1
            contador = 0
        sequencia.append(0)
    print(f"Caso {x}: {len(sequencia)} números")
    print(sequencia[::-1])