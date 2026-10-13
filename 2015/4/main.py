import hashlib


def find_lowest_number_from_secret(content: str) -> int:
    i = 0
    while i < 10000000:
        secret = content + str(i)
        render_string = calculate_hash(secret)
        if render_string.startswith("00000"):
            break
        else:
            i += 1
    return i


def calculate_hash(content: str) -> str:
    res = hashlib.md5(content.encode())
    return res.hexdigest()


def main() -> int:
    # secret = "pqrstuv"
    secret = "yzbqklnj"
    number = find_lowest_number_from_secret(secret)
    print(calculate_hash(secret + str(number)))
    print(number)
    return find_lowest_number_from_secret(secret)


if __name__ == "__main__":
    main()
