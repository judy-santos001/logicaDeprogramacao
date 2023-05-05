#1 Frase na tela - Implemente um programa que escreve na tela a frase "O primeiro programa a gente nunca esquece!".

print('O primeiro programa, a gente nunca esquece ^^')

#2 Etiqueta - Elabore um programa que, após limpar a tela, escreve seu nome completo na primeira linha, seu endereço na segunda, e o CEP e telefone na terceira.

nome= "judy santos"
endereco = "Para"
cep ="68xxx-xxx"
print('nome:',nome)
print('endereço:', endereco)
print("CEP:", cep)

'''3 Mensagem - Escreva uma mensagem para uma pessoa de que goste. Implemente um programa que imprima essa mensagem, e envie-a. '''

print('\"Oi pessoa que eu gosto\nsecretamente...\"')

#- 4 Elabore um programa para produzir na tela a letra X usando a própria.
name = "J"
for x in name:
    
    x = x.upper()
if (x =="J"):
   print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")

# 5 tabela de notas - Escreva um programa que produza a seguinte saída na tela:
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

