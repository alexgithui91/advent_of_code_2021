import csv


def part_one():
    col1, col2, col3, col4, col5 = [], [], [], [], []

    with open("day3_input.csv", newline="") as f:
        reader = csv.reader(f)
        binary_list = list(reader)

    for itm in binary_list:
        col1.append(int(itm[0][0]))
        col2.append(int(itm[0][1]))
        col3.append(int(itm[0][2]))
        col4.append(int(itm[0][3]))
        col5.append(int(itm[0][4]))

    most_comm_1 = max(set(col1), key=col1.count)
    most_comm_2 = max(set(col2), key=col2.count)
    most_comm_3 = max(set(col3), key=col3.count)
    most_comm_4 = max(set(col4), key=col4.count)
    most_comm_5 = max(set(col5), key=col5.count)

    most_comm_binary = (
        str(most_comm_1)
        + str(most_comm_2)
        + str(most_comm_3)
        + str(most_comm_4)
        + str(most_comm_5)
    )

    most_comm_decimal = int(most_comm_binary, 2)


def part_two():
    pass


def main():
    part_one()
    # part_two()


if __name__ == "__main__":
    main()
