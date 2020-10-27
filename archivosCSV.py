fileconnection = open("novenoF.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    print("{:<35} {:>30} {:>4}".format(
                 vals[0],
                 vals[1],
                 vals[2]))

