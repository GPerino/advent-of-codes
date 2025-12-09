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
        print(delta, dial)
        if dial > 99:
            count2 += dial // 100
        if dial < 1:
            count2 += ((old_dial - 1) // 100) - ((dial - 1) // 100)
        dial = dial % 100
        print(count2)
        if dial == 0:
            count1 = count1 + 1
    file.close()

    print(f"Part 1: {count1}")
    print(f"Part 2: {count2}")


main()
