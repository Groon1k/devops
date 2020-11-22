import re

count = 0
lst = []
start = int(input('start of working day: '))
end = int(input('end of working day: '))
f1 = open('/var/log/auth.log')
for line in f1:
    count += 1
    time = re.search(r"\w\w:\w\w:\w\w", line)
    if int(time.group(0)[0:2]) < start or int(time.group(0)[0:2]) > end or (int(time.group(0)[0:2]) == end and (int(time.group(0)[3:5]) != 0 or int(time.group(0)[6:]) != 0 )):
            lst.append(count)
print(lst)
