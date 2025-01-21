import re

# Match example
result = re.match(r'\d+', '123abc')
if result:
    print("Matched:", result.group())  # Output: 123

# Search example
result = re.search(r'abc', '123abc456')
if result:
    print("Found:", result.group())  # Output: abc

# Findall example
result = re.findall(r'\d+', 'abc123def456ghi789')
print("All Matches:", result)  # Output: ['123', '456', '789']

# Sub example
result = re.sub(r'\d+', '#', 'abc123def456')
print("Replaced String:", result)  # Output: abc#def#
