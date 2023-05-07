#1- Implemente um programa que escreve na tela a frase "O primeiro programa a gente nunca esquece!".

print('O primeiro programa, a gente nunca esquece ^^')

#2 - Elabore um programa que, após limpar a tela, escreve seu nome completo na primeira linha, seu endereço na segunda, e o CEP e telefone na terceira.

nome= "judy santos"
endereco = "Para"
cep ="68xxx-xxx"
print('nome:',nome)
print('endereço:', endereco)
print("CEP:", cep)

# 3 - Escreva uma mensagem para uma pessoa de que goste. Implemente um programa que imprima essa mensagem, e envie-a. '''

print('\"Oi pessoa que eu gosto\nsecretamente...\"')

# 4 -Elabore um programa para produzir na tela a letra X usando a própria.
name = "J"
for x in name:
    
    x = x.upper()
if (x =="J"):
   print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")

# 5-  Escreva um programa que produza a seguinte saída na tela:
'''ALUNO(A) NOTA
======== =====
ALINE 9.0
MÁRIO 10
SÉRGIO 4.5
SHIRLEY 7.0'''
aluno0 ="Aline"
aluno1= "Mário"
aluno2="Sergio"
aluno3 ="Shirley"
def criarTabela():
    print("nome do aluno\t\tnota")
    print("-"*50)
    print("%s:\t\t\t%f" % (aluno0, 9))
    print("%s:\t\t\t%f" % (aluno1, 10))
    print("%s:\t\t\t%f" % (aluno2, 4.5))
    print("%s:\t\t\t%f" % (aluno3, 7))
    print("-"*50)
criarTabela()

# 6 - Um produto  que custa R$ 1200, sofreu um desconto de 5 % , no mês seguinte obteve um acrescimo de 9% .Cacule  seus respectivos vaore apos alterações
# para calcular desconto :valor do produto * (1 -(desconto/100))
# para calcular acrescimo : valor do produto * (1 + (acrescimo/100))

def descontoEacrescimo ():
    valorDoProduto = float(1200)
    desconto= valorDoProduto *(1 - (5/100))
    acrecimo= valorDoProduto *(1 + (9/100))
    print("com o desconto de 5% o produto passou a ser {:.2f}".format(desconto))
    print("com o acrescimo de 9% o produto passou a ser {:.2f}".format(acrecimo))
    
descontoEacrescimo()



# 7 - Calculando o IMC -ÍNDICE DE MASSA CORPORAL
'''< 18- magreza
   > 18- normal
    > 30- obsidade'''
    # imc = peso/(altura)^2
    
peso = float(input("Digite seu peso :"))
altura = float(input("Digite sua altura :"))
imc = peso / (altura**2)
print("Seu IMC é {:.2f}".format(imc))
if imc < 18:
    print('seu imc é de magreza')
elif imc >= 18:
    print("seu imc é normal")
elif imc >30 :
    print('eu imc é de obsesidade')

# 8 - Calculando a area do triangulo
# a = (b*h)/2

base = 5
altura = 6
area = (base * altura) /2
print(f'A area do triangulo é {area}')

# 9 - passando troco

valorProduto = float(input("Insira o valor do  produto :"))
valorQueOclienteTem = float(input("Insira o valor que deseja paga :"))
subtraindo = valorQueOclienteTem -  valorProduto
print("Seu troco : {:.2f}".format(subtraindo))
