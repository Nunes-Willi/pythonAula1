#Atividade extra Challenge
#TODO 01
# lado = float(input("Coloca o lado: "))
# altura = float(input("Coloca a altura: "))
# if lado == altura:
#     print (f' RED LINE A area é:{lado ** 2} \n O perimetro é: {lado + lado + altura + altura}')
# else: print(f' A area é:{lado * altura} \n O perimetro é: {lado * 2 + altura * 2}')

#TODO 02
nome = input("Qual seu nome: ")
qtdFilhos = int(input("Quantia de filhos: "))

if qtdFilhos <= 0:
    print("Você não tem Filhos")
else: print (f"{nome} Tem {qtdFilhos} filho(s/a/as)")


# if qtdFilhos <= 0:
#     print("Você não tem Filhos")
# elif qtdFilhos == 1:
#     filho = input("Qual o nome do seu filho(a)")
#     print (f"{nome} Tem {qtdFilhos} filho(a) de nome {filho}")
# elif qtdFilhos > 1:
#     # qtd = qtdFilhos
#     while qtdFilhos:
#         filhos = input("Qual os nomes do seus filho(s/a/as)")
#         if len(filhos) == qtdFilhos:
#             print(f"{filhos}")