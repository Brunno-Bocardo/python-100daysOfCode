# String
print("This is a string")
print("This is a string"[9]) # nona letra
print("This is a string"[-9]) # nona letra de trás pra frente

# Integer
print(26)
print(29 + 57)

# Float
print(3.14)

# Large Integers
print(123_456_789) #just make the number more readable

# Boolean
print(True)
print(False)


# ============================================================================

# Podemos descobrir o typo de um dado ou variável
type(123)
fruta = "banana"
print(type(fruta))


# Type conversion / Type Casting
print("123" + "76") # concatenação, não soma
print(int("123") + int("76"))  # soma


# ============================================================================

print(6 / 2) # 3.0
# numa divisão, sempre retornará um float

print(6 // 2) # dessa forma, elimuna as casas decimais 


# ============================================================================

# Potência
print(2 ** 3)


# ============================================================================

decimal_number = 8.85
print(round(decimal_number)) # 9
decimal_number = 3.3
print(round(decimal_number)) # 3
large_decimal_number = 6.7358409584640
print(round(large_decimal_number, 2)) # 6.74