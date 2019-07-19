Add your answers to the Algorithms exercises here.

# Exercise 1

---

a) This function runs in `O(n)` Time Complexity. As the size of n increases, so to does the number of iterations the function will go through. With

b) the first range loop taking in `n` gives the first O(n), then the second and third nested loops also utilize n making it O(n^2) on the first nesting and O(n^3) on the third nested loop. The fourth nested loop is a constant time of 9 iterations any time the functions gets into that part of the loop so that loop is an O(1) which we ignore due to the `O(n^3)` being the dominant evaluation

c) This function is running `O(n)` Time Complexity because each time it calls itself, it does so with one less `n` (bunnies). Therefore the time to run directly correlates to the size of `n`

# Exercise 2

---

If the given number of eggs is not in question and it is just a matter of finding the floor where the egg breaks with the least amount of possible eggs, I would start with using a divide and conquer method. On the first drop, you would drop from the middle floor (n // 2) and eliminate half of the building at once, losing one egg in the process if it breaks. If it breaks, that is the upper half of floors gone, if it does not, that is the lower half of the floors gone, repeat chuncking the building into these halfs until the target floor is acquired. Using the binary search would make this function `O(log(n))` Time Complexity
