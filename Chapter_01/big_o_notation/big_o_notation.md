# Grokking Algorithms
## Big O Notation

- Big O notation is special notation that tells you how fast an algorithm is.
- Algorithm running times grow at different rates.
- As an example run times for binary versus simple search do not grow at the same rate.
- As number of items increases binary search takes a little more time to run; but simple search takes a lot more time to run.
- Algorithm speeds are not measured in seconds, but in growth of the number of operations.
- Big O notation speaks to how quickly the run time of an algorithm increases as the size of the input increases.
- Big O notation is about the worst case scenario.
- Run time of algorithms is expressed in Big O notation.

## Some Common Big O Run Times

- O(log n) : also known as log time. Example: Binary Search.
- O(n) : also known as linear time. Example: Simple Search.
- O(n * log n) : also known as a fast sorting algorithm. Example: Quick-Sort.
- O(n<sup>2</sup>) : also known as a slow sorting algorithm. Example: Selection-Sort.
- O(n!) : also known as a really slow algorithm. Example: The Traveling Salesman.

## Some Additional Notes

- Logs are the flip of exponentials.
  - 10<sup>2</sup> = 100 <-> log<sub>10</sub>100 = 2
  - How many 10s do we multiply together to get 100
- O(log n) is faster then O(n), but it gets a lot faster as the list of items you're searching grows.
- The Traveling Salesman is one of the unsolved problems in computer science. There's no fast known algorithm for it. Best solution is an approximate solution.





