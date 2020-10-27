olypmicsfile = open("abc.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(" ")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

olypmicsfile = open("abc.txt", "r")
num_lines=0
for aline in olypmicsfile.readlines():
    num_lines+=1
print(num_lines)


olypmicsfile.close()

