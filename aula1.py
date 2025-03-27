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

nota1 = float(input("Nota: "))
nota2 = float(input("Nota: "))
nota3 = float(input("Nota: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

if nota1 > 10 or nota2 > 10 or nota3 > 10:
    print ("ERROR: Notas maiores que o permitido(Max 10)")
elif nota1 < 0 or nota2 < 0 or nota3 < 0:
    print ("ERROR: Notas menores que o permitido(Min 0)")
else: print("Média: ", round(media, 2))