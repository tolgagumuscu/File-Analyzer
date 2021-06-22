import os


def find_number(directory):
    number_of_files = 0
    number_of_directories = 0
    for root, dirs, files in os.walk(directory):
        number_of_files += files.__len__()
        number_of_directories += dirs.__len__()
    return number_of_files, number_of_directories


def find_size(directory):
    total_size = 0
    size_list = []
    for r, d, f in os.walk(directory):
        for name in f:
            dir = (os.path.abspath(os.path.join(r, name)))
            size = os.stat(dir).st_size
            total_size += size
            size_list.append(size)
    return total_size, size_list


def find_type(directory):
    type_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            name, extension = os.path.splitext(file)
            type_list.append(extension)
    return type_list


def find_name(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)

    return file_list
