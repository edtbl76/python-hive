#!/usr/bin/env python3

#   NAND
#
#   0, 0 = 1
#   0, 1 = 1
#   1, 0 = 1
#   1, 1 = 0
#
def nand_gate(input1, input2):
    if input1:
        if input2:
            return 0
    return 1

#   NOT
#
#   0 = 1
#   1 = 0
#
def not_gate(input):
    # A not gate is ultimately the special case of a nand_gate, where both inputs are equivalent.
    return nand_gate(input, input)


#   AND
#
#   0, 0 = 0
#   0, 1 = 0
#   1, 0 = 0
#   1, 1 = 1
#
def and_gate(input1, input2):
    # AND is just a negated nand gate
    return not_gate(nand_gate(input1, input2))


#   OR
#                   NAND _ RESULTS
#   0, 0 = 0        nand(nand(0, 0), nand(0, 0)) = nand(1, 1) = 0
#   0, 1 = 1        nand(nand(0, 0), nand(1, 1)) = nand(1, 0) = 1
#   1, 0 = 1        nand(nand(1, 1), nand(0, 0)) = nand(0, 1) = 1
#   1, 1 = 1        nand(nand(1, 1), nand(1, 1)) = nand(0, 0) = 1
#
def or_gate(input1, input2):
    # the inner nand_gates act as a negation of the inputs.
    # By negating the inputs to their opposites, we create an or gate by solving for the opposing inputs in a
    # nand gate (which has the reverse pattern of the OR gate)
    return nand_gate(nand_gate(input1, input1), nand_gate(input2, input2))


#   XOR
#                               NANDS only                                      MIXED
#   0, 0 = 0        NAND( NAND(0, NAND(0, 0)), NAND(0, NAND(0, 0))      and(nand(0, 0), or(0,0))
#                   NAND( NAND(0, 1), NAND(0, 1))                       and(1,0)
#                   NAND(1, 1) = 0                                      0
#
#   0, 1 = 1        NAND( NAND(0, NAND(0, 1)), NAND(1, NAND(0, 1))      and(nand(0, 1), or(0, 1))
#                   NAND( NAND(0, 1), NAND(1, 1))                       and(1, 1)
#                   NAND(1, 0) = 1                                      1
#
#   1, 0 = 1        NAND( NAND(1, NAND(1, 0)), NAND(0, NAND(1, 0))      and(nand(1, 0), or (1, 0))
#                   NAND( NAND(1, 1), NAND(0, 1))                       and(1, 1)
#                   NAND(0, 1) = 1                                      1
#
#   1, 1 = 0        NAND( NAND(1, NAND(1, 1)), NAND(1, NAND(1, 1))      and(nand(1, 1) or (1, 1))
#                   NAND( NAND(1, 0), NAND(1, 0))                       and(0, 1)
#                   NAND(1, 1) = 0                                      0
#
#   The mixed is easier to understand.
#   The pattern for XOR is => equal inputs are 0, unequal inputs are 1.
#   This is a good case for AND, provided we can make both equal 0's and equal 1's false
#   - The internal gates as NAND and OR make sense, because differing inputs always result to 1.
#       which means that they will match, so that the outer gate (AND) will return a 1
#   - The second reason they make sense is that they have opposite results for equal inputs.
#      When nand has both 0, it returns 1, while or returns 0. (and vice versa). This means that for
#      equal inputs, nand and or will always provide differing outputs, which provides the invariant that
#       we can make equal 0's and equal 1's both false (which is one of the traits of the XOR)
def xor_gate(input1, input2):
    return and_gate(nand_gate(input1, input2), or_gate(input1, input2))


# Test NAND Gate
print(f"A: 0, B: 0 | Output: {nand_gate(0,0)}")
print(f"A: 0, B: 1 | Output: {nand_gate(0,1)}")
print(f"A: 1, B: 0 | Output: {nand_gate(1,0)}")
print(f"A: 1, B: 1 | Output: {nand_gate(1,1)}")

# TEST NOT Gate
print(f"A: 0 | Output: {not_gate(0)}")
print(f"A: 1 | Output: {not_gate(1)}")

# TEST AND Gate
print(f"A: 0, B: 0 | Output: {and_gate(0,0)}")
print(f"A: 0, B: 1 | Output: {and_gate(0,1)}")
print(f"A: 1, B: 0 | Output: {and_gate(1,0)}")
print(f"A: 1, B: 1 | Output: {and_gate(1,1)}")

# TEST OR Gate
print(f"A: 0, B: 0 | Output: {or_gate(0,0)}")
print(f"A: 0, B: 1 | Output: {or_gate(0,1)}")
print(f"A: 1, B: 0 | Output: {or_gate(1,0)}")
print(f"A: 1, B: 1 | Output: {or_gate(1,1)}")

# TEST XOR Gate
print(f"A: 0, B: 0 | Output: {xor_gate(0,0)}")
print(f"A: 0, B: 1 | Output: {xor_gate(0,1)}")
print(f"A: 1, B: 0 | Output: {xor_gate(1,0)}")
print(f"A: 1, B: 1 | Output: {xor_gate(1,1)}")
