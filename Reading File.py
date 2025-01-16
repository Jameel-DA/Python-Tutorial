# read() - Reads the whole data 
# read(l) - Reads data of length
# tell() - Tell you about the position of file handle
# seek() - It hepls to re position your file handle
# readlines() - read data Line by Line

with open("new.txt") as f:
    # print(f.read(10))
    # print(f.read((20)))
    # print(f.tell()) 
    d = f.read() 
    for i in d:
        print(i)

    print(f.readline())        