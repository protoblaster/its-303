# the bytesarray type
# the bytesarray class provides a mutable sequence
# Values must be an integer from 0-255 to represent a byte

emptyArray = bytearray()
nullArray = bytearray(11)
intsArray = bytearray((84, 114, 97, 100, 101, 109,
                    97, 114, 107, 32, 194, 174))
strArray = bytearray("Trademark ©", "utf-8")
bytesArray = bytearray(b"Trademark \xc2\xae")
print("bytesArray =", bytesArray)
print("bytesArray.decode() ->", bytesArray.decode())

strLiteral = "Trademark ©"

# A bytearray sequence behaves similar to a string
print(strLiteral.count("T"))
print(strLiteral.index("T"))

# However, byte values are used instead of string values
print(bytesArray.count(0x54))
print(bytesArray.index(0x54))

# bytesarray objects have methods to mutate them
bytesArray.append(32)
print("bytesArray =", bytesArray)

bytesArray.extend((194, 174))
print("bytesArray =", bytesArray)
print("bytesArray.decode() ->", bytesArray.decode())
bytesArray.remove(0x54)
print("bytesArray =", bytesArray)
bytesArray.insert(0, 0x54)
print("bytesArray =", bytesArray)
bytesArray.pop()
bytesArray.pop()
print("bytesArray.decode() ->", bytesArray.decode())