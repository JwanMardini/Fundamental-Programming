import pickle
import sys


def read_file(filename):
    open_dic = open(filename, 'rb')
    dic = pickle.load(open_dic)
    return dic


def map_to_int(measurements):
    created_dic = {}
    for key in measurements:
        remove_char = measurements[key].rstrip('°')
        created_dic[key] = int(remove_char)
    return created_dic


def find_faulty(primary, secondary, threshold):
    returned_set = set()
    for key in primary:
        if primary[key] >= secondary[key]:
            compare = primary[key] - secondary[key]
        elif primary[key] <= secondary[key]:
            compare = secondary[key] - primary[key]
        else:
            pass
        if compare > threshold:
            returned_set.add(key)
    return returned_set


def display_warnings(faulty_sensors):
    print()
    print('Analyzis of the provided files is complete.')
    print('-------------------------------------------')
    print()
    print('The following sensors differ more than 2°:')
    for element in faulty_sensors:
        print(element)


def main():
    try:
        primary = sys.argv[1]
        secondary = sys.argv[2]
        threshold = 2
        read_primary = read_file(primary)
        read_secondary = read_file(secondary)
        value_to_int1 = map_to_int(read_primary)
        value_to_int2 = map_to_int(read_secondary)
        finds_diffrence = find_faulty(value_to_int1, value_to_int2, threshold)
        display_warnings(finds_diffrence)
    except FileNotFoundError:
        print('Error: The files given as arguments are not valid.')


if __name__ == '__main__':
    main()
