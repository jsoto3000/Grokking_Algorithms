# Grokking Algorithms - Chapter 4

## Divide & Conquer Strategy (D&C)

- Have problem that cannot be solved with learned algorithms
- Then use D&C, well known recursive technique for problem-solving
- D&C is not a simple algorithm to apply to a problem
  - Instead it is a way to think about a problem 
- Farmer with a plot of land
  - 1680 meters by 640 meters rectangular plot
  - Need to evenly divide farm into square plots
  - want plots as big as possible
  - how do you figure out the largest square size you can use for a plot of land?
    - Note: this is at its most basic a 'greatest common denominator' (GCD) problem
    - To solve a problem using D&C there are two steps:
      - (1) Figure out the base case (simplest possible case)
      - (2) Divide or decrease your problem until it becomes the base case
      - Base Case (the easiest case)
        - If one side is a multiple of the other
          - Have a plot of land where one side is 50 meters and the other side is 25 meters
          - Largest plot of land you can have is 25 meters by 25 meters
      - Recursive Case
        - According to D&C, with every recursive call you have to reduce your problem
        - Figure out how to reduce your problem and get to the base case.
        - Use a recursive Euclidean Algorithm to find the GCD.
          - In this case the answer is 80.  

## Binary Search is a D&C algorithm too.
- Base case for Binary Search ia an array with one item
  - if the item you're looking for in the array, you found it!
    - Otherwise, it is not in the array.
  - In Recursive case split the array in half
    - throw away one half
    - search on other half  

## Quicksort
- A sorting algorithm
- Much faster than selection sort
- One of the fastest sorting algorithms
- Frequently used
- Uses D&C
- Use Quicksort to sort an array
  - Base Case
    - Empty arrays and arrays with only one element
  - Recursive Case
    - Any array with two or more elements
  - The average runtime of quicksort is O(n log n)
    - but in worst case it takes O(n<sup>2</sup>)
  - The constant in Big O notation can matter sometimes
    - That's why quicksort is faster than Merge Sort
    - However, the const almost never matters for simple search vs binary search
      - O(log n) is os much faster than O(n) as list gets bigger

## Big O Notation
- How long would each of these operations take in Big O notation?
  - Printing the value of each element in an array
    - O(n)
  - Doubling the value of each element in an array
    - O(n)
  - Doubling the value of just the first element in an array
    - O(1)
  - Creating a multiplication table with all the elements in the array
    - if array is [2, 3, 7, 8, 10]
    - first multiply every element by 2
    - then multiply every element by 3, then by 7, and so on
    - O(n<sup>2</sup>)

## Inductive Proof
- a way to prove that your algorithm works
- has two steps:
  - base case
  - inductive case
- method for proving that a statement P(n) is true for every natural number n,
  - that is, that the infinitely many cases P ( 0 ) , P ( 1 ) , P ( 2 ) , P ( 3 ) , … all hold. 
  - Informal metaphors help to explain this technique: such as falling dominoes or climbing a ladder:
    - Mathematical induction proves that we can climb as high as we like on a ladder:
      - by proving that we can climb onto the bottom rung (the basis or base case), and 
      - that from each rung we can climb up to the next one (the step or inductive case).
