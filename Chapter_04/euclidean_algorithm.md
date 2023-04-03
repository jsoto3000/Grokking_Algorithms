# Grokking Algorithms - Chapter 4
## Euclidean Algorithm
Source: Khan Academy

- The Euclidean Algorithm 
  - The Greatest Common Divisor (GCD) of two integers A and B is the largest integer that divides both A and B.  

- The Euclidean Algorithm is a technique for quickly finding the GCD of two integers.  
- The Euclidean Algorithm for finding GCD(A,B) is as follows:
  - If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.
  - If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
  - Write A in quotient remainder form (A = B⋅Q + R)
  - Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)

- Understanding the Euclidean Algorithm 
  - If we examine the Euclidean Algorithm we can see that it makes use of the following properties:
    - GCD(A,0) = A 
    - GCD(0,B) = B 
    - If A = B⋅Q + R and B≠0 then GCD(A,B) = GCD(B,R) where Q is an integer, R is an integer between 0 and B-1

  - The first two properties let us find the GCD if either number is 0. The third property lets us take a larger, more difficult to solve problem, and reduce it to a smaller, easier to solve problem.
  - The Euclidean Algorithm makes use of these properties by rapidly reducing the problem into easier and easier problems, using the third property,  until it is easily solved by using one of the first two properties.

