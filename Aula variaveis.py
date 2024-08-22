#variaveis

#idade = 50

#a = 10

#_idade = 50

#Idade = 50

#print = 10 causa problemas em demais prints

#10t não começa com letra ou _

variavel = 20


print (variavel *100)

print ("meu carro tem", variavel, "rodas")

print (id(variavel),variavel)

variavel = "texto"

print (id(variavel),variavel,type(variavel))

print (id(variavel),variavel)

variavel = 20.

print (id(variavel),variavel)

var = 1
print(var)

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

#var = 1
#print(Var)


texto = "Matheus"

print("Olá " + texto + ", tudo bem?")

#atribuir um novo valor na variavel (acumulador)

var = 1
print(var)
var = var + 1
print(var)


var = 100
var = 200 + 300
print(var)

#x = x * 2
 
#Solução de problemas matemáticos simples


a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
 

john = 3

mary = 5

adam = 6

print(john , mary, adam, sep=',')

total_apples = john + mary + adam

print (total_apples)

peter = 12.5
suzy = 2
print(peter / suzy)
print("Número total de maçãs:", total_apples)

#Operadores atalhos

#x *= 2
#sheep = sheep + 1
#sheep += 1

#i =10
#i*= 5+10

#print(i)

#i= 10
#i= i * 5 +10

#print(i)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = (miles * 1.61)
kilometers_to_miles = (kilometers / 1.61)

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")


x = 0
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)


#comentarios

"""
Este é um comentario de mais de uma linhas 
aqui é a segunda linha

"""
print("teste")


'''
Este é um comentario de mais de uma linhas 
aqui é a segunda linha

'''
variavel = """
isso é um
grande texto
que pode ser impresso
"""

print("teste")
print(variavel)

print("Conta-me qualquer coisa...")

#utilização de imputs

anything = input()
print("Hum...", anything, "... Realmente?")
 
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")
 
#anything = input("Digite um número: ")
#something = anything ** 2.0
#print(anything, "elevado a 2 é", something)
 
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)


# Testando uma mensagem TypeError.

anything = input("Digite um número: ")
something = anything * 2
print(anything, "elevado a 2 é", something)

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

str(number)

 
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é " + str((leg_a**2 + leg_b**2) ** .5))


x = float(input("Digite o valor para x: "))

y = 1 / (x + 1 /(x + 1 / (x + 1 / x ))) 

print("y =", y)

#calcula horas

hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

# Escreva seu código aqui.

total_minutos = (hour * 60) + mins + dura

hour = total_minutos // 60 % 24

mins = total_minutos % 60


print(hour, mins, sep=':')















