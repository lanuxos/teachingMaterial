# file management

# read()
print('READ')
# f = open('C:\\temp\\file_management.txt', 'r')
f = open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'r')
print(f.name)
print(f.closed)
print(f.mode)
print(f.read())

# readline()
print('READ LINE')
f_line = open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'r')
while True:
    one_line = f_line.readline()
    if len(one_line):
        print(one_line)
    else:
        break

# readlines()
print('READ LINES')
f_lines = open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'r')
print(f_lines.readlines())

# loop read one by one word
f_one_by_one = open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'r')
words_list = []
word_count = 0
for lines in f_one_by_one:
    for one in lines.split():    # split() spit word through space
        words_list.append(one)
        word_count += 1

print('ONE BY ONE WORD: ', word_count, 'word(s)', words_list)

# tell()
f_tell = open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'r+')
position = f_tell.tell()
print('POSITION', position)
read_out = f_tell.read(5)
print('READ OUT:', read_out)
position = f_tell.tell()
print('tell() POSITION', position)

# seek(offset[, from])  from => 0 begin of file; 1 current position; 2 end of file
position = f_tell.seek(5, 0)    # 
print('seek(5, 0) POSITION', position)
read_out = f_tell.read(5)
print('READ OUT:', read_out)

# # write() writelines()
# new_line = '\nthis is new line using write() method'
# new_message = ['\nnew message line1\n', 'new message line2\n', 'new message line3\n']
# f_write = open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'a+')
# f_write.write(new_line)
# f_write.writelines(new_message)
# f_write.close()

# # with
# with open('/Users/la/Documents/teachingMaterial/python/file_management.txt') as file_with_read:
#     for read_out_line in file_with_read:
#         print(read_out_line)

# with open('/Users/la/Documents/teachingMaterial/python/file_management.txt', 'a+') as file_with:
#     another_new_line = '\nthis line write using "with" keyword'
#     file_with.write(another_new_line)

# directory management
import os
print(os.getcwd())
# os.rename('/Users/la/Documents/teachingMaterial/python/file_management.txt', '/Users/la/Documents/teachingMaterial/python/file_management_1.txt')
# os.remove('/Users/la/Documents/teachingMaterial/python/file_management_1.txt')
# os.mkdir('/Users/la/Documents/teachingMaterial/python/os_mkdir')
# os.chdir('/Users/la/Documents/teachingMaterial/python/')
# os.rmdir('/Users/la/Documents/teachingMaterial/python/os_mkdir')
