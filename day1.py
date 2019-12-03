def day1():
    f = open("day1input.txt", "r")
    file = f.readlines()
    total = 0

    for row in file:
        number = int(row)
        number = number // 3 - 2
        fuel = number
        fuelreqs = 0
        while fuel > 6:
            fuel = fuel // 3 - 2
            fuelreqs = fuelreqs + fuel
        total = total + number + fuelreqs
    f.close()
    print("total fuel required:", total)


if __name__ == "__main__":
    day1()
