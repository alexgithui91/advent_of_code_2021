import csv

# def most_frequent(List):
#     return max(set(List), key=List.count)


# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))


def part_one():
    with open("day3_input.csv", newline="") as f:
        reader = csv.reader(f)
        binary_list = list(reader)
    print(bi)


def part_two():
    pass


def main():
    part_one()
    # part_two()


if __name__ == "__main__":
    main()
