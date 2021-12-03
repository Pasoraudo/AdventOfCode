import re


def check_passports(m):
    cont = 0
    for i in m:
        if complete_passport(i):
            cont += 1
    return cont


def strong_check_passports(passports):
    cont = 0
    checks = {0: check_byr, 1: check_ecl, 2: check_eyr, 3: check_hcl,
              4: check_hgt, 5: check_iyr, 6: check_pid}
    for i in passports:
        ord_pass = sorted(i.split())
        if len(ord_pass) == 8:
            ord_pass.pop(1)
        if not complete_passport(i):
            continue
        valid = True
        j = 0
        while valid and j < 7:
            if not checks[j](ord_pass[j]):
                valid = False
            j += 1
        if valid:
            cont += 1
    return cont


def complete_passport(passport):
    return len(passport.split()) == 8 or (len(passport.split()) == 7 and not ("cid" in passport))


def check_byr(byr):
    return 1920 <= int(byr[4:8]) <= 2002


def check_iyr(iyr):
    return 2010 <= int(iyr[4:8]) <= 2020


def check_eyr(eyr):
    return 2020 <= int(eyr[4:8]) <= 2030


def check_hgt(hgt):
    if hgt[-2:] == "cm":
        return 150 <= int(hgt[4:-2]) <= 193
    elif hgt[-2:] == "in":
        return 59 <= int(hgt[4:-2]) <= 76


def check_hcl(hcl):
    if hcl[4] == "#":
        if re.search('[0-9a-f]', hcl[5:11]):
            return True
    return False


def check_pid(pid):
    return len(pid) == 13


def check_ecl(ecl):
    return ecl[4:7] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def main():
    address = "./data/day4"
    file = open(address, "r")
    passports = file.read().split("\n\n")
    file.close()
    problems = {1: check_passports, 2: strong_check_passports}
    prob = int(input("¿Problema 1 o 2?\n"))
    print("El resultado es: ", problems[prob](passports))
