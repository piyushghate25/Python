with open('log.txt' , 'r') as f:
    content1  = f.read()

with open('this.txt' ,'r') as f:
    content2 = f.read()

if(content1 == content2):
    print("This files are identical")
else:
    print("This files are not identical")