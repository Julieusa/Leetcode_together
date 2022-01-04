# This is Julie! 

## My daily progress are as follows.
 ### Day 1(11/05/2021): 
 Review two number sum and code for three number sum. Got O(n^3) solution.
 
 Learned using append to store an array in the list.
 ### Day 2(11/06/2021): 
 Modify code for three number sum to get optimal solution O(n^2). 
 
 Review Validate Subsequence. The key is fixing the value from array, compare each of the elements in the sequence.
 ### Day 3(11/07/2021): 
Sorted Square Array. Use inner function to get O(nlogn) in time but we can get O(n) by using manual sort similarly to two number sum. 

Find smallest difference element from two given array. 
 ### Day 4(11/08/2021): 
Non-Constructible Change. When current coin value greater than the currentchangeCreated+1, we can't make the change. This logic need to be digested. 

Move Element to End. The key is using two index, one in the front and the other one in the end.Use this array[i], array[j] = array[j], array[i] to swap two         element.  
 ### Day 5(11/09/2021): 
Monotonic Array: learn to use a flag

Spiral Traverse

 ### Day 6(11/10/2021):
Looking for missing numbers: Learn to read the standard input stream (console)by using input() and transform it to certain type. 
1. Using split() and Map(): 
Split() function helps in getting multiple inputs from users. It breaks the given input by the specified separator. If a separator is not provided then any white space is a separator. Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs.
Map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable.Use the Python Map Function to transform the list of strings to a list of integers.

Find all prime numbers in [1,n]

 ### Day 7(11/11/2021):
Find the longest peak length

 ### Day 8(11/12/2021):
Find the product of array

 ### Day 9(11/13/2021):
Find the first duplicate value in array

Learn about using set() in python:A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes like we do in lists. https://www.geeksforgeeks.org/sets-in-python/

Need to find more examples to practice the idea of using set().

 ### Day 10(11/14/2021):
Merge overlapping intervals
Learn to sort an array by a key parameter.

 ### Day 11(11/15/2021):
Four number sum.
Consider about adding two number sum

 ### Day 12(11/16/2021):
Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array tp be sorted.

 ### Day 13(11/17/2021):
 Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integres contained in that array.
 
 Need to use the hash table again. 

 ### Day 14(11/18/2021):
 Write a function that takes in a list of scores and returns the Minimum number of rewards that you must give out to students to satisfy the two rules.
 1. All studetns must receive at least one reward.
 2. Any given students must receive strictly more rewards than an adjacent students( a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score. 
 Understand the second rule is important. 
 
 ### Day 15(11/20/2021):
 Redo minmum reward question. 

 
 ### Day 16(11/21/2021):
 Zigzag traverse:
Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a zigzag parttern all the way to the bottom right corner. 

Figure out the partern for the index changing is important. In general, separate them to two way, one is go down-left and the other one is go up-right. Then need to consider the border case. 

 ### Day 17(11/22/2021):
 Fnd the max sum of non-adjacent elemnets. Understand the skills for Dynamic programming, it's bottom-up pattern.
 Max(i) = max{max(i-1), max(i-2)+current elements}
  
 ### Day 18(11/23/2021):
 Find the number of ways to make changes for the target amount using the given coin denominations.
 		if denom <= amount: 
				ways[amount] += ways[amount-denom]
				
				
### Day 19(11/24/2021)
Find the minimum number of coins to make a change for the target amount using the given coin denominations. 
In order to compare with last question, I merge the solution to the same file.  

### Day 20(11/28/2021)
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the forst string to obtain the second string. 

At any position (i,j) in the two-dimensional array, if str2[i] is equal to str1[j], then the edit distance at position(i,j) is equal to the one at position (i-1, j-1), since adding str2[i] and str1[j] to the substrings represented at position (i-1, j-1) does not require any additional edit operation. if str2[i] is not equal to str1[j], then the edit distance at position (i, j) is equal to 1+the minimum of the edit distances at positions (i-1, j), (i, j-1), (i-1,j-1). 
<img width="543" alt="Screen Shot 2021-11-28 at 5 42 41 PM" src="https://user-images.githubusercontent.com/30751636/143826203-81e24940-4157-48f8-a995-bc7da1bc891a.png">

### Day 21(11/29/2021)
Modify levenshteinDistance.py for a better solution. We only need to store two rowes in the process of updating 


### Day 22(12/2/2021)
Find the number of ways to reach the bottom right corner of the given grid-shaped, rectangular graph.
Three methods: recursive, dynamical programming, useing math idea of permutatons 

Start 2 weeks study plan for algorithm 1 on Leetcode:
  Day 1: Binary search, First Bad Version, Search Insert Position 

### Day 23(12/3/2021)
2 weeks study plan for algorithm 1 on Leetcode:
  Day 2: Two Pointers:Squares of a Sorted Array,  Rotate Array(This one need to digest again)

### Day 24(12/4/2021)
2 weeks study plan for algorithm 1 on Leetcode:
  Day 3:  Two Pointers: Move zeros,  Two sum
  
### Day 25(12/5/2021)
2 weeks study plan for algorithm 1 on Leetcode:
  Day 4:  Two Pointers: Reverse string, reverse words in a string for a sentence 

### Day 25(12/8/2021)
2 weeks study plan for algorithm 1 on Leetcode:
  Day 6:  Sliding Window
  Need to learn more about string!! 
  Day 5 is List, I don't know how to use it. 
  
### Day 26(12/9/2021)
2 weeks study plan for algorithm 1 on Leetcode:
  Day 7:  Breadth-First Search / Depth-First Search
  Use recurceive or iterative(better), the second question need use Stack!

### Day 27(12/10/2021)
2 weeks study plan for algorithm 1 on Leetcode:
  Day 8 is about DFS/BFS for trees. I don't understant those. Need to learn.
  Day 9:  Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell. This question is interesting but I don't really understand the solution. Need to be figured out. 
      Use Dynamic programing. 
      
### Day 27(12/11/2021)
2 weeks study plan for algorithm 1 on Leetcode:     
  Day 10: Iteration or recursion for linked list. Learn how to use list and change pointer. Need to practice more for linked list structure. 

### Day 28(12/27/2021 - 12/28/2021) 
 Study Hash table and Linked list. 
 Design a linked list and hash table(HashSet and HashMap).
 ![image](https://user-images.githubusercontent.com/30751636/147639713-ef6f2c15-3e67-431b-aaed-2bec86f6f08c.png)

 Pratical application of HashSet: contain duplicates(only duplicate), single number, Intersection of two arrays(*, return unique element), Happy number(*).https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
 
 ### Day 29(12/29/2021) 
Pratical application of HashMap:
  Two Sum: each element can only be used once
  Contain Duplicates II (duplicates in given k distance), 
  Intersection of two arrays II (*, return all common elements which might not be unique)
  Isomorphic Strings: need to build map between two strings. 
        zip(s, t):use in for loop, return iterate same index pair like (s[0], t[0]), (s[1], t[1]), (s[2], t[2])...
  First Unique Character in a String
        collections.Counter(s:string):A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
	
 ### Day 30(12/30/2021)
 Practical Application - Design the Key:
 Group Anagrams:# The use of collections.defaultdict
 Collections:  It's a module that implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
 ![image](https://user-images.githubusercontent.com/30751636/147867330-db39389c-c57a-40cf-98c5-cac0d92f626e.png)

 Defaultdict(type):a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary.  The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet). The "default" is created by the defined type, e.g list if given type=list. 
 Tuple: Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
 Tuples are used to store multiple items in a single variable. Tuple items can be of any data type 
   
 ### Day 31(12/31/2021)
 Linked list :https://leetcode.com/explore/learn/card/linked-list/
 To get a value in the linked list, we need to start from the head to search it.
 ![image](https://user-images.githubusercontent.com/30751636/147867479-932924f4-505f-49b5-8f29-19f972874c42.png)
 Singly linked list: It has two attributes val and next.
 Two pointer technique: Circle in linked list, Intersection of two linked lists(*), Remove the nth node from the linked list(*)
 ![image](https://user-images.githubusercontent.com/30751636/147867497-47c388a5-3928-4570-835b-1b77704dc5f3.png)
 
 
  ### Day 32(1/1/2022)
  Classical problems for linked list
  Reversed linked list: Need use two pointer.  A node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. 
  Remove linked list element:  Add one sentinel node as a sudo-head to make the remove easier. 
  Odd-Even linked list: Seperate it to two lists as oddlist and evenlist then combine them. 
  Palindrome Linked List: Copying the linked list into an array then use two pointer(one for the head the other one for the tail), loop through middle element.
  Doubly linked List: It has one more refence field as "Prev", it makes delete element easier. We no longer need to traverse the linked list to get the previous node, both the time and space complexity are O(1).
  

 ### Day 33(1/2/2022)
   Conclusion problems for linked list:
   Merge Two sorted list, Add two numbers: always create a new LinkNode and a pointer, one for update solution linked list, the other one as a pointer to current node. Be careful the solution will return head.next, since the head is psudo head. 
   
 ### Day 34(1/3/2022)  
   Review linked list, start recursion algorithm to prepare for dynamic programming algorithm. 
   https://leetcode.com/explore/learn/card/recursion-i/
