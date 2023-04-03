# Grokking Algorithms - Chapter 2
## Data Structures

- Arrays
  - All elements are stored contiguously (right next to each other) in memory.
  - Since all elements must be contiguous, adding additional items may require to move all the items in the array.
  - Great for reading random elements.
    - Allow random access.
    - Can look up any element in array instantly.
    - Are faster at reads.
  - Elements in array are numbered starting from 0 (not 1).
  - Position of an element is called its index.
  - All elements should be same type (all ints, all doubles, etc.)
  - To insert element in middle need to shift all the rest of the elements down.
    - Also, if no space may need to move all elements altogether.
  - All elements need to be moved up when deleting an element.
####
- Linked Lists
  - Elements can be anywhere in memory. Do not need to be contiguous.
  - Can only do sequential access.
    - Read elements one by one starting at the first elment
  - Each element stores the address of the next element.
  - Never need to move an element.
  - However, needing to jump around linked lists are not ideal.
  - Are better for inserting elements in the middle.
  - Also better for deleting elements.
####
- Run Times for Common Operations on Arrays and Lists

####
<div style="margin-left: auto;
            margin-right: auto;
            width: 50%">

----------|Arrays|Lists
---|---|---
Reading|O(1)|O(n)
Insertion|O(n)|O(1)
Deletions|O(n)|O(1)

</div>

- O(n) = Linear Time. 
- O(1) = Constant Time

## Some Additional Notes

- Insertions into arrays or linked lists can fail if no space left in memory.
  - Deletions will never fail.
- There are two types of access:
  - Random Access
    - Binary search requires random access.
      - Need to get to the middle instantly.
  - Sequential Access
- Arrays have fast reads and slow inserts.
- Linked lists have slow reads and fast inserts.
- Also can have a hybrid data structure.
  - An array of linked lists.
  - Hash table.

## Sorting Algorithms

- Selection Sort
  - Takes O(n<sup>2</sup>) time.
  - Very useful to sort:
    - Names in a phonebook.
    - Travel Dates.
    - Emails (newest to oldest).
  - Good algorithm but not very fast.
- Quick Sort
  - Fast sorting algorithm.



