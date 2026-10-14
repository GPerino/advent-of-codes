def get_file_content(file_path: str = "input.txt") -> str:
    with open(file_path, "r") as file:
        return file.read()


def check_vowels_in_line(line: str) -> bool:
    v = "aeiou"
    vowels = [ch for ch in line if ch in v]
    if len(vowels) >= 3:
        return True
    else:
        return False


def check_double_letter(line: str) -> bool:
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            return True
    return False


def check_not_contains_prohibited_string(line: str) -> bool:
    string_to_avoid = ["ab", "cd", "pq", "xy"]
    res = [ele for ele in string_to_avoid if (ele in line)]
    if len(res) >= 1:
        return False
    else:
        return True


def check_character(line: str) -> bool:
    prohibited_string = check_not_contains_prohibited_string(line)
    vowels = check_vowels_in_line(line)
    double_letter = check_double_letter(line)
    if double_letter and vowels and prohibited_string:
        return True
    else:
        return False


def main() -> int:
    nice_string = 0
    content = get_file_content("input.txt").split("\n")
    for line in content:
        result = check_character(line)
        if result:
            nice_string += 1
    print(nice_string)
    return nice_string


if __name__ == "__main__":
    main()
