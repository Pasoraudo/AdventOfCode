def system_1(data):
    memory = {}
    mask = ""
    for i in data:
        if isinstance(i, str):
            mask = i
            continue
        memory[i[0]] = int(masks(mask, bin(i[1])[2:]), 2)
    return sum(memory.values())


def masks(mask, num):
    res = ""
    if len(num) < 36:
        num = '0'*(36 - len(num)) + num
    for i in range(36):
        if mask[i] == '0' or mask[i] == '1':
            res += mask[i]
        else:
            res += num[i]
    return(res)

def system_2(data):
    memory = {}
    mask = ""
    for i in data:
        if isinstance(i, str):
            mask = i
            continue
        addresses = masks2(mask, bin(i[0])[2:])
        for j in addresses:
                memory[j] = i[1]
    return sum(memory.values())


def masks2(mask, num):
    res = [""]
    if len(num) < 36:
        num = '0'*(36 - len(num)) + num
    for i in range(36):
        if mask[i] == '0':
            for j in range(len(res)):
                res[j] += num[i]
        elif mask[i] == '1':
            for j in range(len(res)):
                res[j] += mask[i]
        else:
            aux = res[:]
            for j in range(len(res)):
                res[j] += '0'
                aux[j] += '1'
            res += aux
    return(res)



def main():
    address = "./data/day14"
    file = open(address, "r")
    aux = file.read().splitlines()
    file.close()
    data = []
    for i in aux:
        if 'mask' in i:
            data.append(i[i.find("=") + 2:])
        else:
            data.append((int(i[i.find('[') + 1:i.find(']')]), int(i[i.find('=') + 2:])))
    problems = {1: system_1, 2: system_2}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](data))