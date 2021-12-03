"""
Este programa se usó para crear los porgramas en Prolog que dan la solución.
Solución 1: findall(X,cont(X,_,shiny_gold_),Lista), sort(Lista,Sorted), my_length(Sorted,R).
Solucion 2: findall(C,cont(shiny_gold_,C,Y), Lista), my_sum_elements(Lista, R).
"""

def descomponer_norma(norma, file):
    contiene_a = ""
    res = ""
    i = 0
    j = 0
    while norma[i] != "bags":
        contiene_a += norma[i]
        contiene_a += "_"
        i += 1
    i += 2

    while i < len(norma):
        res = "maleta(" + contiene_a
        esta_maleta = "," + norma[i] + ","
        i += 1
        while norma[i][0:3] != "bag":
            esta_maleta += norma[i] + "_"
            i += 1
        res += esta_maleta + ").\n"
        file.write(res)
        i += 1
    return res

def descomponer_normas(normas):
    file = open("Day7_Prolog.pl", "w") #No se que modifique el archivo .pl sin querer
    for i in normas:
        descomponer_norma(i.split(), file)
    file.write("cont(X,C,Y) :- maleta(X,C,Y), not(maleta(X,C,other_)).\n")
    file.write("cont(X,C,Y) :- maleta(X,A,Z), cont(Z,B,Y), C is A * B.\n")
    file.write("my_length([], 0).\n")
    file.write("my_length([_|Xs], L) :- my_length(Xs, L2), L is L2 + 1.\n")
    file.write("my_sum_elements([], 0).\n")
    file.write("my_sum_elements([X|Xs], S) :- my_sum_elements(Xs, S2), S is S2 + X.")
    file.close()

def main():
    address = "./data/day7"
    file = open(address, "r")
    rules = file.read().split("\n")
    file.close()
    descomponer_normas(rules)
