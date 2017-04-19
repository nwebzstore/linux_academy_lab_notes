# file processing in python

filename = '/var/log/secure'

# line by line is the preferred way to read a file

# for line in open(filename):
 #    print(line)

# slurping the file (reading a file in one go)
#with open(filename) as file_handle:
#    lines = file_handle.readlines()
#    for line in lines:
#        print(line)

# writing to files
filewrite = 'textfile.txt'
with open(filewrite, 'w') as file_handle:
    file_handle.write("here i have written some text for your review\n")

with open(filewrite, 'a') as file_handle:
    file_handle.write("here i write something new\n")

