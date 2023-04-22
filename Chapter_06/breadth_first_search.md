# Grokking Algorithms - Chapter 6

## Introduction to Graphs

- Shortest-Path Problem
  - trying to find the shortest something
  - algorithm to solve a shortest-path problem is called <b><i>breadth-first search</b></i>  
    - First step is to model the problem as a graph
      - note a graph here does not by definition involve an x or y axis
      - rather, a graph is a set of connections made up of nodes and edges
    - Second step is to solve the problem using breadth-first search.

## What is a Graph

- a graph models a set of connections
- it consists of several nodes
- each node is connected to neighboring nodes
- each graph is made up of nodes and edges  
  - NODE 1 ---edge---> NODE 2
- a node can be directly connected to many other nodes
  - those nodes are called neighbors
- graphs are a way to model how different things are connected to each other
- can use hash tables to express relationships in a graph
  - hash table allows you to map a key to a value
    - the order in which you add the key/value pairs does not matter
- directed graph
  - relationship is only one way between nodes
    - Node 1 ----> Node 2
      - Node 2 is Node 1's neighbor
      - Node 1 is not Node 2's neighbor
- undirected graph
  - no direction, but both nodes are each other's neighbor
    - Node 1 ---- Node 2
      - Node 2 is Node 1's neighbor
      - Node 1 is Node 2's neighbor
- see breadth_search.py

## Breadth-First Search

- a different kind of search algorithm
  - runs on graphs
  - can help answer two types of questions:
    - (1) Is there a path from Node A to Node B
    - (2) What is the shortest path from Node A to Node B
      - prefer a first-degree connection to a second degree connection, and a second-degree connection to a third-degree connection, and so on.
      - should not search any second-degree connection prior to first-degree connections
      - search radiates out from the starting point
      - first degree connections are added to the search list prior to second=degree connections
      - find path from A to B, and also the shortest path
      - Queue
        - need to search in order items are added
        - are similar to stacks
          - cannot access random elements in queue
          - two operations:
            - enqueue (add item; almost the same as push)
            - dequeue (remove item; almost the same as pop)
        - it is a FIFO (first in, first out) data structure
          - versus a stack which is LIFO (last in, first out)
        - search list needs to be in a queue
          - need to search in order items added to list to arrive at shortest path
        - once item is searched need to make sure it is not searched again, to avoid infinite loop
  - can use it to:
    - write a checkers AI that calculates the fewest moves to victory
    - write a spellchecker (fewest edits from your misspelling to a real word; for example, READED -> READER in one edit)
    - find the doctor closest to you in your network
  - Run Time for Breadth-First search
    - run time for search of entire network is at least O(number of edges)
    - breadth-first search algorithm uses a queue to track searched items where adding one item takes constant time: O(1)
      - breadth-first search takes O(V + E)
        - V for number of vertices
        - E for number of Edges
  - See breadth_search.py
  - Topological Sort
    - Task A depends on Task B
      - Task A shows up later in list
      - Morning Routine where:
        - 'shower' depends on 'wake up'
          - note that 'shower' can be moved around
        - 'brush teeth' depends on 'wake up'
        - 'eat breakfast' depends on 'brush teeth'
          - Valid Morning Routine
            - (1) wake up
            - (2) brush teeth
            - (3) eat breakfast
            - (4) shower
          - Invalid Morning Routine (cannot eat breakfast prior to brush teeth)
            - (1) wake up
            - (2) shower
            - (3) eat breakfast
            - (4) brush teeth
    - Way to make an ordered list of the graph
  - Tree
    - special type of graph where no edges ever point back
    - i.e., family tree
      - nodes (people in family tree depicting parent-child relationships)
      - edges (all edges point downward from parent to children)
        - father cannot be grandfather's dad!