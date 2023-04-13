# Instruction Set Architecture

 In practice, the hardware of our computer, such as the _Central Processing 
  Unit (CPU)_, works with a series of electrical signals called _binary_, 
  meaning ‘composed of two things:

- 0 representing ‘OFF’ or FALSE
- 1 representing ‘ON’ or TRUE

 Our computer’s software, the programming languages we typically write in 
  like C++, Java, or Python, uses human-readable code such as double 
  priceOfGas = 2.49; and if-else statements. The hardware and software of 
  our computers are not speaking the same language because 0’s and 1’s do 
 not directly equate into phrases that we programmers can read.

 It is ultimately the job of the ISA to manage the translation of these 
  values into the hardware readable code. The ISA defines the list of all 
  the functions that the CPU can understand and how to translate a message 
  between the hardware and software so that both entities understand each 
 other.
 

## CISC (Complex Instruction Set Computer)

 The first attempts at designing ISAs focused on reducing the number of 
  instructions that a computer would have to process. Many of the data 
  transfer channels were moved by hand, physically disconnecting wires and 
  plugging them into different components, so the logic went that the 
  fewer times people had to move the cables, the faster this would go. 
  Memory space was also very limited, meaning that the fewer lines of code,
 the better.

 Inside the computer, this was implemented with more hardware such as 
  cables, components, and a significant increase in power consumption to 
  processes complex instructions. It was generally viewed that combining 
  instructions such as “load a number from memory, perform an arithmetic 
 calculation, and store to another memory location” into one instruction 
 was the most efficient way to get things done.

 This new standard of architecture models came to be known as Complex 
  Instruction Set Computer, or CISC for short, and for quite some time 
  reigned supreme in design theory. The design focused on having computer 
  scientists write as few lines of code as possible to maximize their 
  performance.
 
## RISC (Reduced Instruction Set Computer)

It wasn’t until the mid-1970s that another approach came along, the Reduced Instruction Set Computer or RISC. John Cocke, widely recognized as the founder of RISC, theorized that if they simplified the instructions to a very limited number of easy calculations, the computer could process them in a single machine cycle, allowing for multiple processes to be “pipelined” (something we’ll learn in an upcoming module), and in turn resulting in faster overall speeds and reducing the amount of power needed to operate the computer.

Dr. Cocke, when reviewing the inputs and outputs of a CISC computer at a telegraph switchboard, realized that the computer rarely chose the most advantageous method of performing a task. By reducing the number and complexity of the instructions he could improve the overall performance while at the same time reducing components, power use, and heat generation. The downside was that the programmers would have to write more code for the computer. We might not think twice nowadays about creating a several thousand line program, disk space is nearly limitless and RAM is abundant, but in the days of Dr. Cocke, these resources were just beginning to show signs of being capable of handling large programs.

## Modern / Future

Three primary ISAs have emerged out of the technology revolution of the late 20th century:

- x86 (CISC design)
- ARM (RISC design)
- MIPS (modified RISC design for embedded processors)
    - (Microprocessor w/o Interlocked Pipeline Stages) fixed 32bit instruction length, limited instructions. 


Each design has its advantages, disadvantages, and parts of the industry where they excel and will continue to do so for the foreseeable future. Eventually, quantum computing will force the development of new ISAs as hardware begins relying on more than two states (OFF and ON) and transforms into multi-state logic processors (OFF, ON, and both). Companies such as IBM, Intel, and Microsoft are working diligently to develop these solutions as the technology arrives.


---
ISA is an abstract concept. It is a contract between the software and 
hardware so that a specific sequence of binary data will result in a 
specific sequence of processing by the CPU. 

Layers
- User Programs
- High Level Language 
- Compiler
- Assembly Language
- ISA
- Hardware


## CPU
![](img/hardware.png)

### `Control Unit (CU)`
Overseer of CPU, responsible for controlling and 
 monitoring the input and output of data from the computer’s hardware.

The Control Unit is the component receiving instructions from the software and running the show. Its primary job is making sure that data is sent to the right component, at the right time, and arrives with integrity.

Part of this job is keeping all the hardware working on the same schedule. It does this with a clock, which sends out a regular electrical signal to all components at the same time to coordinate activities.

### `Arithmetic and Logic Unit (ALU)` 

where all the processing on your 
  computer takes place. Even as you scroll this text box, the ALU is 
  calculating pixel changes on the screen and sending that output to the 
 monitor.

The ALU is the fundamental building block of the CPU, the brains of the entire computer. Nearly all functional processing occurs in this chip. As the name implies, the ALU’s functions can be divided into two primary areas:

- Arithmetic operations that deal with calculating data (e.g. 5 * 4 = 20)
- Logic operations that deal with comparisons and conditionals (e.g. 25 > 10)

### `Registers (Immediate Access Store)` 

limited space, high-speed memory 
 that the CPU can use for quick processing.

Registers are small pieces of memory right on the CPU. They are fixed in number and defined in the Instruction Set Architecture. There are typically 8, 16, 32, or 64 registers depending on the architecture and are also fixed in size based on the size of the number it can hold. They provide the CPU with a place to store and access values that are crucial to the immediate calculations the ALU is processing.

### `Random Access Memory (RAM)`

additional high-speed memory that a computer uses to store and access information on a short-term basis. In general, a computer’s performance can be directly correlated to the amount of RAM it has available to use. RAM is considered primary volatile memory, which means it loses whatever is stored on it as soon as power is disconnected.

### `Buses`

engineering term for a job-specific high-speed wire. These wires are often grouped together in bundles and will transfer electrical signals either in parallel or in serial — that is, many signals at once or one pulse at a time. Buses can be grouped into three functions: data buses, address buses, and control buses.

- **Data Buses** carry data back and forth between the processor and other components. Data buses are bidirectional, which means that they transfer data both to and from other locations.
- **Address Buses** carry a specific address in memory and are unidirectional. We can visualize all of our memory like a village with each house representing a package of data. Every house/data has an address. When our computer tells a program or component what data to use, it sends the address and then the component knows where to find the data when it needs it.
- **Control Buses** unidirectional and are responsible for carrying the control signals of the CU to other components as well as the clock signals for synchronization.

### Hard Disks

Hard disks, or hard drives, are responsible for the long-term, or 
secondary storage of data and programs. This is an example of non-volatile memory, meaning that it will retain its information when we shut down our computer.

---

# Opcodes

The Instruction Set Architecture defines how hardware processes binary data. Each 0 or 1 of binary data is called a bit and groups of these bits are put together in specific lengths that create instructions.

While the length of a specific binary instruction varies widely based on the ISA that is being used, the first few bits are always the OPCODE or OPeration CODE. This sequence of bits tells the processor what type of instruction it is receiving.

Every function or calculation that a processor can perform is defined by a specific OPCODE and the CU routes the remaining bits of information to the corresponding hardware that will execute the operation.

The list of all of these is included with the ISA documentation in the form of an OPCODE Table:

| Mnemonic | OPCODE | Layman's<br/> Definition                                                  | Formal<br/>Definition          |
|----------|--------|---------------------------------------------------------------------------|--------------------------------|
| ADD      | 000001 | Loads 2 numbers from registers and<br/>saves result into another register | rs_reg <- op_reg_1 + op_reg_2  |
|
| LOAD     | 000010 | Loads a number from a memory address <br/> location into a register       | rs_reg <- op_reg_1 + op_reg_2  |
|
| STORE    | 000011 | Copies data in a regstier to a <br/>memory address for long term storage  | mem[op_reg_1_addr] <- op_reg_2 |
|

After the OPCODE, the remaining bits in the instruction are normally referred to as the “operands”. These are the pieces of data, sometimes presented as memory addresses or sometimes given directly as literals, on which the processor will operate.
The CPU will fetch the data from memory or registers, perform the function, and then return the result to the directed memory address or register.


# MIPS 

The MIPS ISA is a simple instruction set that is broken up into three distinct types of instructions, all 32-bits in length:

- `R-Type or Register` MIPS instructions are used for most arithmetic and 
logic operations
- `I-Type or Immediate` instructions are used primarily for data transfer and 
immediate operations using constants
- `J-Type or Jump` instructions are used to jump the program to the specific 
instruction, such as in a loop

Along with the instruction types, it also details that each CPU will have 32 registers, each capable of holding a 32-bit piece of data. MIPS operates on data that is stored in the register or with a 16 bit ‘immediate’ piece of data. Immediate data is typically a constant that can be sent to the processor so it doesn’t need to take up space in a register.

MIPS is often used in distributed/embedded technologies because of its RISC architecture and concise instruction set. Some advantages to this in a small system include limited space requirements, increased battery life, and little to no customer interaction.

## Instruction Format

```text
000000 00000 00000 00000 00000 000000
  op    rs    rt    rd   shamt  func
```

| Abbreviation | Definition                          |
|--------------|-------------------------------------|
| op           | OPCODE                              |
| rs           | first source register               |
| rt           | second source register              |
| rd           | destination register                |
| shamt        | bit shift amount                    |
| func         | extra bits for additional functions |

## R-Type Instructions

R-Type instructions are the most common in MIPS and give us a good way of understanding how an ISA defines the process that a CPU goes through when receiving data.

All R-type instructions have an op of ‘000000’ which signifies to the processor to look at the func bits to determine which process to execute.

The three references to registers, (rs, rt, rd) directly call them by number. There are 32 registers in a MIPS system and the five bits will produce 32 numbers (0 as 00000 to 31 as 11111). The first two (rs & rt) are the operands and the last (`rd) is where to store the result.

The shift amount is used to shift the number by the amount in the shift bits, for our purposes this will always be 00000, meaning no shift. The last six bits are the function to be performed on the operands.

Let’s take a look at this example instruction:

```text
000000 00101 10010 00110 00000 100000
  op    rs    rt    rd   shamt  func
```

- op -> 000000 signifies an R-Type instruction
- rs -> 00101 gets contents in Register 5
- rt -> 10010 gets contents in Register 18
- rd -> 00110 sets the result in Register 6
- shamt -> 00000 means there is no shift
- func -> 100000 function signature for adding

Our processor will add the contents of Register 5 (16) and Register 18 (103) and store that result (119) into Register 6. In the example, these numbers are shown as integers, but in the registers they will be stored in binary. Notice that the first register is always 0 and is a protected register, this is common in most ISAs.