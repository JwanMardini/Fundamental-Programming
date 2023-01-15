# def cross_reference(files):
#     length = len(files)
#     if length == 0:
#         return set()
#     else:
#         sets = []
#         index = 0
#         while index < length:
#             filename = open(files[index], 'r')
#             content = filename.readlines()
#             created_list = []
#             for line in content:
#                 created_list.append(line.rstrip('\n'))
#             set1 = set(created_list)
#             sets.append(set1)
#             index += 1
#         result = set(sets[0])
#         for item in sets:
#             result = result.intersection(item)
#         return result


# # def cross_reference(files):
# #     length = len(files)
# #     if length == 0:
# #         return set()
# #     else:
# #         set2 = set()
# #         index = 0
# #         while index < length:
# #             filename = open(files[index], 'r')
# #             content = filename.readlines()
# #             created_list = []
# #             for line in content:
# #                 created_list.append(line.rstrip('\n'))
# #             set1 = set(created_list)
# #             set3 = set1.intersection(set2)
# #             set2 = set1
# #             index += 1
# #     return set3


# def main():
#     list = ['Lab3_3_1.txt', 'Lab3_3_2.txt', 'Lab3_3_3.txt']
#     cross_reference(list)


# if __name__ == '__main__':
#     main()

mystr = 'abc' * 3
print(mystr)
