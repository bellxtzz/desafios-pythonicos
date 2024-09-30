print("\33[1;35;40mMensagem de um Slack de um gerente de hotel!\33[m\n")

print("Seja bem-vinda (o) ao hotel YuZiee!")
print("Para sabermos se há quartos disponíveis, informe a quantidade de quartos ocupados.")
print("Para quartos ocupados, digite: 'S'.")
print("Para quartos vazios, digite: 'N'.\n")

tabela = dict()

andar = 1 
quantidade = []
quartos = 5
quartos_vazios = []

for i in range(quartos):
    ocupado = (input(f"\33[1;35;40mInforme se o quarto {i+1}º está ocupado: \33[m").upper())[0]
    quantidade.append(ocupado)

x = quantidade.count("N")
    
print("\nA quantidade de quartos vazios é: ", x)

print("{:<10}   {:<10}   {:<10}   {:<10}   {:<10}   ".format("\33[1;34;40m1º Quarto:\33[m", "\33[1;35;40m2º Quarto:\33[m" , "\33[1;34;40m3º Quarto:\33[m", "\33[1;35;40m4º Quarto:\33[m", "\33[1;34;40m5º Quarto:\33[m"))
for i,q in enumerate(quantidade):
  print(("{:^10} ".format(q)), end=" ")
print()