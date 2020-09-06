a = 0b01011010
b = 0b10101111
print(bin(a & b))  # 0b00001010
print(bin(a | b))  # 0b11111111
print(bin(a ^ b))  # 0b11110101

# can also do multiple bitwise comparisons at a time
print(bin((a ^ b) | (b & a)))  # 0b11111111
print(bin((a | b) ^ (b & a)))  # 0b100111110110

print(bin(a >> 1))  # 101101
print(bin(a >> 3))  # 1011
print(bin())
