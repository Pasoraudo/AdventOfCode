def operator(data):
    res = 0
    op = ""
    while data:
        elemento = data.pop(0)
        print(data)
        print(res)
        print(elemento)
        if elemento == "+" or elemento == "*":
            op = elemento
        elif elemento[-1] == ")":
            if op == "+":
                res += int(elemento.replace(")", ""))
            elif op == "*":
                res *= int(elemento.replace(")", ""))
            if elemento[-2] == ")":
                data.insert(0, str(res) + ")")
            else:
                data.insert(0, str(res))
            return res
        elif len(elemento) > 1 and elemento[0] == "(":
            data.insert(0, elemento[1:])
            operator(data)
        else:
            if op == "+":
                res += int(elemento)
            elif op == "*":
                res *= int(elemento)
            else:
                res = int(elemento)
    return res

def operator2(data):
    res = 0
    op = ""
    while data:
        elemento = data.pop(0)
        if elemento == "m" or elemento == "*":
            op = elemento
        elif elemento[-1] == ")":
            if op == "m":
                res += int(elemento.replace(")", ""))
            elif op == "*":
                res *= int(elemento.replace(elemento[elemento.index(")")], ""))
            if elemento[-2] == ")":
                data.insert(0, str(res) + ")")
            else:
                data.insert(0, str(res))
            return res
        elif len(elemento) > 1 and elemento[0] == "(":
            data.insert(0, elemento[1:])
            operator2(data)
        else:
            if op == "m":
                res += int(elemento)
            elif op == "*":
                res *= int(elemento)
            else:
                res = int(elemento)
    return res

def main():
    address = "./data/day18"
    file = open(address, "r")
    data = file.read().split("\n")
    file.close()
    res = 0
    for i in data:
        print(i)
        lista = i.split(" ")
        ind = lista.index("+")
        while ind is not None:
            lista[ind - 1] = "(" + lista[ind - 1]
            lista[ind + 1] = lista[ind + 1] + ")"
            lista[ind] = "m"
            try:
                ind = lista.index("+")
            except ValueError:
                ind = None
        print(lista)
        res += operator2(lista)
    print(res)