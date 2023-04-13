# Assembly 

While Assembly has been mostly abstracted away from the lives of the majority of programmers, it still has a few specific use cases throughout the industry such as:

- Embedded systems that have limited memory and hardware capacity
- Direct hardware testing
- Software optimization

Embedded systems, along with their microcontrollers, are very often programmed in Assembly because it gives programmers the ability to control hardware functions on a task by task level, ensuring the size and speed of the program maximizes hardware limits.

A refrigerator, for example, has limited storage and computing capacity. Programming in Assembly ensures that both are used to their full potential.

Learning an Assembly language can give a programmer the idea of the “cost of code”. Certain algorithms can be optimized based on data storage and memory access techniques. Understanding how hardware implements these techniques can help a programmer choose the right tools for the right job and develop superior code.

Small optimizations in programs might not seem incredibly important with our advances in processing power, but in some cases, they can make all the difference. For example, if we are trying to achieve as near to real-time analysis as we can get, say to predict market swings in the stock market, things as trivial as the bit-space taken up by an integer can make a huge difference at run-time.

 There are several Assembly languages, each written for a specific 
  processor, or more precisely, in accordance with a processor’s 
  Instruction Set Architecture. Three primary industry competitors are the 
 `x86`, `ARM`, and `MIPS` architectures, which account for the majority of desktop, mobile, and embedded technologies respectively.
 
## Compilation Process

When we push Run in our code editor, the computer is performing a number 
 of tasks in the background before the computer hardware even gets to see 
its first bit of binary code.

 In general, there are four steps, known as the Compilation Process, that 
 make up the journey high-level code goes on before reaching the hardware:

- <u>**Preprocessing**</u> is the first step of compilation and is used to 
prepare the user’s code for machine code by removing comments, expanding included macros, and performing any code maintenance prior to handing the file to the compiler.
- <u>**Compiling**</u> is the process of taking the expanded file from the 
preprocessor and translating the program into an optimized Assembly language.
- <u>**Assembling**</u> is the process of taking an assembly language program and 
using an assembler to generate machine code.
- <u>**Linking**</u> is the process of filling in function calls, including 
additional 
objects, libraries, and source code from other locations into the main source code.

While the compilation process is tailored to each language and architecture, the overall procedure is fairly standard. It is in the compiling and assembling stages where Assembly is generated and used to create machine code.

## Assembly Code Format

 Assembly language and binary code have almost a direct translation 
 between their outputs.

 Assembly was created as a mnemonic language to make machine code easier 
  to read and write, one instruction translating to one instruction. In 
  fact, most ISAs will have both the binary code and Assembly language 
 breakdown on the same page when talking about specific instructions.

 Just like in binary, Assembly begins with an opcode. Luckily for us, the 
  opcodes are much more readable than a bunch of 0’s and 1’s. Let’s take a 
 look at the multiply function:

```text
Assembly: MULT $3, $2
Binary: 00000000111001100000000000011000
```

 It’s easy to see how much easier it is to write a program in Assembly 
  than to write it in binary. In most Assembly instructions, what follows 
  the opcodes are the memory locations to be operated on. These memory 
  locations are referred to as `operands`. Generally, these are direct 
  register addresses but can also be memory references to values stored in 
 other types of memory such as the cache or RAM.

In MIPS, direct register addresses begin with the $ symbol, so in our MULT example, we are multiplying the value stored in register $2 by the value in register $3
(see [MIPS docs](https://s3-eu-west-1.amazonaws.com/downloads-mips/documents/MD00086-2B-MIPS32BIS-AFP-6.06.pdf) for more info)

## MATH

 Arithmetic operations make up the majority of functions in the Assembly 
 languages.

 After all, the manipulation of binary numbers is how you execute any type 
  of code, whether that be changing a character from lowercase to upper 
  case or turning a pixel on a screen from red to blue.

One of the most important aspects of mathematical operations is how 
n umbers are stored at the machine hardware level. Memory locations, such 
as registers, cache, or secondary storage, all have fixed binary lengths.

 These fixed lengths mean that processors must have special registers to 
  “catch” overflow from operations. Overflow operations can include 
  handling extremely large numbers, marking when a carryover occurs in 
  addition or storing both the quotient and remainder of division operations.

 Most languages allow for at least two distinct types of each arithmetic 
  operation. One type performs a calculation on two registers and the 
  other performs an operation using one value from a register and another 
 value that is directly added, known as an immediate or constant.

 The addition calculation for example can be called using the ADD opcode 
  which then takes three registers as operands, two registers to add 
 together and another to store the answer in.

 The addition function also has an ADDI command, which takes a register 
  address and a constant to operate on and a register to store the answer in.

 In the ADD function, the value in $5 is added to the value in $4 and 
 stored in $6.

```text
ADD $4, $5, $6
```

In the ADDI function, the constant 7 is added to the value in $4 and stored in $6

```text
ADDI $4, $6, 7
```

Other common arithmetic operations include: SUB, SUBI, MULT, MULTI, DIV, and DIVI.



## Memory Access Operations

- LW = LOAD WORD
- SW = STORE WORD

## CONTROL FLOW Operations

_branch statements_ are used to define conditional statements. Most 
branching operations center around arithmetic operations and their results

There are two primary ways we branch

- On equality
  - `BEQ` (Branch on Equal)
  - `BNE` ( Branch on Not Equal)
- On reference to zero
  - `BGTZ` / `BGEZ` (Branch on > zero / Branch on ≥ zero)
  - `BLTZ` / `BLEZ` (Branch on < zero / Branch on ≤ zero)
  
 The other way we can control the flow of our program is to jump directly 
  to a specific instruction using a _jump statement_, followed by the memory 
  location that contains the instruction. This is similar to making 
  function calls or returning back out of a function.
 

```text
Jump to Register 21 and execute instruction stored there: 

    J $31
```

## Memory Addressing (Direct/Indirect)

 Let’s assume that Register 5 has the value 11010001112 (83910) stored in 
  it. Let us also assume that there is a piece of memory with the address 
 839, that contains the value 10001110001112 (455110).

### Direct
 When we directly reference something in memory we are telling the 
 assembler that we want the value that is stored in that exact location.

 Let’s take a look at an Assembly code example that adds the value of 
 Register 5 to Register 5 and saves the result in Register 6:
 
```text
ADD $5, $5, $6
```
Register 6 now contains 110100011102 (167810). 839 + 839 = 1678

### Indirect
 When we indirectly reference memory we are telling the assembler that we 
  don’t want to use the value of what is stored in the reference, we want 
  to use that value as the address to another memory location and use the 
 value stored there.

```text
LW $4, ($5)
ADD $5, $4, $6
```
In MIPS we can only perform operations on registers so the first step is 
to retrieve the value from memory with the Load Word statement and save it into Register 4. When we use the parentheses around Register 5 we are now telling the assembler to go and find the data that is stored in the memory address 839 which was 10001110001112 (455110).

At the conclusion of our ADD statement, Register 6 now contains the value 10101000011102 (539010). 4551 + 839 = 5390.

## Translations between Binary and Assembly

Assembly was written as the first language above binary to make it easier for humans to write functional programs. As such, there is almost a line for line equivalency between the two codes.

When we first translated the simple square() method to Assembly in Exercise 3, our two lines of Python code expanded into 16 lines of Assembly. The code editor has the Python and the translated Assembly in the window to the right.

When the Assembler translates the Assembly code into machine code, each line will create a 32-bit MIPS instruction in accordance with the standards of the ISA.

The Assembly ADD function and the binary ADD function are structured the same way in the documentation in order to give developers better control over their programs.

