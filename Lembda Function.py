# Lembda Function
# It is used when an anonymous function is required for a short period of time.
# It can take nemerous argument.
# It can only have one expression.

# These are mainly used when we need nameless function for short period of time.

a = lambda a,b,c : a+b+c

print(a(2,3,4))


lar = lambda x,y: x if x > y else y

print(lar(2,3))