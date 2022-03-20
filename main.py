import os


def sorting(directory):
    sorted_list = {}
    for items in os.listdir(directory):
        with open(directory + '/' + items, 'r+', encoding='utf-8') as fd:
            common_list = fd.read().splitlines()
            str_len = len(common_list)
            sorted_list.update({str_len: [fd.name, str_len, common_list]})
    return sorted(sorted_list.values(), key=lambda x: x[2], reverse=True)


def created(created_file):
    with open(created_file + '.txt', 'w+', encoding='utf-8') as newfile:
        for file in sorting('task_three'):
            newfile.write(f'{file[0]}\n')
            newfile.write(f'{file[1]}\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')


created('new_text')
