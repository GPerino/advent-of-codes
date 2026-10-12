class Santa:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


def define_next_coordinates(direction: str):
    x = 0
    y = 0
    if direction == "^":
        y += 1
    if direction == ">":
        x += 1
    if direction == "v":
        y -= 1
    if direction == "<":
        x -= 1
    return x, y


def get_file_content(file_path: str = "input.txt"):
    with open(file_path, "r") as file:
        return file.read()


def main():
    define_directions()


if __name__ == "__main__":
    main()
