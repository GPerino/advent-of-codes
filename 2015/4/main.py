import hashlib
from itertools import count


def find_lowest_number_from_secret(content: str) -> int:
    i = 1
    iterator = count(i, 1)
    for i in iterator:
        secret = content + str(i)
        render_string = calculate_hash(secret)
        if render_string.startswith("000000"):
            break
        i += 1
    return i


def calculate_hash(content: str) -> str:
    res = hashlib.md5(content.encode())
    return res.hexdigest()


def main() -> int:
    # secret = "abcdef"
    secret = "pqrstuv"
    # secret = "yzbqklnj"
    number = find_lowest_number_from_secret(secret)
    print(calculate_hash(secret + str(number)))
    print(number)
    return find_lowest_number_from_secret(secret)


if __name__ == "__main__":
    main()
