import sys


def main():
    try:
        filename = sys.argv[1]
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' could not be found.")
    else:
        list = read_file(filename)
        name = input('Enter a name to search for: ')
        for element in list:
            name_in_list = element[(0)]
            message_in_list = element[(1)]
            if name == name_in_list:
                display_entry(name, message_in_list)


def read_file(filename):
    open_file = open(filename, 'r')
    name = open_file.readline().rstrip('\n')
    list = []
    while name != '':
        message = open_file.readline().rstrip('\n')
        list.append((name, message))
        name = open_file.readline().rstrip('\n')
    return list


def display_entry(name, message):
    print(f'[{name}] --> {message}')


if __name__ == '__main__':
    main()
