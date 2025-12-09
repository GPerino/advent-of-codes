# Lx => -x
# Rx => +x
max_number = 100


def find_password(dial: int):
    total = dial
    password = 0
    with open('test.txt', "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            n = int(line[1:])
            delta = n if direction == 'R' else -n
            prev = total
            total += delta
            print(prev, total, delta)
            password += abs(total // 100 - prev // 100)
            print("password",password)
        f.close()
    return password


def main():
    password = find_password(50)
    print(password)


if __name__ == "__main__":
    main()
