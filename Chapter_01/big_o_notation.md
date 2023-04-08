# Grokking Algorithms - Chapter 1
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

<div style="margin-left: auto;
            margin-right: auto;
            width: 50%">

Big O Notation|Run Time|Example
----|----|----
O(log n)|log time|Binary Search
O(n)|linear time|Simple Search
O(n * log n)|fast sorting algorithm|Quick-Sort
O(n<sup>2</sup>)|slow sorting algorithm|Selection-Sort
O(n!)|a really slow algorithm|The Traveling Salesman.


</div>

## Some Additional Notes

  - Logs are the flip of exponentials.
    - 10<sup>2</sup> = 100 <-> log<sub>10</sub>100 = 2.
    - How many 10s do we multiply together to get 100.
  - O(log n) is faster then O(n), but it gets a lot faster as the list of items you're searching grows.
  - The Traveling Salesman is one of the unsolved problems in computer science. There's no fast known algorithm for it. Best solution is an approximate solution.





