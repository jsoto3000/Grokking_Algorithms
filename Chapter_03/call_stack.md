# Grokking Algorithms - Chapter 3  
## Call Stack

- Stack  
  - Simple Data Structure
- Call Stack
  - Important concept in general programming
  - Important to understand when using recursion.
  - It is a simple data structure.
  - Has only two actions:
    - push (insert)
    - pop (remove and read)  

- Call Stack
  - When you call a function from another function:
    - The calling function is paused in a partially completed state

## Call Stack Walk-thru what happens when call a function
  - (see call_stack.py)
  - NOTE: print is a function in Python
    - For this example pretend it is not

<div style="margin-left: auto;
            margin-right: auto;
            width: 50%">

===> Call greet(MAGGIE)  
===> First computer allocates a box of memory for function call

Memory Allocation|
---|

===> Computer uses memory  
===> variable name set to 'MAGGIE'  
===> variable name saved in memory

--------GREET---------|
---|

NAME:| MAGGIE |
---|--------|

===> Every time you make a function call  
===> The computer saves variable values for that call in memory  
===> Next you print, 'Hello, MAGGIE!'  
===> Again computer allocates memory for this function call  
===> The computer is using a stack for these memory boxes  
===> Second function call is added to top of first one  

--------GREET2---------|
---|

NAME:| MAGGIE |
---|--------|

--------GREET---------|
---|

NAME:| MAGGIE |
---|--------|

===> Next you print, 'How are you, MAGGIE?'  
===> Then you return from the function call  
===> When this happens the memory box on top of the stack gets popped off  
===> Now the topmost bix on the stack is the for the greet(MAGGIE) function call  
===> When you called the greet2(MAGGIE) function, the greet(MAGGIE) function was <i>partially completed</i>  
===> This is the main point!  
===> <i><b> When you call a function from another function, the calling function is paused in a partially completed state!</i></b>  
===> Now that you are done with the greet2(MAGGIE) function, you're back to the greet(MAGGIE) function  
===> You pick up where you left off  

--------GREET---------|
---|

NAME:| MAGGIE |
---|--------|

===> Next you print, 'Getting ready to say bye ...'  
===> Then you call the bye() function  
===> A box for that function is now added to the top of the stack  


----------BYE-----------|
---|

--------GREET---------|
---|

NAME:| MAGGIE |
---|--------|

===> Then you print, 'Ok, bye!'
===> Next you return from the function call
===> bye() function is popped off  
===> Your are now back to the greet(MAGGIE) function  

--------GREET---------|
---|

NAME| MAGGIE |
---|--------|

===> There is nothing else to be done!  
===> Finally, return from the greet(MAGGIE) function too!  

</div>

## Call Stack example with Recursion
  - (see call_stack_recursion.py)

<div style="margin-left: auto;
            margin-right: auto;
            width: 50%">

===> fact(x)  
===> first call to fact(x)  
===> x is 3

FACT|
---|

x| 3   |
---|-----|

===> if x == 1  

FACT|
---|

x| 3   |
---|-----|

===> else:  

FACT|
---|

x| 3   |
---|-----|

===> return x * fact(x-1)  
===> <b><i>a recursive call!</b></i>  

FACT|
---|

x| 2   |
---|-----|

FACT|
---|

x| 3   |
---|-----|

===> if x == 1  
===> now we are in the second call to fact(x)  
===> x is 2  
===> the topmost function call is the call we are currently in  

FACT|
---|

x| 2   |
---|-----|

FACT|
---|

x| 3   |
---|-----|

===> else:  
===> note: both function calls have a variable named 'x'    
===> and the value of x is different in both

FACT|
---|

x| 2   |
---|-----|

FACT|
---|

x| 3   |
---|-----|

===> return x * fact(x-1)  
===> you cannot access the top two calls' x from this call and vice versa

FACT|
---|

x| 1   |
---|-----|

FACT|
---|

x| 2   |
---|-----|

FACT|
---|

x| 3   |
---|-----|

===> if x == 1  

FACT|
---|

x| 1   |
---|-----|

FACT|
---|

x| 2   |
---|-----|

FACT|
---|

x| 3   |
---|-----|
 
===> return 1  
===> we made three calls to fact(x), but we had not finished a single call until now  
===> topmost call is first box popped off the stack  
===> it is the first call we return from  
===> it returns 1  

FACT|
---|

x| 2   |
---|-----|

FACT|
---|

x| 3   |
---|-----|

===> return x * fact(x-1)  
===> this is the function call we just returned from   
===> x is 2  
===> returns 2

x| 3   |
---|-----|


===> return x * fact(x-1)  
===> this is the function call we just returned from  
===> x is 3  
===> returns 6  
===> There is nothing else to be done!  


</div>

## Revisit recursive approach to key_search_box pseudocode  
  - while loop approach generates a pile of boxes to search
  - in recursive approach there is no pile
    - pile of boxes is saved on the call stack
    - have a stack of half-completed function calls
      - each with its own half-complete list of boxes to search
    - using stack is convenient
      - cost is that it takes up memory
      - can end up with too tall stack
    - if stack takes up too much memory:
      - re-write code using while loop instead
      - use tail recursion
        - advanced topic outside of scope
        - not supported by all languages
        - Python to date does not support tail recursion