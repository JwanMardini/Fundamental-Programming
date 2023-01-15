import sys
import pickle


def display_menu():
    print()
    print('1. Add file')
    print('2. Calculate')
    print()


def cross_reference(files):
    length = len(files)
    if length == 0:
        # if the list is empty then return empty set
        return set()
    else:
        sets = []
        index = 0
        # index is to control the loop over the recived list
        while index < length:
            # opens the file and adds the content into a list
            filename = open(files[index], 'r')
            content = filename.readlines()
            created_list = []
            for line in content:
                created_list.append(line.rstrip('\n'))
            # converts the list to a set
            set1 = set(created_list)
            # adds the set to a list
            sets.append(set1)
            index += 1
        # finds the number that occurs in all sets in the list
        result = set(sets[0])
        for item in sets:
            result = result.intersection(item)
        return result


def map_numbers_to_names(numbers, filename):
    list = []
    open_dic = open(filename, 'rb')
    dic = pickle.load(open_dic)
    for number in numbers:
        if number in dic:
            list.append(dic[number])
        elif number not in dic:
            list.append(f'Unknown ({number})')
    open_dic.close()
    return list


def display_suspects(names):
    print()
    print('The following persons was present on all crime scenes:')
    print('------------------------------------------------------')
    counter = len(names)
    if counter == 0:
        print('No matches')
    else:
        for name in names:
            print(name)


def main():
    try:
        dic = sys.argv[1]
        controller = True
        list_of_files = []
        while controller:
            display_menu()
            choice = input('Enter choice: ')
            if choice == '1':
                filename = input('Enter a filename (include full path): ')
                list_of_files.append(filename)
            elif choice == '2':
                cross_reference1 = cross_reference(list_of_files)
                list_w_the_names = map_numbers_to_names(cross_reference1, dic)
                display_suspects(list_w_the_names)
                controller = False
            else:
                continue
    except FileNotFoundError:
        print('Error: There was a problem with at least one of the files.')


if __name__ == '__main__':
    main()
