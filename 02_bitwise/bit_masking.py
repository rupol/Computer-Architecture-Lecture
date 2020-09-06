instruction = 0b10011010

# shifting by 6 should leave us with first two values
shifted = instruction >> 6
print(bin(shifted))  # 0b10

# what if we wanted to extract the two numbers in the middle?
# first, convert so the bits in the middle are the last two digits
shifted = instruction >> 3
print(bin(shifted))  # 0b10011
# it's still not isolated, so now we'll need to remove all the preceding numbers (turn to 0s)
# apply mask
mask = 0b00000011 & shifted
print(bin(mask))
