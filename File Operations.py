# Modes of Opening a file 

# 'r' : Read Only
# 'w' : Write Only
# 'a' : Append data at the end of file
# 'wt' : Write Text
# 'wb' : Write Binary
# 'rb' : Read Binary
# 'rt' : Read Text


f = open("sam.txt","w")

f.write("I am Data Analyst")

f.close()

f1 = open("sam.txt")

print(f1.read())