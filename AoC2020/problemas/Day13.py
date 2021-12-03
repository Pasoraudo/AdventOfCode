from itertools import count


def best_bus(data):
    timestamp = data[0]
    buses_id = list(data[1].keys())
    wait_time = 1000
    for i in buses_id:
        if wait_time > int(timestamp / i) * i + i - timestamp:
            best = i
            wait_time = int(timestamp / i) * i + i - timestamp
    return best * wait_time


def t_time(data):
    buses = data[1]
    start_idx, steps = 0, 1
    for bus, offset in buses.items():
        for tstamp in count(start_idx, steps):
            if not (tstamp + offset) % bus:
                start_idx = tstamp
                steps *= bus
                break
    return tstamp


def parse_data(my_file):
    data = open(my_file).readlines()
    return int(data[0].strip()), {
        int(bus): idx
        for idx, bus in enumerate(data[1].split(',')) if bus != 'x'
    }


def main():
    address = "./data/day13"
    file = open(address, "r")
    data = parse_data(address)
    file.close()
    problems = {1: best_bus, 2: t_time}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](data))