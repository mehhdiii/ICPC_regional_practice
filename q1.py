from cgi import test


def checker(testcase):
    stdnts = testcase[0]
    testcase = testcase[2:]
    out = []
    for indx, i in enumerate(testcase):

        smallcount = 0
        bigcount = 0
        for indxj, j in enumerate(testcase[indx+1:]):
            if j > i:
                bigcount +=1
            elif j<i:
                smallcount +=1
        if bigcount >= smallcount:
            if len(out)==0:

                out.append(i)
            elif out[-1] < i:
                out.append(i)
                
        
            # else:
    if out[-1] < testcase[-1]:
        out.append(testcase[-1])

    if len(out)>7:
        out = out[:7]
        
    return out


n = int(input())

for i in range(n):
    testcase = list(map(int, input().split(' ')))
    
    out = checker(testcase)
    print('Case #'+str(i+1)+': ' + str(len(out)), end = ' ')

    outstr = ''
    for x in out:
        outstr =  outstr + str(x)+' '

    outstr= outstr[:-1]

    print(outstr)
