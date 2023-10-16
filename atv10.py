# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km= int (input ("Digite a velocidade em km: "))
n1= 60
multa= km * 420
if km <= n1 :
    print ("limite de velocidade respeitado")
else :
    print (f"limite de velocidade nao respeitado, multa de {multa} ")