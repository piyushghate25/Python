with open("poem.txt") as f:
    content = f.read()
    if("twinkle" in content):
         print("It is present ")
    else:
        print("It is not present ")