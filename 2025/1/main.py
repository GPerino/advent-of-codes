# Lx => -x
# Rx => +x
max_number = 100


def find_password(dial: int):
    password = 0
    lines = open("input.txt", "r").read().splitlines()
    for _, line in enumerate(lines):
        delta = int(line.replace("L", "-").replace("R", ""))
        old_dial = dial
        dial = (dial + delta) % 100
        print(old_dial, delta, dial)
        if dial == 0 :
            password += 1
            # if old_dial == 0:
            #     password -= 1
            print(password)

    return password


def main():
    print(find_password(50))


if __name__ == "__main__":
    main()
