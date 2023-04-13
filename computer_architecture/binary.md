`byte`: 8 bits

`word (aka binary word)`: 16 bites/ 2 bytes.

`Least Significant Bit (LSB)`: Right-Most Bit 

`Most Significant Bit (MSB)`: Left-most Bit


| Decimal | Binary | twos |
| --- | --- | --- | 
| 1 | 1 | 2^0 |
| 2 | 10 | 2^1 |
| 3 | 11 | | 
| 4 | 100 | 2^2 |
| 5 | 101 | | 
| 6 | 110 | | 
| 7 | 111 | | 
| 8 | 1000 | 2^3 |
| 9 | 1001 | | 
| 10 | 1010 | | 
| 11 | 1011 | | 
| 12 | 1100 | | 
| 13 | 1101 | | 
| 14 | 1110 | | 
| 15 | 1111 | | 
| 16 | 10000 | 2^4 | 
| 17 | 10001 | | 
| 18 | 10010 | |
| 19 | 10011 | | 
| 20 | 10100 | | 
| 21 | 10101 | | 
| 22 | 10110 | | 
| 23 | 10111 | | 
| 24 | 11000 | | 
| 25 | 11001 | | 
| 26 | 11010 | | 
| 27 | 11011 | | 

### TRICKS

 The highest a binary number can be is 2n - 1, where n is the number of 
 digits in the binary number.

 011010001010 is 12 digits long; therefore, the highest number that can be 
 represented in binary with these digits is 4095:
 
# Decimal to Binary Conversion
 Converting from binary to decimal can get tedious, especially as our 
  binary data grows in length. Lucky for us, converting from decimal to 
 binary is very straightforward.

 The method we will use only requires us to be able to divide by 2, hence 
 its name, _Division-by-2 Method._

Whenever we divide a number we always have two answers:

- the result (also known as quotient)
- the remainder

 If our remainder is 0, we normally don’t include it when we give the 
 answer but it is still there.

- 35 / 7 = 5 remainder 0
- 36 / 7 = 5 remainder 1

 When we divide by 2 we will always end up with a remainder that is either 
 a 1 or a 0, in other words, binary digits.

 The Divide-By-2 method will continue dividing a number by two until the 
  result, the first part of the answer, is 0. The first time we divide, 
  the remainder goes in the LSB column. Each time we divide after that, 
 the remainder is written as the next digit to the left.

 We can use our even/odd trick we learned to check if we’ve got the right 
 digit in the LSB. Odds will always be 1‘s and evens will be 0‘s.

Follow along with the conversion of 2710 to binary:

| Dividend10	| Divisor10|	Result10 |	Remainder10	| Cumulative Binary2 |
| --- | --- | --- | --- | --- |
| 27 (odd)	|2 |	13	|1 -> LSB|	1
| 13 (odd)	|2 |	6	|1	|11
| 6 (even)	|2 |	3	|0	|011
| 3 (odd)	|2 |	1	|1	|1011
| 1 (odd)	|2 |	0	|1 -> MSB	11011


**Answer: 2710 = 110112

---
