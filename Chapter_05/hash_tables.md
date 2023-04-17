# Grokking Algorithms - Chapter 5

## Hash Tables

- One of the most useful basic data structures
  - Also known as:
    - Hash Maps
    - Maps
    - Dictionaries
    - Associative Arrays
  - Hash Function with an Array
  - They are very fast
  - Have many uses
  - data structure with extra logic behind it
  -  arrays and lists map straight to memory but hash tables are 'smarter'  
  - intelligently figures out where to store elements
    - Internals of Hash Tables
    - implementation
    - collisions
    - hash functions 
  - Arrays and lists map straight to memory but Hash Tables are smarter  
  - Hash Tables are also extremely fast
    - Average case takes O(1)
    - O(1) is called constant time
      - does not mean instant
      - means time remains same regardless of size of Hash Table
  - Will likely never need to implement hash tables yourself
    - Any good programming language will have an implementation
    - Python has Hash Tables
      - See book.py
  - A hash table has keys and values
    - it maps keys to values
  - It's important for hash functions to consistently return the same output to the same input
    - if not, will not be able to find item after adding it to the hash table  
      - f(x) = 1 is consistent
      - f(x) = rand() is not consistent
      - f(x) = next_empty_slot() is not consistent
      - f(x) = len(x) is consistent


<div style="margin-left: auto;
            margin-right: auto;
            width: 75%">

--| simple search      | Binary Search          | Hash Function
----|--------------------|------------------------|----
<i><b> # of items in book </i></b>| <i><b>O(n)</i></b> | <i><b>O(Log n)</i></b> | <i><b>O(1)</i></b>
100| 10 sec             | 1 sec                  | Instant
1000| 1.6 min            | 1 sec                  | Instant
10000| 16.6 min           | 2 sec                  | Instant

</div>

## Hash Functions
- A function where you put in a string and you get back a number
  - string here means any kind of data
    - a sequence of bytes
- Maps strings to numbers
- Requirements for a hash function
  - needs to be consistent
  - should map different words to different numbers

<div style="margin-left: auto;
            margin-right: auto;
            width: 90%">

Array| Index Position 0 | Index Position 1 | Index Position 2    | Index Position 3| Index Position 4
----|------|-------|---------------------|----|----
<i><b>items</i></b>| <i><b>Milk</i></b> | <i><b>cheese</i></b> | <i><b>bread</i></b> | <i><b>apple</i></b> | <i><b>avocado</i></b> 
item prices| 1.49 | 0.79  | 2.49 | 0.67 | 1.49 

</div>

- consistently maps a name to the same index
  - everytime put in 'avocado' get same number (price) back
- maps different strings to  different indexes
  -  Avocado maps to index 4
  -  Milk maps to index 0
- knows how big the associated array is and only returns valid indexes
  - if array is len(5) will not return index 100
    - index 100 is invalid  

## Use Cases  

- Using Hash Tables for Lookups
  - Modeling relationships from one thing to another
  - Phone Book
    - each name has a phone number associated with it
    - add name and associated phone number
    - enter name and get associated phone number
    - see ()
    - Great for:
      - creating a mapping from one thing to another thing
      - looking something up
        - see phone.py
  - mapping web addresses to ip addresses
    - dns resolution
- preventing and filtering out duplicate entries
  - checking for duplicates is very fast with a Hash Table
  - running a voting booth
    - use hash table to track people who voted
      - see vote.py
      - someone comes in to vote check if already in hash
        - returns name value if already voted
        - if not returns none
- Caching
  - Caching/Memorizing data instead of making your server do the work
  - common way to make things faster
  - all large websites use caching
  - data is cashed in a hash table  
  - see cache.py

## Collisions and Performance

- to understand the performance of hash tables you first need to understand what collisions are
- collision occurs when two keys are assigned the same slot  
- Many different ways to deal with collisions
  - Simple Solution:
    - When multiple keys map to same slot, start a linked list at that slot  
    - con: can degrade performance; end up with same result as putting everything in a linked list to begin with  
- Hash function is extremely important
  - maps all keys to a single slot
  - ideally will map keys evenly all over the hash
  - if linked lists get long, it will slow down your hash table
    - but will not get too long if have a good hash function
    - a good hash function will avoid and/or minimize collisions
- Performance
  - O(1) >>> constant time
  - O(n) >>> linear time


<div style="margin-left: auto;
            margin-right: auto;
            width: 75%">

--| Hash Tables (Avg.) | Hash Tables (Worst.) | Arrays | Linked Lists
----|--------------------|----------------------|--------|----
SEARCH| O(1)               | O(n)                 | O(1)   | O(n)
INSERT| O(1)               | O(n)                 | O(n)   | O(1)
DELETE| O(1)               | O(n)                 | O(n)   | O(1)

</div>

- To avoid collisions need:
  - a low load factor
  - good hash function
- Load Factor
  - number of items in a hash table/total number of slots
  - hash tables use an array for storage, so count number of occupied slots
  - having a load factor greater than 1 means you have more items than slots in your array  
  - resizing:
    - once the load factor starts to grow, need to add more slots to the hash table  
  - with a lower load factor have fewer collisions
    - table will perform better
    - good rule of thumb: resize when ;oad factor greater than 0.7
    - resizing is expensive!
      - however, on average hash tables take O(1) time even with resizing
- Good Hash Function
  - a good hash function distributes values in the array evenly
  - a bad hash function groups values together and produces a lot of collisions  
  - it is important for hash functions to have a good distribution
    - they should map items as broadly as possible
    - worst case for a hash table is when the hash function maps all items to the same slot
- Have Four Hash Functions that work with strings:
  - (A) Return "1" for all input
  - (B) Use the length of string as the index
  - (C) Use the first character of the string as the index: so, all strings starting with a are hashed together, and so on.
  - (D) Map every letter to a prime number: a = 2, b =3, c = 5, d = 7, e =11 , and so on. For a string, the hash function is the sum of all the characters modulo the size of the hash. i.e., if the string is "bag", the index is 3 + 2 + 17 % 10 = 22 % 10 = 2  
  - For each example below, which of the four hash function(s) listed above will provide a good distribution (assume a hash table size of 10 slots)  
    - phonebook where keys are names and values are phone numbers. Names are as follows: Esther, Ben, Bob, and Dan
      - C & D
    - mapping from battery size to power. Sizes are A, AA, AAA, AAAA
      - B & D
    - mapping from book titles to authors. Titles are Maus, Fun Home, and Watchmen
      - B, C, and D
- Recap
  - Will most likely never have to implement a hash table yourself
    - programming language you use should provide it
    - Python's hash tables get the average case performance: constant time >>> O(1)
    - hash tables are a powerful data structure
      - extremely fast
      - let you model data in a different way
    - can make a hash table combining a hash function with an array
    - collisions are bad
      - need a hash function that minimizes collisions
    - hash tables have really fast search, insert, and delete capabilities  
    - hash tables are good for modeling relationships from one item to another
    - once your hash table's load factor is greater than 0.7, it is time to resize it
    - hash tables are good for caching data (i.e., web server)  
    - hash tables are great for catching duplicates