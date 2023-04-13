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
- 