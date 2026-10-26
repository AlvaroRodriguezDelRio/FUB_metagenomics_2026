import sys

file_name = sys.argv[1]

for i in range(1,10,1):
    for line in open(file_name):
        line = line.rstrip()
        print (line)
