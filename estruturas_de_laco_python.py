# Criar pequenas listas para mostrar os elementos contidos nelas

lista_de_fruta = ['banana', 'maça', 'uva', 'abacate', 'laranja', 'limao', 'melao']

for frutas in lista_de_fruta:
    print(frutas)


#Conte a quantidade de frutas na lista lista_de_frutas

contador = 0
for frutas in lista_de_fruta:
    contador +=1
    print(contador)


#Inserindo contagem em lista de números de 0 a 100

lista_numeros = range(0, 100)
for numero in lista_numeros:
    print(numero)

#Inserindo contagem em lista de números de 0 a 100 com intervalo 2

lista_numeros = range(0, 100, 2)
for numero in lista_numeros:
    print(numero)

#Inserindo contagem em lista de números de 0 a 100 com intervalo 5 onde o útimo número seja 100

lista_numeros = range(0, 105, 5)
for numero in lista_numeros:
    print(numero)


#Crie uma estrutura em laco onde x seja exibido na tela equanto for menor que 10
i = 0
while i < 10:
    print('i ainda é menor que 10:', i)
    i = i + 1
