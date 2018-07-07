import re;

fileName = input("Enter name of file")
if len(fileName) < 1:
    fileName = "sample.txt"
handle = open(fileName)
sum = 0
#print(handle)
for line in handle:
    nums = re.findall("[0-9]+", line)
    if nums is None or len(nums)==0:
        continue
    for num in nums:
        sum += int(num)
print(sum)
