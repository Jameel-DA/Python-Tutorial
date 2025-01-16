with open("sam.txt", 'a') as f:
    f.write("My Name is Jameel Joy")
    f.close()

with open("sam.txt", 'r') as f:
    print(f.read())    