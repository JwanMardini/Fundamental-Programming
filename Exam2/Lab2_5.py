import sys


def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    list_1 = read_file(filename1)
    list_2 = read_file(filename2)
    true = True
    false = False
    odd_numbers = filter_odd_or_even(list_1, true)
    even_numbers = filter_odd_or_even(list_2, false)
    filtred_numbers = odd_numbers + even_numbers
    reversed_bubble_sort(filtred_numbers)


def read_file(filename):
    open_file = open(filename, 'r')
    content = open_file.readlines()
    contentlist = []
    for line in content:
        parts = line.split(' ')
        for numbers in parts:
            numbers = int(numbers)
            contentlist.append(numbers)
    return contentlist


def filter_odd_or_even(numbers, odd):
    list = []
    if odd is True:
        for num in numbers:
            sum = num % 2
            if sum != 0:
                list.append(num)
    elif odd is False:
        for num in numbers:
            sum = num % 2
            if sum == 0:
                list.append(num)
    return list


def reversed_bubble_sort(list):
    for s in range(len(list)):
        for element in range(0, len(list) - 1):
            if list[element] < list[element + 1]:
                switch = list[element]
                list[element] = list[element + 1]
                list[element + 1] = switch
    print(list)


if __name__ == '__main__':
    main()
