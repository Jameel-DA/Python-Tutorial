# Creating a new file
with open("new.txt","w") as f:
    f.write("Hello This is My New File")

# Write in Existing file 
with open ("new.txt","w") as f:
    f.write("Ok This is the Updated Content")   
    f.write("\nOk This is New Line") 
    
      