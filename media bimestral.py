#Levantamento de dados do usuário;

print("Programa de cálculo de média bimestral \n")

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

#Cálculos do programa

nota = nota1+nota2

media = nota/2

print("A média correspondente é:", media )

if media >= 5:
    print("Aluno aprovado!")

if media < 5:
    print("Aluno reprovado!")

print("Obrigado por usar este programa!")
print("Desenvolvido por RDA Sol. T.I.")




