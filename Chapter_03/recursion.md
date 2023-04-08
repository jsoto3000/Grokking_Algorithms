# Grokking Algorithms - Chapter 3

## Recursion
  - Coding technique used in many algorithms.
  - Elegant way to solve problems.
  - Learn how to break problem down into a base case and recursive case.
    - Divide and Conquer strategy uses this simple concept to solve difficult problems.
  - Recursion is used when it makes the solution clearer.
  - There is no performance benefit to using recursion.
    - Loops are sometimes better for performance.
    - Leigh Caldwell (stackoverflow.com) quote:
      - "Loops may achieve a performance gain for your program."
      - "Recursion may achieve a performance gain for your programmer."  


## Pseudocode
  - High level description of problem
  - Written like code, but closer to human speech

## Recursive Functions
  - Many important algorithms use recursion.
  - It's easy to write a recursion function incorrectly that ends up in an infinite loop.
    - Recursion function calls itself.
  - Every recursion function has two parts:
    - (1) Recursive Case:
      - When function calls itself.
    - (2) Base Case:
      - When function doesn't call itself again.
        - So it does not go into an infinite loop.