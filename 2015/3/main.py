# B(xB,yB)=(xA+xAB,yA+yAB),où xAB et yAB sont les coordonnées du vecteur.

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


def discover(content: str):
    santa_position = (0, 0)
    bot_position = (0, 0)
    positions = [santa_position]
    for character in content:
        x, y = define_next_coordinates(character)
        santa_position = (santa_position[0] + x, santa_position[1] + y)
        bot_position = (bot_position[0] + x, bot_position[1] + y)
        positions.append(santa_position)
    return len(set(positions))


def main():
    content = get_file_content()
    print(discover(content))
    return discover(content)


if __name__ == "__main__":
    main()
