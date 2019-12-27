import os

path = "./YourFolderName/"
files = os.listdir(path)

# '_' show character that you like split filename with it
sorted_files = sorted(files, key=lambda x: int(os.path.splitext(x.split('_')[1])[0]))

print(sorted_files)

# for file in sorted_files:
#     print(file)

'''
If your files are anything like the following:
files = ['file_2', 'file_3', 'file_10', 'file_11', 'file_20', 'file_1', 'file_21']

Without use of this code and
Use common file reading methods and sorted() method (in python) you see:
['file_1', 'file_10', 'file_11', 'file_2', 'file_20', 'file_21', 'file_3']

But by use this code you see:
['file_1', 'file_2', 'file_3', 'file_10', 'file_11', 'file_20', 'file_21']
'''
