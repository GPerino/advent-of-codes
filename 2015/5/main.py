from collections import Counter


def get_file_content(file_path: str = "input.txt") -> str:
    with open(file_path, "r") as file:
        return file.read()


def check_double_pair(line: str) -> bool:
    double = []
    for i in range(len(line) - 1):
        double.append(line[i] + line[i + 1])
    count = Counter(double)
    for i in range(len(double) - 1):
        if count[double[i]] >= 2:
            if double[i] != double[i + 1]:
                return True
    return False


def check_contains_repeated_letter(line: str) -> bool:
    return True


def check_character(line: str) -> bool:
    repeated_letter = check_contains_repeated_letter(line)
    double_pair = check_double_pair(line)
    print(repeated_letter, double_pair)
    if double_pair and repeated_letter:
        return True
    return False


def main() -> int:
    nice_string = 0
    content = get_file_content("test.txt").split("\n")
    for line in content:
        result = check_character(line)
        if result:
            nice_string += 1
    print(nice_string)
    return nice_string


if __name__ == "__main__":
    main()
