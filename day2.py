import csv


def part_one():

    with open("day2_input.csv", newline="") as f:
        reader = csv.reader(f)
        navigation_list = list(reader)

    horizontal = 0
    depth = 0

    for row in navigation_list:
        direction = row[0].split(" ")[0]
        distance = int(row[0].split(" ")[1])

        if direction == "forward":
            horizontal += distance
        if direction == "down":
            depth += distance
        if direction == "up":
            depth -= distance

    print(horizontal * depth)


def part_two():

    with open("day2_input.csv", newline="") as f:
        reader = csv.reader(f)
        navigation_list = list(reader)

    horizontal = 0
    depth = 0
    aim = 0

    for row in navigation_list:
        direction = row[0].split(" ")[0]
        distance = int(row[0].split(" ")[1])

        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        if direction == "down":
            aim += distance
        if direction == "up":
            aim -= distance

    print(horizontal * depth)


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
