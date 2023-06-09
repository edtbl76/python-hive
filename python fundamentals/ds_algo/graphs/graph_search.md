# Graph Search Conceptual

Two Common Approaches

- `Depth-First Search (DFS)` follows each possible path to its end
- `Breadth-First Search (BFS)` broadens its search from the point of origin 
  to an ever-expanding circle of neighboring vertices

 To enable searching, we add vertices to a list, _visited_. This list is 
  pretty important because it keeps the search from visiting the same 
  vertex multiple times! This is particularly vital for cyclical graphs 
 where you might otherwise end up in an infinite loop.

So how do you calculate the runtime for graph search algorithms?

 In an upper bound scenario, we would be looking at every vertex and every 
  edge. Because of this, the big O runtime for both depth-first search and 
 breadth-first search is O(vertices + edges).
 

---

## Depth-First Search (DFS) Conceptual
 Imagine you’re in a car, on the road with your friend, “D.” D is on a 
  mission to get to your destination by process of elimination. D won’t 
  stop and ask for directions. D just sticks to a chosen path until you 
 reach the end.

 At that point, if the end wasn’t actually your destination, D brings you 
  back to the last point when there was an intersection and tries another 
 path.

 Like your friend D, depth-first search algorithms check the values along 
 a path of vertices before moving to another path.

 While this isn’t exactly ideal when you want to find the shortest path 
  between two points, DFS can be very helpful for determining if a path 
 even exists.

 In order to accomplish this path-finding feat, DFS implementations use 
  either a stack data structure or, more commonly, recursion to keep track 
 of the path the search is on and the current vertex.

 In a stack implementation, the most recently added vertex is popped off 
  the stack when the search has reached the end of the path. Meanwhile, in 
  a recursive implementation, the DFS function is recursively called for 
 each connected vertex.
 

---

## Breadth-First Search (BFS) Conceptual

 You’re back in a car, but this time, your friend “B” is navigating. 
  Unlike D, B is a bit hesitant about whether you’ve gone the right way 
  and keeps checking in to see if you are on the best path. At each 
  intersection, B tries out each possible route one by one, but only for a 
 block in each direction to see if you’ve found your destination.

 Like B, breadth-first search, known as BFS, checks the values of all 
 neighboring vertices before moving into another level of depth.

 This is an incredibly inefficient way to find just any path between two 
  points, but it’s an excellent way to identify the _shortest path_ between 
  two vertices. Because of this, BFS is helpful for figuring out 
 directions from one place to another.

 Unlike DFS, BFS graph search implementations use a queue data structure 
  to keep track of the current vertex and vertices that still have 
  unvisited neighbors. In BFS graph search a vertex is dequeued when all 
 neighboring vertices have been visited.


---

- You can use a graph search algorithm to traverse the entirety of a graph 
data structure to locate a specific value
- Vertices in a graph search include a “visited” list to keep track of 
  whether or not each vertex has been checked
- Depth-first search (DFS) and breadth-first search (BFS) are two common 
  approaches to graph search
- The runtime for graph search algorithms is O(vertices + edges)
- DFS, which employs either recursion or a stack data structure, is useful 
  for determining whether a path exists between two points
- BFS, which generally relies on a queue data structure, is helpful in 
  finding the shortest path between two points
- There are three common traversal orders which you can apply with DFS to 
  generate a list of all values in a graph: 
  - pre-order, 
  - post-order
  - reverse post-order