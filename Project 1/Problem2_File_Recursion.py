import os

def find_files(suffix,path):
    if not os.path.isdir(path):
        return 'Invalid Directory'

    path_list = os.listdir(path)
    output = []
    for item in path_list:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            output += find_files(suffix, item_path)
        if os.path.isfile(item_path) and item_path.endswith(suffix):
            output.append(item_path)
    return output
paths = './testdir'

print("***Test Case 1***")
print(find_files(suffix='c', path=paths))

print("***Test Case 2***")
print(find_files(suffix='h', path=paths))

print("***Test Case 3***")
print(find_files(suffix='z', path=paths))

print("***Test Case 4***")
print(find_files('.c', './asdf'))

print("***Test Case 5***")
print(find_files('.c', './Problem 2/emptydir'))

print("***Test Case 6***")
print(find_files('.py', path = paths))