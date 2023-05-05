
//1 Frase na tela - Implemente um programa que escreve na tela a frase "O primeiro programa a gente nunca esquece!".
console.log("O primeiro programa, a gente nunca esquece !")

//2 Etiqueta - Elabore um programa que, após limpar a tela, escreve seu nome completo na primeira linha, seu endereço na segunda, e o CEP e telefone na terceira.
//console.clear();
console.log("Judy santos\nPara\n68xxx-xxx")

//3 Mensagem - Escreva uma mensagem para uma pessoa de que goste. Implemente um programa que imprima essa mensagem, e envie-a. 
console.log("\'Olá pessoa que gosto secretamente\'")

//4 Elabore um programa para produzir na tela a letra X usando a própria




  /* 5 tabela de notas - Escreva um programa que produza a seguinte saída na tela:
ALUNO(A) NOTA
======== =====
ALINE 9.0
MÁRIO DEZ
SÉRGIO 4.5
SHIRLEY 7.0
*/
function BoletimEscolar (aluno, nota){
    this.aluno = aluno
    this.nota = nota
}
const aluno1 = new BoletimEscolar("Aline", 9)
const aluno2 = new BoletimEscolar("Mario", 6)
const aluno3 = new BoletimEscolar("Sérgio", 6)
const aluno4 = new BoletimEscolar("Shirley", 6)

console.table([aluno1, aluno2, aluno3, aluno4])
