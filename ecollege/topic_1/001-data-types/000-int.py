x = 5
y = 10
y = 0xA     # hexadecimal
y = 0o12    # octal
y = 0b1010  # binary
print("x=", x, ",", "y=", y)

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

# In python2 x / y uses floor division like:
print("x // y =", x // y)   # floor division
print("x % y", x % y)       # modulus (remainder after division)
print("x ** y =", x ** y)   # power

# There are several built-in functions:
print("divmod(x, y) =", divmod(x, y))   # returns tuple with divisor and remainder
print("pow(x, y) =", pow(x, y))         # power function (raises x to y)
print("abs(-x) =", abs(-x))             # how far the number is from 0 (always a positive value)
print("int(5.2) =", int(5.2))           # always turns a float to an int
print("int('0xff', 16) =", int("0xff", 16))     # base 16 -- different type of number
print("float(x) =", float(x))           # turns int into float

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
x, y = 4, 2
print("x =", x, ",", "y =", y)

# Bitwise Operators
print("Or: x | y =", x | y)
print("Xor: x ^ y =", x ^ y)
print("And: x & y =", x & y)
print("Left Shift: x << y =", x << y)
print("Right Shift: x >> y =", x >> y)
print("Inversion: -x =", -x)
