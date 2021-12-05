def parte1(input):
    hPos = 0
    depth = 0
    for i in input:
        if i[0] == 'forward':
            hPos += int(i[1])
        elif i[0] == 'down':
           depth += int(i[1])
        elif i[0] == 'up':
            depth -= int(i[1])
    return hPos * depth

def parte2(input):
    hPos = 0
    depth = 0
    aim = 0
    for i in input:
        x = int(i[1])
        if i[0] == 'forward':
            hPos += x
            depth += aim * x
        elif i[0] == 'down':
            aim += x
        elif i[0] == 'up':
            aim -= x
    return hPos * depth

def main():
    address = "./data/day2"
    file = open(address, "r")
    aux = file.read().split("\n")
    file.close()
    data = []
    for i in aux:
        data.append(i.split())
    print('Los resultados del dia 2')
    print("Parte 1:", parte1(data))
    print("Parte 2:", parte2(data))
