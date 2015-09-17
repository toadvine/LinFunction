__author__ = 'benjamin_sanchez'


def main():
    counter = int(input())
    for x in range(counter):
        value = [int(x) for x in input().split()]
        x_shift = (value[2] - value[0])
        y_shift = (value[3] - value[1])
        x_val = int(y_shift / x_shift)
        y_val = -int(x_val * value[0] - value[1])
        print("(" + str(x_val) + " " + str(y_val) + ")", end=" ")

main()
