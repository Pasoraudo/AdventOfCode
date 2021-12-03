def count_wrong_tickets(fields, my_ticket, nearby_tickets):
    all_tickets = []
    all_fields = []
    cont = 0
    for i in nearby_tickets:
        all_tickets += i
    for i, j in fields.values():
        all_fields += i
        all_fields += j
    for i in all_tickets:
        if i not in all_fields:
            cont += i
    return cont

def remove_wrong_tickets(fields, nearby_tickets):
    aux_tickets = nearby_tickets[:]
    all_fields = []
    for i, j in fields.values():
        all_fields += i
        all_fields += j
    for i in aux_tickets:
        for j in i:
            if j not in all_fields:
                nearby_tickets.remove(i)

def work_tickets(fields, my_ticket, nearby_tickets):
    remove_wrong_tickets(fields, nearby_tickets)
    nearby_tickets += [my_ticket]
    res = []
    j = 0
    while j < len(nearby_tickets[0]):
        aux = list(fields.keys())
        for i in nearby_tickets:
            for t in fields:
                if t in aux and (i[j] not in list(fields[t][0]) and i[j] not in list(fields[t][1])):
                    aux.remove(t)
        res += [aux]
        j += 1
    print(res)
    index = 1
    f = {}
    while index < len(res):
        for i in res:
            if len(i) == index:
                for j in i:
                    if j not in f.values():
                        f[res.index(i)] = j
                        index += 1
    s = {}
    for i in range(len(my_ticket)):
        if f[i][0:9] == "departure":
            print(f[i], i, my_ticket[i])
    return f



def main():
    address = "./data/day16"
    file = open(address, "r")
    data = file.read().split("\n\n")
    file.close()
    fields = {}
    for i in data[0].split('\n'):
        key = i[:i.index(':')].replace(' ', '_')
        aux = i[i.index(':'):].split()
        value = (range(int(aux[1].split('-')[0]), int(aux[1].split('-')[1]) + 1), range(int(aux[3].split('-')[0]), int(aux[3].split('-')[1]) + 1))
        fields[key] = value
    my_ticket = [*map(int, data[1].split('\n')[1].split(','))]
    nearby_tickets = []
    for i in data[2].split('\n')[1:]:
        nearby_tickets += [[*map(int, i.split(','))]]
    problems = {1: count_wrong_tickets, 2: work_tickets}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](fields, my_ticket, nearby_tickets))