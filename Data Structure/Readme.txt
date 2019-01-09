This folder contains following Data Structure programs .
Data Structure Programs
IMPORTANT NOTE ­ Use Generics to Solve all the Data Structure Programs
1. UnOrdered List
a. Desc ­> Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file
b. I/P ­> Read from file the list of Words and take user input to search a Text
c. Logic ­> Create a Unordered Linked List. The Basic Building Block is the Node
Object. Each node object must hold at least two pieces of information. One ref to
the data field and second the ref to the next node object.
d. O/P ­> The List of Words to a File.



2. Ordered List
a. Desc ­> Read .a List of Numbers from a file and arrange it ascending Order in a
Linked List. Take user input for a number, if found then pop the number out of the
list else insert the number in appropriate position
b. I/P ­> Read from file the list of Numbers and take user input for a new number
c. Logic ­> Create a Ordered Linked List having Numbers in ascending order.
d. O/P ­> The List of Numbers to a File.

3. Simple Balanced Parentheses
a. Desc ­> Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.
b. I/P ­> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
c. Logic ­> Write a Stack Class to push open parenthesis “(“ and pop closed
parenthesis “)”. At the End of the Expression if the Stack is Empty then the
Arithmetic Expression is Balanced. Stack Class Methods are Stack(), push(),
pop(), peak(), isEmpty(), size()
d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.


4. Simulate Banking Cash Counter
a. Desc ­> Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.
b. I/P ­> Panel to add People to Queue to Deposit or Withdraw Money and dequeue
c. Logic ­> Write a Queue Class to enqueue and dequeue people to either deposit
or withdraw money and maintain the cash balance
d. O/P ­> True or False to Show Arithmetic Expression is balanced or not.



5. Palindrome­Checker
a. Desc ­> A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.
b. I/P ­> Take a String as an Input
c. Logic ­> The solution to this problem will use a deque to store the characters of
the string. We will process the string from left to right and add each character to
the rear of the deque.
d. O/P ­> True or False to Show if the String is Palindrome or not.

6. Hashing Function to search a Number in a slot
a. Desc ­> Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
efficiently search a number from a given set of number
b. I/P ­> read a set of numbers from a file and take user input to search a number
c. Logic ­> Firstly store the numbers in the Slot. Since there are 10 Numbers divide
each number by 11 and the reminder put in the appropriate slot. Create a Chain
for each Slot to avoid Collision. If a number searched is found then pop it or else
push it. Use Map of Slot Numbers and Ordered LinkedList to solve the problem.
In the Figure Below, you can see number 77/11 reminder is 0 hence sits in the 0
slot while 26/11 remainder is 4 hence sits in slot 4
d. O/P ­> Save the numbers in a file



7. Number of Binary Search Tree
Solve the Problem in the following link
https://www.hackerrank.com/challenges/number­of­binary­search­tree.

8. Write a program Calendar.java that takes the month and year as command­line
arguments and prints the Calendar of the month. Store the Calendar in an 2D Array,
the first dimension the week of the month and the second dimension stores the day
of the week. Print the result as following.

9. Create the Week Object having a list of WeekDay objects each storing the day (i.e
S,M,T,W,Th,..) and the Date (1,2,3..) . The WeekDay objects are stored in a Queue
implemented using Linked List. Further maintain also a Week Object in a Queue to
finally display the Calendar
Note ­ If a particular day has no date then the date is set as empty string and add it
to queue.



10. Modify the above program to store the Queue in two Stacks. Stack here is also
implemented using Linked List and not from Collection Library

11. Take a range of 0 ­ 1000 Numbers and find the Prime numbers in that range. Store
the prime numbers in a 2D Array, the first dimension represents the range 0­100,
100­200, and so on. While the second dimension represents the prime numbers in
that range

12. Extend the Prime Number Program and store only the numbers in that range that are
Anagrams. For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
Further store in a 2D Array the numbers that are Anagram and numbers that are not
Anagram

13. Add the Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Stack using
the Linked List and Print the Anagrams in the Reverse Order. Note no Collection
Library can be used.

14. Add the Prime Numbers that are Anagram in the Range of 0 ­ 1000 in a Queue using
the Linked List and Print the Anagrams from the Queue. Note no Collection Library
can be used.
