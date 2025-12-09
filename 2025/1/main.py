def main():
    dial = 50
    count1 = 0
    count2 = 0
    file = open("input.txt", "r")
    for line in file:
        line = line.strip()
        delta = int(line[1:])
        if line[0] == "L":
            old_dial = dial
            dial = dial - delta
        else:
            dial = dial + delta
        if dial == 0:
            count1 = count1 + 1
    file.close()

    print(f"Part 1: {count1}")
    print(f"Part 2: {count2}")


main()
