print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5)  # Bitwise AND
print(9 | 4)  # Bitwise OR
print(12 ^ 42)  # Bitwise XOR
print(~88)  # Bitwise NOT

# OUTPUT:
# 0
# 10
# 0
# 13
# 38
# -89


shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))

# AND
print(bin(0b1110 & 0b101)) # 0b100

# OR
print(bin(0b1110 | 0b101)) # 0b1111

# XOR
print(bin(0b1110 ^ 0b101)) # 0b1011

#NOT
print(~1)
print(~2)
print(~3)
print(~42)
print(~123)

# OUTPUT ^^
# -2
# -3
# -4
# -43
# -124

# BITMASK CHECKS
def check_bit4(input):
    mask = 0b1000
    checked = input & mask
    if checked > 0:
        return "on"
    return "off"


#  ENABLE BIT w/ BIT MASK
a = 0b10111011
mask = 0b100
print(bin(a | mask)) # 0b10111111

# FLIP BITS w/ XOR
a = 0b11101110
mask = 0b11111111
print(bin(a ^ mask)) #0b10001

# use shift to slide masks in place   (Shifts "nth" bit)
def flip_bit(number, n):
  mask = 0b1 << (n - 1)
  result = number ^ mask
  return bin(result)

