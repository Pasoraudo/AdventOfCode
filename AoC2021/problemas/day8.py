def parte1(input):
    res = 0
    for line in input:
        for i in line:
            longI = len(i)
            if (longI == 2 or longI == 3 or longI == 4 or longI == 7):
                res += 1
    return res


def parte2(input, output):
    res = 0
    pos = 0
    for line in input:
        aux = {}
        long5 = []
        long6 = []
        for i in line:
            longI = len(i)
            orderedI = ''.join(sorted(i))
            if longI == 2:
                aux['1'] = orderedI
            elif longI == 3:
                aux['7'] = orderedI
            elif longI == 4:
                aux['4'] = orderedI
            elif longI == 7:
                aux['8'] = orderedI
            elif longI == 5:
                long5.append(orderedI)
            else:
                long6.append(orderedI)
        cuatroMenosUno = aux['4']
        for i in aux['1']:
            cuatroMenosUno = cuatroMenosUno.replace(i, '')
        for i in long5:
            if len(i) == len(set(i.join(aux['1']))):
                aux['3'] = i
            elif len(i) == len(set(i.join(cuatroMenosUno))):
                aux['5'] = i
            else:
                aux['2'] = i
        for i in long6:
            if len(i) != len(set(i.join(aux['1']))):
                aux['6'] = i
            elif len(i) == len(set(i.join(aux['4']))):
                aux['9'] = i
            else:
                aux['0'] = i
        code = dict([(v, k) for k, v in aux.items()])
        aux = ''
        for i in output[pos]:
            aux += code[''.join(sorted(i))]
        res += int(aux)
        pos += 1
    return res


"""
    El input debe tener un enter al final, en caso contrario salta un error
"""


def main():
    with open("./data/day8", 'r') as f:
        data = [i[:-1].split(' | ') for i in f.readlines()]
    input = []
    output = []
    for i in data:
        input.append(i[0].split(' '))
        output.append(i[1].split(' '))
    print('Los resultados del dia 8')
    print("Parte 1:", parte1(output))
    print("Parte 2:", parte2(input, output))
