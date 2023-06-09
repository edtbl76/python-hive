# Depth-First Search: Conceptual

##  Depth-First Search Algorithm
Depth-First Search is an algorithm used for searching tree data 
structures for a particular node, or node with a particular value 
associated with it. Depth-First Search is also more generally used as a 
tree traversal algorithm, specifying an order in which to exhaustively 
access all nodes of a tree. The algorithm begins at the root node and 
explores deeper into the tree until it reaches a leaf node. Only then 
 will it back-track up the tree until it finds an unexplored child node. 
 This process continues until the desired node is found, or all nodes have 
been explored.

 There is an intuitive recursive implementation of this algorithm which we 
  will discuss in this article, but this search method can also be 
  implemented with an iterative method that uses a stack to store roots of 
  unexplored subtrees. Consider Breadth-First Search, where we traverse a 
  tree by preferring to explore laterally between siblings before moving 
  to deeper levels. While in Depth-First Search we traverse the tree 
  vertically, from parent to child, before exploring any siblings of that 
  parent. Depth-First Search is an exhaustive search and thus will find 
  the targeted node if it exists in the tree. This, however, has practical 
  implications. If a search tree is very large, or infinite in size, the 
 Depth-First Search algorithm may never halt.

## The Algorithm
### Recursive Implementation
The recursive version of the algorithm works by starting at the root node, and breaking the tree up into subtrees, until it finds the target node, or until every node in the tree has been considered as the root of a subtree. We recursively call the function on all of our root’s children, treating each child node as a root of its own subtree. We define a function that accepts a tree node and a target value as input parameters. The recursive DFS algorithm implements the following logic:

- If the input node value matches our target value then return the input node.
- For each child of the input node, recursively call this function and 
  return the first non-null value returned by a recursive call.
- If this root node has no children, or the recursive calls did not return 
  any node, then return null.

To search a tree with this function, we invoke the function with the root 
  node of our tree.

### Iterative Implementation
 The iterative algorithm does not make use of any recursive calls. Instead,
  we maintain a stack of references to unexplored siblings of the nodes we 
  have already accessed. The recursive algorithm is effectively doing 
  something very similar, but the program call stack is implicitly used to 
  store the path from the root to the current node. With the iterative 
  algorithm, we need to implement a stack ourselves. These two 
  implementations have the same time and space complexity, so the choice 
  of which to implement is usually a matter of personal preference.

# Complexity
 Depth-First Search has a time complexity of O(n) where n is the number of 
 nodes in the tree. In the worst case, we will examine every node of a tree.

 Depth-First Search has a space complexity of O(n) where n is the number 
  of nodes in the tree. In the worst case, we will need to store a 
  reference to every node in a stack. Consider an adversarial example of a 
  linked list as a type of tree with no branching. Trees like this could 
  reach the worst-case space complexity if the target node is the leaf 
  node or is absent from the tree altogether.

## Practical Considerations
DFS is a popular tree search algorithm for its intuitive and concise 
implementations. Depth-First search, and other tree traversal algorithms 
like it, can be found in many modern applications. DFS can be used for 
searching for objects in a data structure like files in a file system.  
More abstract applications can be found in domains like artificial 
intelligence, for example, searching through possible moves in a game like 
chess, or searching for a path through a maze.     
 
Depth-First Search is an exhaustive method, so consider that some trees 
may  be infinitely large or just large enough that they are practically  
impossible to completely traverse. In practice, we can limit the depth  
allowed to search by the algorithm. Consider something like an algorithm  
for playing chess. We can simulate a series of moves and responses, but 
the search space may be so large that no modern computer could reasonably  
explore all possible paths.