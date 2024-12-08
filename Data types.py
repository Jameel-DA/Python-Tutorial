# Data type is a Type of Data it is use for declaring a variable.
    
# Python Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data.

# The following are the standard or built-in data types in Python:

# Text-type: String
name = "Jameel"
print(type(name))  # Output: <class 'str'>

# Numeric Types: Integer(int), Floating point(float), Complex
age = 25
print(type(age))  # Output: <class 'int'>

price = 19.99
print(type(price))  # Output: <class 'float'>

number = 3 + 4j
print(type(number))  # Output: <class 'complex'>


# Sequence Types: list, tuple and range
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>

coordinates = (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>

# Boolean Type: bool
is_active = True
print(type(is_active))  # Output: <class 'bool'>

# Set Type: set, frozenset
unique_numbers = {1, 2, 3, 4}
print(type(unique_numbers))  # Output: <class 'set'>

frozen = frozenset({1, 2, 3})
print(type(frozen))  # Output: <class 'frozenset'>

# Mapping Type: dictionaries(dict)
student = {"name": "Jameel", "age": 22}
print(type(student))  # Output: <class 'dict'>


# Binary Types: bytes, bytearray, memoryview
byte_data = b"Hello"
print(type(byte_data))  # Output: <class 'bytes'>

byte_array = bytearray(b"Hello")
print(type(byte_array))  # Output: <class 'bytearray'>

memory = memoryview(b"Hello")
print(type(memory))  # Output: <class 'memoryview'>

# None Type
data = None
print(type(data))  # Output: <class 'NoneType'>
