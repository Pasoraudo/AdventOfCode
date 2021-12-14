from collections import Counter


def problemas(data, instrucciones, steps):
    res = Counter(data)
    data = Counter(data[i:i+2] for i in range(len(data) - 1))
    for step in range(steps):
        aux = data.copy()
        for i in data:
            if i in instrucciones.keys() and data[i] > 0:
                num = data[i]
                if instrucciones[i] not in res:
                    res[instrucciones[i]] = 0
                aux[i[:1] + instrucciones[i]] += num
                aux[instrucciones[i] + i[1:]] += num
                aux[i] -= num
                res[instrucciones[i]] += num
        data = aux
    return max(res.values()) - min(res.values())

def leerDatos():
    with open("./data/day14", 'r') as f:
        data = f.read().split('\n\n')
    instrucciones = dict([i.split(' -> ') for i in data[1].split('\n')])
    return data[0], instrucciones

def main():
    data, instrucciones = leerDatos()
    print('Los resultados del dia 14')
    print("Parte 1:", problemas(data, instrucciones, 10))
    print("Parte 2:", problemas(data, instrucciones, 40))
