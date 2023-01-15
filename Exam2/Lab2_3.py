import sys


def main():
    try:
        filename = sys.argv[1]
    except FileNotFoundError:
        print('An error occurred while trying to read the file.')
    else:
        list = read_lines(filename)
        print()
        distance = float(input('How far do you want to drive (kilometers)? '))
        print()
        list_with_tubles = parse_cars(list)
        calculate = calculate_percentage(distance, list_with_tubles)
        display_result(calculate)


def read_lines(filename):
    open_file = open(filename, 'r')
    content = open_file.readlines()
    contentlist = []
    for line in content:
        contentlist.append(line.rstrip('\n'))
    return contentlist


def parse_cars(listan):
    new_list = []
    for element in listan:
        parts = element.split(':')
        car_model = parts[0]
        max_range = int(parts[1])
        new_list.append((car_model, max_range))
    return new_list


def calculate_percentage(distance, cars):
    new_list = []
    for element in cars:
        car = element[(0)]
        max_range = element[(1)]
        precenteg_value = float(distance / max_range * 100)
        new_list.append((car, precenteg_value))
    return new_list


def display_result(percentages):
    print('To drive the specified distance would correspond to this many\n')
    print('percent of each cars specified max range.')
    for element in percentages:
        car = element[(0)]
        precent_value = float(element[(1)])
        if precent_value > 100:
            print(f'{car:37}-->  Distance exceeds max range ({precent_value:.0f}%)')
        else:
            print(f'{car:37}-->  {precent_value:.0f}%')


if __name__ == '__main__':
    main()
