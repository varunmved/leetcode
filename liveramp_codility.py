# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, X, D):
    # write your code in Python 2.7
    x =X
    d = D
    a = A
    
    if x < d:
        #if it can jump the whole distance
        return 0
    elif x<=d + a[0]:
        #it can jump after only the first leaf
        return 0
    else:
        ld = 0
        for i in range(0,len(a)):
            if((a[i] <= d and a[i] >ld) or (a[i] > d and a[i] <= ld + d)):
                ld = a[i]
            if(ld + d >= x):
                return i
            i+=1
        return -1
        



A = [1, 3, 1, 4, 2, 5]
a = solution(A,7,3)
print(a)

