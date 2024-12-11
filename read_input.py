def read_day_01(example = False):

    file = f"input/input_01{'_example' if example else ''}.txt"

    arr_1, arr_2 = [], []

    with open(file) as infile:
        for line in infile.readlines():
            numbers = line.split()
            arr_1.append(int(numbers[0]))
            arr_2.append(int(numbers[1]))
    return arr_1, arr_2

def read_day_02(example = False):
    file = f"input/input_02{'_example' if example else ''}.txt"

    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append([int(i) for i in line.split()])
    return data

def read_day_03(example = False):
    file = f"input/input_03{'_example' if example else ''}.txt"
    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append(line)
    return data

def read_day_04(example = False):
    file = f"input/input_04{'_example' if example else ''}.txt"
    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append(line)
    return data


def read_day_05(example = False):
    file = f"input/input_05{'_example' if example else ''}.txt"
    rules, updates = [], []

    with open(file) as infile:
        for l in infile.readlines():
            l = l.strip("\n")
            if "|" in l:
                rules.append(tuple(int(i) for i in l.split("|")))
            elif "," in l:
                updates.append([int(i) for i in l.split(",")])
    return rules, updates

def read_day_06(example = False):
    file = f"input/input_06{'_example' if example else ''}.txt"
    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append(line.strip("\n"))
    return data

def read_day_08(example = False):
    file = f"input/input_08{'_example' if example else ''}.txt"
    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append(line.strip("\n"))
    return data

def read_day_09(example = False):
    file = f"input/input_09{'_example' if example else ''}.txt"
    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append(line.strip("\n"))
    return data[0]

def read_day_10(example = False):
    file = f"input/input_10{'_example' if example else ''}.txt"
    data = []
    with open(file) as infile:
        for line in infile.readlines():
            data.append(line.strip("\n"))
    return data