import csv


def part_one():
    most_comm_binary = ""
    least_comm_binary = ""

    with open("day3_input.csv", newline="") as f:
        reader = csv.reader(f)
        tmp_list = list(reader)

    binary_list = [[] for i in range(len(tmp_list[0][0]))]

    for lst_cnt in range(len(binary_list)):
        for itm in tmp_list:
            binary_list[lst_cnt].append(int(itm[0][lst_cnt]))

    for lst_itm in binary_list:
        most_comm_binary += str(max(set(lst_itm), key=lst_itm.count))
        least_comm_binary += str(min(set(lst_itm), key=lst_itm.count))

    print(int(most_comm_binary, 2) * int(least_comm_binary, 2))


def part_two():
    with open("day3_input.csv", newline="") as f:
        reader = csv.reader(f)
        org_list = list(reader)


def main():
    # part_one()
    part_two()


if __name__ == "__main__":
    main()
