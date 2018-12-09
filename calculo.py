""" Cálculos básicos com Python"""
"""Faça um algoritmo para resolver a equação z = x + y - 4,
 armazenando o resultado na variável z.
 Considere que os valores iniciais de x e y são, respectivamente, 10 e 5.
Depois disso exiba o resultado."""

x = 10
y = 5
z = x + y -4

print(z)
""""Faça um algoritmo para resolver a equação u = a * a - b + c,armazenando
o resultado na variável z. Considere que os valores iniciais de a, b e c são,
respecitvamente, 4, 6.5 e 10.5. Depois disso exiba o resultado."""

a = 4
b = 6.5
c = (10.5)

u= a * a -b + c
print (u)


#Criando um pequeno menu de opções 

# Escolha a opção abaixo

print( "Menu :\n1 =Escreva Guilheme \n2 = Escreva João \n3 = Escreva Luisa \n4 =Escreva Cristina")

opcao = input("Escolha uma opção: ")


if opcao == '1':
    print('Guilherme ')

elif opcao == '2':
    print('João ')

elif opcao == '3':
    print('Luisa ')

elif opcao == '4':
    print('Cristina')
else:
    print( 'Opção inválida - Selecione um número de 1 a 41')

