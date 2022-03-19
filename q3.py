def checkprime(n):

    for i in range(2, n):

        if n%i==0:
            return False
    return True

def outter(n1, n2):

    u = checkprime(n1)
    v = checkprime(n2)
    # print(u, v)
    if u and v:
        return n1+n2
    elif u or v:
        return n1*n2
    else:
        return 'not possible'
n = int(input())

for i in range(n):
    testcase  = list(map(int, input().split(' ')))
    n1 = testcase[0]
    n2 = testcase[1]

    outstr = outter(n1, n2)

    
    print('Case #', i+1, ': ', outstr, sep ='')