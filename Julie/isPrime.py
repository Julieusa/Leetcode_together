# Your code needs to read a positive integer n from the standard input stream (console),
# then calculate all prime numbers in the interval [1,n], 
# calculate the result and print it to the standard output stream (console) , each prime number occupies one line.

n = int(input())
for i in range(2, n + 1): # [2,n]
    isPrime = True
    for j in range(2, int(pow(i, 0.5)) + 1): #  find whether exit factors of i in [2, sqrt(i)]
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
