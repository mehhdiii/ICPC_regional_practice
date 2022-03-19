def denom(n):
    lst = [5000, 1000, 500, 200, 100, 50, 20, 10]
    out = {}
    # out = []
    # for i in range(lst):
    #     out.append(0)
    flag = 0
    for i in lst:
        if n//i<1:
            if flag==1:
                out[i] = 0
        else:
            flag=1
            out[i] = n//i
            
            n = n%i

        
    return out



n = int(input())


for i in range(n):
    x = int(input())
    
    
    print('Case #', i+1, ': ', sep='', end='')

    out = denom(x)
    outstr = ''
    for i in out.keys():

        outstr += str(out[i])+ 'x'+ str(i)+ ', '
    print(outstr[:-2])
