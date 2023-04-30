Skip to Content
My Home
Course Menu
Get Unstuck
Tools


Avatar
Technical Interview Problems in Python: Lists: Pair Sum: Optimized
Learn
TECHNICAL INTERVIEW PROBLEMS IN PYTHON: LISTS
Pair Sum: Optimized
We’ll explore a common trade-off: time vs. space.

Our previous solution used nested for loops to iterate through each element in the list and then iterate again for each element in the list to find their sum for a O(N^2) time complexity.

On the bright side, that solution used O(1) space because we’re not using any additional data structures.

If we sort the list before looking for pairs, we can reach O(N * logN) time complexity, but we’re going to go for a O(N) solution by trading away a little space.

Engineering is about trade-offs! This is another opportunity to communicate benefits and drawbacks to the interviewer.

As with other naive solutions, we’re doing more work than is necessary. Given the target integer, what information we can gather in a single iteration?

# <> marks the current element
nums = [4, 2, 8, 9, 6]
target = 8
 
[<4>, 2, 8, 9, 6]
# target - 4 = 4
# we need another 4...
 
[4, <2>, 8, 9, 6]
# target - 2 = 6
# we need a 6...
 
[4, 2, <8>, 9, 6]
# target - 8 = 0
# we need a 0...
 
[4, 2, 8, <9>, 6]
# target - 9 = -1
# we need a -1...
 
[4, 2, 8, 9, <6>]
# target - 6 = 2
# we need a 2...
At each step of the iteration, we know the “complement” number needed to sum to the target.

Use a dictionary to store that complement at each iteration and solve this problem with O(N) time complexity and O(N) space complexity.

Instructions
1.
Write a function pair_sum(), which has two parameters: nums and target.

pair_sum() should return a list containing a single pair of indices whose values sum to target. This can be any pair that meets the requirements.

If no such values exist, return None.

Your solution should run in O(N) time and O(N) space!

Checkpoint 2 Passed

Stuck? Get a hint
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
1234567891011121314151617181920212223
# pair sum
# linear time, linear space requirement
# return list of indices that sum to target

def pair_sum(nums, target):
  complements = {}
  indices = {}
  for i in range(len(nums)):
    x = complements.get(nums[i], None)
    if x is not None:

Run


View solution
Output:
None
 should equal any of 
[[1, 3], [0, 4]]
 False

None
 should equal any of 
[[5, 6]]
 False

None
 should equal 
None
 True

None
 should equal any of 
[[0, 2], [0, 5]]
 False

 
11/12
Back
Next
