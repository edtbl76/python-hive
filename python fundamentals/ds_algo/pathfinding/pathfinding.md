# Pathfinding

The algorithmic concept of finding the shortest path between point A and 
point B on a graph. We can find pathfinding algorithms implemented in many 
location-based applications. 

 One example of pathfinding in the real-world is GPS software! When using 
  a GPS for getting directions, the software is given two points: a 
  starting location and an ending location. Then, the program calculates 
  the shortest viable route for the user to take in order to get to their 
 destination.

 Pathfinding is also used in video games with grid-based terrains. Think 
  of a game where your character is being chased by an enemy NPC. A 
  pathfinding algorithm is used to find the quickest path from the NPC’s 
 location to your character’s location.


## Types of Pathfinding Algorithms

 There are two different types of pathfinding techniques that are covered 
 in this course: Dijkstra’s algorithm and A* algorithm.

 Using a dictionary and a min-heap, `Dijkstra’s `algorithm finds the 
  shortest path by calculating the distance between a starting vertex and 
  every other vertex in a graph and keeping track of the path with the 
 smallest distance.

 The` A*` algorithm is a modification of Dijkstra’s algorithm. A* works by 
  having both a starting vertex and a target vertex. The algorithm 
  computes an estimated distance, or heuristic, for all possible paths 
  between the starting vertex and the goal vertex and then selects the 
 shortest one.
 
---
