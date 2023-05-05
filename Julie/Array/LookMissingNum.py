# Description
# Please obtain a positive integer n and an array A from the standard input stream (console). 
# The array A contains a total of n - 1 integers, and the range of n - 1 integers is in the interval [1,n] (no repetition), 
# find out the number that does not appear in the array in the range of [1,n], 
#and output the number to the standard output stream through the print statement (control station).


def missing(n,A):

    A.sort()
    A.append(-1) 
    for i in range(n):
        if int(A[i]) == i + 1:
            continue
        print(i + 1)
        break

n = int(input())
A = input().split()
A = list(map(int, A))
missing(n,A)
