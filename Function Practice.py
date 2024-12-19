# Find even number
def even(li):
    for i in li:
        if i % 2 == 0:
            print(f"{i} : even")
even([1,2,3,4,5,6,7,8])  


# Find Unique element in a list 

# def unique_ele(li):
#     s = set(li)
#     s = list(s)
#     return s

# print(unique_ele([1,2,3,4,2,4]))



def unique_ele(li):
    new = []
    for i in li:
        if i not in new:
            new.append(i)
    return new
print(unique_ele([1,2,3,4,2,4]))