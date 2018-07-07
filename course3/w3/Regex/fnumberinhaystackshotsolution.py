import re

fileName = input("Enter name of file")
if len(fileName) < 1:
    fileName = "sample.txt"
handle = open(fileName)
data = handle.read()
print(sum([int(num) for num in re.findall("[0-9]+",data)]))
