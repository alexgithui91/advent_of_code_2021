import csv


def part_one():
    with open("day1_input.csv", newline="") as f:
        reader = csv.reader(f)
        measurements_list = list(reader)

    positives = 0

    for itr in range(len(measurements_list)):
        if itr == 0:
            # print("N/A - no previous measurement")
            pass
        else:
            val1 = int(measurements_list[itr][0])
            val2 = int(measurements_list[itr - 1][0])
            diff = val1 - val2
            if diff > 0:
                positives += 1

    return positives


def part_two():
    with open("day1_input.csv", newline="") as f:
        reader = csv.reader(f)
        initial_list = list(reader)

    cleaner_list = []

    for itm in initial_list:
        cleaner_list.append(itm[0])

    min_num = 0
    max_num = len(cleaner_list)
    measurements_list = []
    positives = 0

    for itr in range(min_num, max_num):
        x = itr
        y = itr + 1
        z = itr + 2

        if z == len(cleaner_list) - 1:
            total = (
                int(cleaner_list[x])
                + int(cleaner_list[y])
                + int(cleaner_list[z])
            )
            measurements_list.append(total)
            break
        else:
            total = (
                int(cleaner_list[x])
                + int(cleaner_list[y])
                + int(cleaner_list[z])
            )
            measurements_list.append(total)

    for itr in range(len(measurements_list)):
        if itr == 0:
            # print("N/A - no previous measurement")
            pass
        else:
            val1 = int(measurements_list[itr])
            val2 = int(measurements_list[itr - 1])
            diff = val1 - val2
            if diff > 0:
                positives += 1

    return positives


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
