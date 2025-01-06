# class PublicExample:
#     def __init__(self):
#         self.public_var = "I am Public Data"

#     def disp(self):
#         print(self.public_var)    

# ob = PublicExample()
# print(ob.public_var) #accessible outside the class
# print(ob.disp()) #accessible inside the class

# class ProtectedExample:
#     def __init__(self):
#         self._protected_var = "I am Protected Data"

#     def disp(self):
#         print(self._protected_var)    

# ob = ProtectedExample()
# print(ob._protected_var) #accessible outside the class
# ob.disp() #accessible inside the class


# class PrivateExample:
#     def __init__(self):
#         self.__private_var = "I am Private Data"

#     def disp(self):
#         print(self.__private_var)    

# ob = PrivateExample()
# print(ob.Private_var) #can't accessible outside the class and print error
# ob.disp() #accessible inside the class


# class Encapsulation:
#     def __init__(self):
#         self.__disp()

#     def __get(self):
#         self.__private_var = "I am Private Var"

#     def __disp(self):
#         self.__get()
#         print(self.__private_var)
#         print("I am Private Method")    

# ob = Encapsulation()
# # ob.__disp() #We Cant accesible the Private Fuction outside the class

# # print(ob.__private_var)#cant Access the Private Variable outside the class 