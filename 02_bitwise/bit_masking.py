instruction = 0b10100010

# shifting by 6 should leave us with first two values
shifted = instruction >> 6
# print(bin(shifted))  # 0b10

# what if we wanted to extract the two numbers in the middle?
# first, convert so the bits in the middle are the last two digits
shifted = instruction >> 3
# print(bin(shifted))  # 0b10011
# it's still not isolated, so now we'll need to remove all the preceding numbers (turn to 0s)
# apply mask
mask = 0b00000011 & shifted
# print(bin(mask))

middle_two = (instruction >> 3) & 0b00000011
# print(bin(middle_two))

b = (instruction >> 5) & 0b00000001
# print(bin(b))

c = (instruction >> 4) & 0b00000001
print(bin(c))

flag = 0b00000101  # 00000LGE
l = (flag >> 2) & 0b00000001
g = (flag >> 1) & 0b00000001
e = (flag >> 0) & 0b00000001
print(l, g, e)
