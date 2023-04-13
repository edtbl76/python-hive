from nand import NAND_gate
from not_gate import NOT_gate
from and_gate import AND_gate
from or_gate import OR_gate
from xor_gate import XOR_gate

def half_adder(a, b):
  s = XOR_gate(a, b)
  c = AND_gate(a, b)
  return (s, c)

print("-- HALF --")
print(half_adder(0, 0))
print(half_adder(0, 1))
print(half_adder(1, 0))
print(half_adder(1, 1))


def full_adder(a, b, c):
  s1, c1 = half_adder(a, b)
  s2, c2 = half_adder(s1, c)
  c_out = OR_gate(c1, c2)
  return (s2, c_out)

print("-- FULL --")
print(full_adder(0, 0, 0))
print(full_adder(0, 0, 1))
print(full_adder(0, 1, 0))
print(full_adder(0, 1, 1))
print(full_adder(1, 0, 0))
print(full_adder(1, 0, 1))
print(full_adder(1, 1, 0))
print(full_adder(1, 1, 1))

