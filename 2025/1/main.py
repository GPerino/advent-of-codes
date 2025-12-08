# Lx => -x
# Rx => +x

max_number = 100


def get_file_lines(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


def count_rotation(x: int):
    rotations = 0
    lines = get_file_lines("input.txt")
    for _, line in enumerate(lines):
        line = line[:1], line[1:]
        if line[0] == "L":
            x = (x - int(line[1])) % max_number
        else:
            x = (x + int(line[1])) % max_number

        if x == 0:
            rotations += 1
    return rotations


def main():
    x = 50
    print(count_rotation(x))


if __name__ == "__main__":
    main()
