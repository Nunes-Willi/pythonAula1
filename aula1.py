#Aula de introdução de PYTHON
import math

#TODO 01
# a = float(input("Number one: "))
# b = float(input("Number two: "))

# prod = a * b

# print (round(prod, 2))

#TODO 02
# fahrenheit = float(input("Graus Fahrenheit: "))

# cent = (fahrenheit - 32) * 5/9

# print (round(cent, 2), "Graus centigrados")

#TODO 03
# polegadas = float(input("Quanto choveu: "))

# mili = polegadas * 25.4

# print("Choveu", round(mili, 2), "milímitros")

#TODO 04
# h = float(input("Altura: "))
# d = float(input("Diametro: "))
# r = d / 2
# valorPi = math.pi

# volume = valorPi * r**2 * h

# print(round(volume, 2))

#TODO 05

# nota1 = float(input("Nota: "))
# nota2 = float(input("Nota: "))
# nota3 = float(input("Nota: "))

# media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

# if nota1 > 10 or nota2 > 10 or nota3 > 10:
#     print ("ERROR: Notas maiores que o permitido(Max 10)")
# elif nota1 < 0 or nota2 < 0 or nota3 < 0:
#     print ("ERROR: Notas menores que o permitido(Min 0)")
# elif media >= 6:
#     print(f"\033[32m {f'Média:{round(media, 2)}, Você PASSOU'}")
# else: print(f"\033[31m{f'Média: {round(media, 2)}, Você REPROVOU'}")

#TODO 06

# p1X1 = float(input("Ponto X1: "))
# p1Y1 = float(input("Ponto Y1: "))
# p2X2 = float(input("Ponto X2: "))
# p2Y2 = float(input("Ponto Y2: "))
# distancia = math.sqrt((p2X2 - p1X1)**2 + (p1Y1 - p2Y2)**2)

# print ("Distância é", round(math.sqrt((p2X2 - p1X1)**2 + (p1Y1 - p2Y2)**2, 2)))
# print ("Distância é", round(distancia, 2))

#TODO 07

# a = float(input("Valor de A: "))
# b = float(input("Valor de B: "))
# c = float(input("Valor de C: "))
# d = float(input("Valor de D: "))
# e = float(input("Valor de E: "))
# f = float(input("Valor de F: "))

# valorDeX = (c * e - b * f) / (a * e - b * d)
# valorDeY = (a * f - c * d) / (a * e - b * d)

# print(f"Valor de X é = {round(valorDeX)}; Valor de Y é = {round(valorDeY)}.")

#TODO 08

# preco = float(input("Preço do carro R$: "))
# custo = preco + (preco * 28 / 100 + preco * 45 / 100)

# print (f"O custo total do consumidor foi de {custo} R$")

#TODO 09

# dias = int(input("Idade em dias: "))
# anos = dias // 365
# diasRestantes = dias % 365
# meses = diasRestantes // 30
# dia = dias % 30
# print(f"Vocẽ tem {anos} anos, {meses} meses e {dia} dias")

#TODO 10

# segundos = int(input("Tempo em segundos: "))
# horas = segundos // 3600
# segundosResto = segundos % 3600
# minutos = segundosResto // 60
# segundo = segundosResto % 60

# print(f"O tempo de duração do evento é de {horas} horas, {minutos} minutos e {segundo} segundos")

#TODO 11

# salarioMin = float(input("Valor do Salário Minimo: "))

# casaPrice = salarioMin * 90
# qtdCasas = (1*10**9)  / casaPrice

# print(f"Podem ser construidas {round(qtdCasas)} com 1B R$")

#TODO 12

# salarioBruto = float(input("Coloque seu salário: "))
# ir = salarioBruto * 15 / 100
# inss = salarioBruto * 11 / 100
# sindicato = salarioBruto * 3 / 100

# salarioLiquido = salarioBruto - ir - inss - sindicato
# print (f"IR = {round(ir, 2)} R$; \n INSS {round(inss, 2)} R$; \n Sindicato {round(sindicato, 2)} R$; \n O seu salário liquido é {round(salarioLiquido, 2)} R$;")

#TODO 13

# distanciaKm = float(input("Distância até a casa da irmã: "))
# consumoPorKm = float(input("Consumo do veículo de Maria por Km: "))
# precoGasolina = float(input("Preço do litro da Gasolina: "))

# if precoGasolina == None:
#     precoGasolina = 6.32
# else:
# qtdLitros = distanciaKm / consumoPorKm
# pagarGasolina = qtdLitros * precoGasolina

# print(f"Vai ser necessário {qtdLitros:,.2f} litros que dará {pagarGasolina:,.2f} R$")

#TODO 14

# disLadoA = float(input("Quantia de metros do Lado A: "))
# disLadoB = float(input("Quantia de metros do Lado B: "))
# disLadoC = float(input("Quantia de metros do Lado C: "))
# disLadoD = float(input("Quantia de metros do Lado D: "))
# mourao = float(input("Preço do mourão: "))
# cercaMetro = float(input("Preço do metro do arame: "))

# metrosTerreno = disLadoA + disLadoB + disLadoC + disLadoD
# qtdMourao = metrosTerreno / 3

# precoMourao = qtdMourao * mourao
# precoArame = cercaMetro * metrosTerreno * 4
# precoTotal = precoMourao + precoArame

# print(f"Vai ser preciso {round(qtdMourao)} mourão, o preço total vai ser de {precoTotal:,.2f} R$, sendo {precoMourao:,.2f} R$ do mourão e {precoArame:,.2f} R$ do arame")


#TODO 15

# modelo = input("Modelo do automóvel: ")
# marca = input ("Marca do automóvel: ")
# ano = int(input("Ano do automóvel: "))
# kmInicial = float(input("Kilometragem inicial:"))
# kmFinal = float(input("Kilometragem final:"))
# litroConsumido = float(input("Litros consumidos pelo automóvel: "))
# precoLitro = float(input("Preço por litro: "))

# pagarLitro = litroConsumido * precoLitro
# distanciaPerc = (kmFinal - kmInicial)
# kmLitro = distanciaPerc / litroConsumido

# print(f"Modelo: {modelo}, Marca: {marca}, Ano: {ano}; \n Distância percorrida: {distanciaPerc}; \n Litros de combustivel consumidos: {litroConsumido}; \n Preço por litro: {precoLitro}; \n Total a Pagar: {pagarLitro:,.2f}; \n Km por litro: {kmLitro:.2f}")