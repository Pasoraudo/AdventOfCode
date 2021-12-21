def parte1(data):
    res = 0
    while len(data) > 3:
        version = int(data[0:3], 2)
        id = int(data[3:6], 2)
        data = data[6:]
        if version == 0:
            break
        data, sumOfVersions = procesPacket(data, version, id)
        res += sumOfVersions
    return res


def procesPacket(data, version, id):
    sumOfVersions = version
    if id == 4:
        num = ''
        while data[0] == '1':
            data = data[1:]
            num += data[0:0 + 5]
            data = data[4:]
        data = data[1:]
        num += data[0:0 + 5]
        data = data[4:]
        print()
    else:
        if data[0] == '0':
            data = data[1:]
            lenghtBlocks = int(data[:15], 2)
            data = data[15:]
            pos = 0
            while pos < lenghtBlocks:
                num = ''
                sumOfVersions += int(data[0:3], 2)
                id = int(data[3:6], 2)
                data = data[6:]
                pos += 6
                while data[0] == '1':
                    data = data[1:]
                    num += data[0:0 + 5]
                    data = data[4:]
                    pos += 5
                data = data[1:]
                num += data[0:0 + 5]
                data = data[4:]
                pos += 5
            print()
        else:
            data = data[1:]
            numBlocks = int(data[0:11], 2)
            data = data[11:]
            for j in range(numBlocks):
                version = int(data[0:3], 2)
                id = int(data[3:6], 2)
                data = data[6:]
                data, aux = procesPacket(data, version, id)
                sumOfVersions += aux
    return data, sumOfVersions

def leerDatos():
    with open("./data/day16", 'r') as f:
        data = bin(int(f.read(), 16))[2:]
    return data

def main():
    data = leerDatos()
    print(data)
    print('Los resultados del dia 16')
    print("Parte 1:", parte1(data))
    #print("Parte 2:", parte2(data))