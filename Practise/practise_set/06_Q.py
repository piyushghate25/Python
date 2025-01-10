

with open("log.txt" ) as f :
    lines = f.readlines()

lineno = 1

for line in lines:
    if "python" in line:
        print(f"It is present in line {lineno}")
        break
    lineno += 1
else:
    print("It is not present in the file")