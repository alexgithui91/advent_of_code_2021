import csv

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

print(positives)
