x = 5.0
y = float.fromhex("A")
print("X =", x, "Y =", y)
print("x.as_integer_ratio() =", x.as_integer_ratio())
print("y.hex() =", y.hex())

# Typical comparisons can be made
print("x == y =", x == y)
print("x != y =", x != y)
print("x >= y =", x >= y)
print("x > y =", x > y)
print("x <= y =", x <= y)
print("x < y =", x < y)

# The usual operators can be used
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)

# There are several built-in functions:
print("divmod(x, y) =", divmod(x, y))   # returns tuple with divisor and remainder
print("pow(x, y) =", pow(x, y))         # power function (raises x to y)
print("abs(-x) =", abs(-x))             # how far the number is from 0 (always a positive value)
print("int(5.2) =", int(x))           # always turns a float to an int
print("float(10) =", float(10))           # turns int into float

# Inline notation can be used
print("x = x + y =", end=" ")
x += y
print(x)
print("x = x - y =", end=" ")
x -= y
print(x)
print("x = x * y =", end=" ")
x *= y
print(x)
print("x = x / y =", end=" ")
x /= y
print(x)

# multiple assignment
x, y = 4.5, 2.1
print("x =", x, ",", "y =", y)

# Bitwise Operators cannot be used for floats