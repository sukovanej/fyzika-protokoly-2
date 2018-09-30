def load_data(filename):
    f = open(filename)
    result = []

    for line in f.readlines():
        result.append(list(map(float, line.replace("\n", "").split(';'))))

    return result


def mereni1(data):
    f_list = []

    for t in data:
        a = t[0] - 4
        a_ = t[1] - 4

        f_list.append(a * a_ / (a + a_))

    return avg(f_list)


def mereni2(data):
    f_list = []
    y = 5

    for t in data:
        y_ = t[0]
        a = t[1] - 4
        a_ = t[2] - 4 - a

        beta = - y_ / y

        f_list.append(a_ / (1 - beta))

    return avg(f_list)


def mereni3(data):
    f_list = []

    for t in data:
        a1 = t[0]
        a2 = t[1] - 4
        d = t[2] - 4
        a1_ = a2 - a1
        a2_ = d - a2

        delta = abs(a1_) - abs(a2_)

        f_list.append((d * d - delta * delta) / (4 * d))

    return avg(f_list)


def mereni4(data):
    f_list = []

    for t in data:
        A = t[1]
        A_ = t[2]
        R = t[3]

        a = A - R
        a_ = A_ - R

        f_list.append(a * a_ / (a - a_))

    return avg(f_list)


def avg(data):
    result = 0

    for val in data:
        result += val

    return result / len(data)

# simple unittests
assert avg([1, 2, 3]) == 2
assert avg([1, 2, 3, 4, 5]) == 3


data1 = load_data("data1.txt")
data2 = load_data("data2.txt")
data3 = load_data("data3.txt")
data4 = load_data("data4.txt")

print(mereni1(data1))
print(mereni2(data2))
print(mereni3(data3))
print(mereni4(data4))
